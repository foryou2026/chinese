# 数据规范 · account-entry

> **归属**：共享
> **关联 R-ID**：app: R-auth-001~016 / admin: R-auth-001~011
> **不做**：状态机定义(C02)、路由/接口(D02)、页面(C03)
> **特殊说明**：auth 模块大量复用 Supabase Auth 内置能力（用户表 `auth.users`、密码哈希、JWT 签发、Token 刷新、Google OAuth）。本文件仅定义 `public` 域下的扩展表，不触碰 `auth.*` 系统表。

---

## 1. ER 图

```mermaid
erDiagram
    AUTH_USERS["auth.users (系统表·只读)"] ||--|| USER_PROFILES : "1:1"
    AUTH_USERS ||--o{ USER_SESSIONS : "1:N"
    AUTH_USERS ||--o{ AUDIT_LOGS : "1:N"
    LOGIN_ATTEMPTS {
        uuid id PK
        text email
        text system_id
    }
    USER_PROFILES {
        uuid id PK
        text auth_provider
        boolean has_password
    }
    USER_SESSIONS {
        uuid id PK
        uuid user_id FK
        text system_id
    }
    AUDIT_LOGS {
        uuid id PK
        uuid user_id FK
        text action
    }
```

---

## 2. 实体/表定义

### user_profiles

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-auth-001, R-auth-003, R-auth-012, R-auth-014 |
| 业务定义 | 用户扩展资料 |
| 状态机 | 无 |

**字段**

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | 无 | 是 | 主键=auth.users.id | 引用 auth.users(id) |
| display_name | text | 否 | null | 否 | 显示名称 | 长度≤50 |
| avatar_url | text | 否 | null | 否 | 头像地址 | 合法URL或null |
| auth_provider | text | 是 | 'email' | 否 | 注册来源 | 枚举:auth_provider_enum |
| has_password | boolean | 是 | true | 否 | 是否有密码 | Google用户为false |

> B01 通用字段 created_at/updated_at 按默认规则携带，不再重复。id 此处不使用 gen_random_uuid()，而是取 auth.users.id 的值。

**关系**

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| auth.users | 1:1 | id | CASCADE |

---

### login_attempts

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-auth-004(app), R-auth-002(admin) |
| 业务定义 | 登录失败计数与锁定 |
| 状态机 | 无 |

**字段**

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| email | text | 是 | 无 | 否 | 尝试登录邮箱 | 邮箱格式 |
| system_id | text | 是 | 无 | 否 | 所属系统 | 枚举:system_enum |
| consecutive_failures | integer | 是 | 0 | 否 | 连续失败次数 | ≥0 |
| last_failure_at | timestamptz | 否 | null | 否 | 末次失败时间 | 无 |
| locked_until | timestamptz | 否 | null | 否 | 锁定截止时间 | 无 |

> UNIQUE(email, system_id)。本表不使用软删除，成功登录后重置 consecutive_failures=0 并清空 locked_until。

**关系**

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| 无 | — | — | — |

> login_attempts 以 email 为键而非 user_id，因为登录失败时账号可能不存在。

---

### user_sessions

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-auth-016(app), R-auth-011(admin) |
| 业务定义 | 活跃会话追踪 |
| 状态机 | SM-auth-001 |

**字段**

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| user_id | uuid | 是 | 无 | 否 | 所属用户 | 引用 auth.users(id) |
| system_id | text | 是 | 无 | 否 | 所属系统 | 枚举:system_enum |
| session_token_hash | text | 是 | 无 | 是 | 会话标识哈希 | 非空 |
| device_info | text | 否 | null | 否 | 设备信息 | 长度≤500 |
| ip_address | text | 否 | null | 否 | 登录IP | 无 |
| logged_in_at | timestamptz | 是 | now() | 否 | 登录时间 | 无 |
| last_active_at | timestamptz | 是 | now() | 否 | 末次活跃时间 | 无 |
| is_active | boolean | 是 | true | 否 | 是否活跃 | 无 |

> 本表不使用软删除。会话失效时设 is_active=false。

**关系**

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| auth.users | N:1 | user_id | CASCADE |

---

### audit_logs

| 项 | 值 |
|----|-----|
| 关联 R-ID | C01 §6 审计要求 |
| 业务定义 | 认证操作审计日志 |
| 状态机 | 无 |

**字段**

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| user_id | uuid | 否 | null | 否 | 操作用户 | 失败登录可为null |
| email | text | 否 | null | 否 | 操作邮箱 | 无 |
| system_id | text | 是 | 无 | 否 | 所属系统 | 枚举:system_enum |
| action | text | 是 | 无 | 否 | 操作类型 | 枚举:audit_action_enum |
| ip_address | text | 否 | null | 否 | 客户端IP | 无 |
| user_agent | text | 否 | null | 否 | 客户端UA | 无 |
| metadata | jsonb | 否 | null | 否 | 附加信息 | 无 |

> 审计日志不做软删除（B01规定）。仅携带 id + created_at，不携带 updated_at/created_by/updated_by。保留 90 天（C01 §6）。

**关系**

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| auth.users | N:1 | user_id | SET NULL |

> user_id 使用 SET NULL 而非 CASCADE，确保用户删除后审计记录留存。

---

## 3. 枚举定义

### auth_provider_enum

| 枚举名 | 值 | 中文名 | 默认 |
|--------|-----|--------|------|
| auth_provider_enum | email | 邮箱注册 | ✅ |
| auth_provider_enum | google | Google登录 | |

### system_enum

| 枚举名 | 值 | 中文名 | 默认 |
|--------|-----|--------|------|
| system_enum | app | 用户系统 | |
| system_enum | admin | 管理系统 | |

### audit_action_enum

| 枚举名 | 值 | 中文名 | 默认 |
|--------|-----|--------|------|
| audit_action_enum | register | 注册 | |
| audit_action_enum | login | 登录成功 | |
| audit_action_enum | login_failed | 登录失败 | |
| audit_action_enum | login_locked | 账号锁定 | |
| audit_action_enum | google_login | Google登录 | |
| audit_action_enum | logout | 退出登录 | |
| audit_action_enum | password_change | 修改密码 | |
| audit_action_enum | password_reset | 重置密码 | |
| audit_action_enum | password_set | 设置密码 | |
| audit_action_enum | session_revoked | 会话踢下线 | |

---

## 4. 业务规则与校验

| BR-ID | 来源 R-ID | 涉及实体/字段 | 描述(一句) | 实现层 |
|-------|-----------|---------------|-----------|--------|
| BR-001 | R-auth-010(app), R-auth-009(admin) | user_profiles | 密码≥8字符，含字母+数字 | Supabase Auth + Application |
| BR-002 | R-auth-004(app), R-auth-002(admin) | login_attempts.consecutive_failures | 连续5次失败锁定30分钟 | Service |
| BR-002a | R-auth-004(app), R-auth-002(admin) | login_attempts.consecutive_failures | 第1-2次仅显示错误，第3次起追加计数 | Application |
| BR-003 | R-auth-005(app), R-auth-003(admin) | — | 验证码5分钟有效 | Supabase Auth (OTP) |
| BR-004 | R-auth-005(app), R-auth-003(admin) | — | 验证码60秒发送冷却 | Service |
| BR-005 | R-auth-009(app), R-auth-007(admin) | — | Access Token 1小时有效 | Supabase Auth |
| BR-006 | R-auth-009(app), R-auth-007(admin) | — | Refresh Token 7天有效 | Supabase Auth |
| BR-007 | R-auth-007(app), R-auth-005(admin) | — | 邮箱用户修改密码需旧密码 | Service |
| BR-008 | R-auth-014(app) | user_profiles.has_password | Google用户设密码不需旧密码 | Service |
| BR-009 | R-auth-007(app), R-auth-005(admin) | — | 新密码≠旧密码 | Service |
| BR-010 | R-auth-012(app) | user_profiles.auth_provider | Google首登自动创建user角色账号 | Service |
| BR-011 | R-auth-006/007(app), R-auth-004/005(admin) | user_sessions.is_active | 密码修改/重置后其他设备下线 | Service |
| BR-012 | R-auth-016(app), R-auth-011(admin) | user_sessions | 每账号每系统最多2台设备同时在线 | Service |
| BR-013 | R-auth-008(admin) | — | admin登录必须校验role=admin | Service |

---

## 5. 计算/派生字段

无

---

## 6. 索引策略

| IDX-ID | 表 | 字段 | 类型 | 唯一 | 支撑查询 |
|--------|-----|------|------|------|---------|
| uniq_login_attempts_email_sys | login_attempts | (email, system_id) | btree | 是 | 登录时查锁定状态 |
| idx_user_sessions_user_sys | user_sessions | (user_id, system_id) | btree | 否 | 查用户活跃会话数 |
| idx_user_sessions_active | user_sessions | (user_id, system_id, is_active) | btree (partial: is_active=true) | 否 | 快速筛选活跃会话 |
| idx_audit_logs_user | audit_logs | (user_id, created_at) | btree | 否 | 按用户查审计记录 |
| idx_audit_logs_action | audit_logs | (action, created_at) | btree | 否 | 按类型查审计记录 |
| idx_audit_logs_system | audit_logs | (system_id, created_at) | btree | 否 | 按系统查审计记录 |

---

## 7. 种子数据

| 表 | 用途 | 示例 | 写入时机 |
|-----|------|------|---------|
| auth.users (通过Supabase Admin API) | 初始管理员账号 | admin@example.com, role=admin | 首次部署 |
| user_profiles | 管理员资料 | auth_provider=email, has_password=true | 随管理员创建 |

---

## 8. 增量融合报告

### 8.1 本轮新增摘要
首轮产出。新建 4 张表：user_profiles、login_attempts、user_sessions、audit_logs。定义 3 个枚举类型。

### 8.2 融合点 / 冲突点 / 已有变更
无（首轮）

---

## 9. 自检报告

**完整性 — R-ID 覆盖对照**

| R-ID (app) | 承接实体/规则 | R-ID (admin) | 承接实体/规则 |
|------------|-------------|--------------|-------------|
| R-auth-001 邮箱注册 | user_profiles + BR-001 | R-auth-001 邮箱登录 | login_attempts + BR-013 |
| R-auth-002 邮箱登录 | login_attempts + BR-002 | R-auth-002 登录限流 | login_attempts + BR-002 |
| R-auth-003 Google登录 | user_profiles(auth_provider) + BR-010 | R-auth-003 忘记密码 | BR-003/BR-004(Supabase OTP) |
| R-auth-004 登录限流 | login_attempts + BR-002/BR-002a | R-auth-004 重置密码 | BR-001 + BR-011 |
| R-auth-005 忘记密码 | BR-003/BR-004(Supabase OTP) | R-auth-005 修改密码 | BR-007/BR-009 + BR-011 |
| R-auth-006 重置密码 | BR-001 + BR-011 | R-auth-006 退出登录 | user_sessions + audit_logs |
| R-auth-007 修改密码 | BR-007/BR-009 + BR-011 | R-auth-007 Token过期 | BR-005/BR-006(Supabase Auth) |
| R-auth-008 退出登录 | user_sessions + audit_logs | R-auth-008 角色校验 | BR-013 |
| R-auth-009 Token过期 | BR-005/BR-006(Supabase Auth) | R-auth-009 密码强度 | BR-001 |
| R-auth-010 密码强度 | BR-001 | R-auth-010 邮箱格式 | Application层校验 |
| R-auth-011 邮箱格式 | Application层校验 | R-auth-011 多设备限制 | user_sessions + BR-012 |
| R-auth-012 Google自动注册 | user_profiles + BR-010 | | |
| R-auth-013 登录注册切换 | 前端路由，无数据需求 | | |
| R-auth-014 Google密码管理 | user_profiles.has_password + BR-008 | | |
| R-auth-015 注册验证码 | BR-003/BR-004(Supabase OTP) | | |
| R-auth-016 多设备限制 | user_sessions + BR-012 | | |

- [x] 每条 R-ID 均有实体或规则承接
- [x] 枚举值与 C02 SM 状态一致（SM-auth-001 状态由 Supabase Auth 管理，本层不定义状态枚举）
- [x] 外键均标注删除策略，ER 图与字段表一一对应

**命名与规范**
- [x] 命名遵循 B01（snake_case 复数表名、snake_case 字段名、布尔 is_/has_ 前缀、时间 _at 后缀）
- [x] 未重定义 B01 全局表（auth.users 仅引用不修改）
- [x] 主键策略统一(uuid)
- [x] 软删除策略明确（login_attempts/audit_logs 不做软删除，user_sessions 使用 is_active 标记）

**建模完备**
- [x] 索引覆盖主查询路径（登录锁定查询、会话数查询、审计查询）
- [x] 无计算/派生字段

**边界**
- [x] 未输出路由/接口/HTML/状态图
- [x] 单文件 < 1200 行
- [x] 无重复上游信息

---

## 99. 待确认问题

| 编号 | 问题 | AI 默认方案 | 影响 |
|------|------|-----------|------|
| Q-001 | user_profiles 是否需要 deleted_at 软删除 | 暂不加，用户删除走 Supabase Auth 删除 + CASCADE | 若未来需用户自注销需重新评估 |
答案：现在要考虑进去，后续做用户注销功能，保留7天，7天后才删除；所以这里应该是软删除。
| Q-002 | audit_logs 90天过期清理机制 | 由定时任务(cron)执行硬删除 created_at < now()-90d | 需后续配置定时任务 |
答案：可以 由定时任务(cron)执行硬删除 created_at < now()-90d
| Q-003 | session_token_hash 使用何种哈希算法 | SHA-256 哈希 Supabase refresh_token | 开发阶段确认 |
答案：哪个好用哪个，安全第一

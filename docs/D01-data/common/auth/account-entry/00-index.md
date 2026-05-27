# 数据规范 · account-entry · 共用总览

> **适用系统**：app, admin
> **关联 R-ID**：app: R-auth-001~016 / admin: R-auth-001~011
> **不做**：状态机定义(C02)、路由/接口(D02)、页面(C03)
> **特殊说明**：auth 模块大量复用 Supabase Auth 内置能力（用户表 `auth.users`、密码哈希、JWT 签发、Token 刷新、Google OAuth）。本文件仅定义 `public` 域下的扩展表，不触碰 `auth.*` 系统表。
> **实体清单**：01-user-profiles.md ~ 04-audit-logs.md
> **枚举清单**：enums.md

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
        timestamptz deleted_at
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

## 2. 业务规则与校验

| BR-ID | 来源 R-ID | 涉及实体/字段 | 描述(一句) | 实现层 |
|-------|-----------|---------------|-----------|--------|
| BR-001 | R-auth-010(app), R-auth-009(admin) | — | 密码≥8字符，含字母+数字 | Supabase Auth + Application |
| BR-002 | R-auth-004(app), R-auth-002(admin) | login_attempts.consecutive_failures | 连续5次失败锁定30分钟 | Service |
| BR-002a | R-auth-004(app), R-auth-002(admin) | login_attempts.consecutive_failures | 第1-2次仅显示错误，第3次起追加计数 | Application |
| BR-003 | R-auth-005(app), R-auth-003(admin) | — | 验证码5分钟有效 | Supabase Auth (OTP) |
| BR-004 | R-auth-005(app), R-auth-003(admin) | — | 验证码60秒发送冷却 | Service(Redis) + Application(倒计时) |
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

## 3. 索引策略

| IDX-ID | 表 | 字段 | 类型 | 唯一 | 支撑查询 |
|--------|-----|------|------|------|---------|
| uniq_login_attempts_email_sys | login_attempts | (email, system_id) | btree | 是 | 登录时查锁定状态 |
| idx_user_sessions_active | user_sessions | (user_id, system_id, is_active) | btree (partial: is_active=true) | 否 | 查活跃会话数+踢下线 |
| idx_user_profiles_deleted | user_profiles | (deleted_at) | btree (partial: deleted_at IS NOT NULL) | 否 | cron清理已注销用户 |
| idx_audit_logs_user | audit_logs | (user_id, created_at) | btree | 否 | 按用户查审计记录 |
| idx_audit_logs_action | audit_logs | (action, created_at) | btree | 否 | 按类型查审计记录 |
| idx_audit_logs_system | audit_logs | (system_id, created_at) | btree | 否 | 按系统查审计记录 |

---

## 4. 种子数据

| 表 | 用途 | 示例 | 写入时机 |
|-----|------|------|---------|
| auth.users (Supabase Admin API) | 初始管理员 | admin@example.com, role=admin | 首次部署 |
| user_profiles | 管理员资料 | auth_provider=email, has_password=true | 随管理员创建 |

---

## 5. 增量融合报告

### 5.1 本轮新增摘要
首轮产出。新建 4 张表：user_profiles、login_attempts、user_sessions、audit_logs。定义 3 个枚举类型。

### 5.2 融合点 / 冲突点 / 已有变更
无（首轮）

---

## 6. 自检报告

**完整性 — R-ID 覆盖对照**

| R-ID (app) | 承接实体/规则 | R-ID (admin) | 承接实体/规则 |
|------------|-------------|--------------|-------------|
| R-auth-001 邮箱注册 | user_profiles + BR-001 | R-auth-001 邮箱登录 | login_attempts + BR-013 |
| R-auth-002 邮箱登录 | login_attempts + BR-002 | R-auth-002 登录限流 | login_attempts + BR-002 |
| R-auth-003 Google登录 | user_profiles(auth_provider) + BR-010 | R-auth-003 忘记密码 | BR-003/BR-004 |
| R-auth-004 登录限流 | login_attempts + BR-002/BR-002a | R-auth-004 重置密码 | BR-001 + BR-011 |
| R-auth-005 忘记密码 | BR-003/BR-004 | R-auth-005 修改密码 | BR-007/BR-009 + BR-011 |
| R-auth-006 重置密码 | BR-001 + BR-011 | R-auth-006 退出登录 | user_sessions + audit_logs |
| R-auth-007 修改密码 | BR-007/BR-009 + BR-011 | R-auth-007 Token过期 | BR-005/BR-006 |
| R-auth-008 退出登录 | user_sessions + audit_logs | R-auth-008 角色校验 | BR-013 |
| R-auth-009 Token过期 | BR-005/BR-006 | R-auth-009 密码强度 | BR-001 |
| R-auth-010 密码强度 | BR-001 | R-auth-010 邮箱格式 | Application层 |
| R-auth-011 邮箱格式 | Application层 | R-auth-011 多设备限制 | user_sessions + BR-012 |
| R-auth-012 Google自动注册 | user_profiles + BR-010 | | |
| R-auth-013 登录注册切换 | 前端路由，无数据需求 | | |
| R-auth-014 Google密码管理 | user_profiles.has_password + BR-008 | | |
| R-auth-015 注册验证码 | BR-003/BR-004 | | |
| R-auth-016 多设备限制 | user_sessions + BR-012 | | |

- [x] 每条 R-ID 均有实体或规则承接
- [x] 枚举值与 C02 SM 一致（SM 状态由 Supabase Auth 管理，本层不定义状态枚举）
- [x] 外键均标注删除策略，ER 图与实体文件一一对应

**命名与规范**
- [x] 命名遵循 B01
- [x] 未重定义 B01 全局表（auth.users 仅引用）
- [x] 主键统一 uuid
- [x] 软删除策略明确（user_profiles 使用 deleted_at、login_attempts/audit_logs 不做软删除、user_sessions 使用 is_active）

**建模完备**
- [x] 索引覆盖主查询路径
- [x] 无计算/派生字段

**边界**
- [x] 未输出路由/接口/HTML/状态图
- [x] 无重复上游信息

---

## 99. 待确认问题

无（已全部确认）

# 接口规范 · account-entry

> **系统**：admin
> **关联 R-ID**：R-auth-001~011
> **不做**：表结构(D01)、页面/原型(C02/C03)
> **特殊说明**：admin 系统无注册、无 Google 登录。Token 刷新由前端 `supabase-js` 自动处理(B01-09)。登录时必须校验 `app_metadata.role=admin`。

---

## 1. 路由表

### 1.1 page-id → URL 映射

| page-id | 页面名称 | URL | 鉴权 | 可见角色 |
|---------|---------|-----|------|---------|
| P-admin-auth-001 | 登录页 | /login | 公开 | 全部 |
| P-admin-auth-002 | 忘记密码页 | /forgot-password | 公开 | 全部 |
| P-admin-auth-003 | 重置密码页 | /reset-password | 公开(需验证码token) | 全部 |
| P-admin-auth-004 | 后台壳 | / | Bearer JWT + role=admin | ROLE-ADMIN |

---

## 2. 接口清单

| API-ID | 方法 | 路径 | 职责(≤10字) | 角色 | R-ID | SM 转移 |
|--------|------|------|------------|------|------|--------|
| API-admin-auth-login | POST | /api/v1/admin/auth/login | 管理员邮箱登录 | 公开 | R-auth-001, R-auth-002, R-auth-008, R-auth-011 | TR-001, TR-002, TR-003, TR-004 |
| API-admin-auth-forgot-password | POST | /api/v1/admin/auth/forgot-password | 发送重置验证码 | 公开 | R-auth-003 | 无 |
| API-admin-auth-verify-reset-otp | POST | /api/v1/admin/auth/forgot-password/verify | 验证重置OTP | 公开 | R-auth-003 | 无 |
| API-admin-auth-reset-password | POST | /api/v1/admin/auth/reset-password | 重置密码 | 公开(需reset_token) | R-auth-004, R-auth-009 | 无 |
| API-admin-auth-change-password | PUT | /api/v1/admin/auth/password | 修改密码 | Bearer JWT + admin | R-auth-005, R-auth-009 | 无 |
| API-admin-auth-logout | POST | /api/v1/admin/auth/logout | 退出登录 | Bearer JWT + admin | R-auth-006 | TR-007 |
| API-admin-auth-me | GET | /api/v1/admin/auth/me | 获取管理员信息 | Bearer JWT + admin | — | 无 |

---

## 3. 接口详情

### 3.1 `POST /api/v1/admin/auth/login` · 管理员邮箱登录

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-login |
| SM 转移 | SM-auth-001:TR-001→TR-002(成功) / TR-003(失败) / TR-004(锁定) |
| R-ID | R-auth-001, R-auth-002, R-auth-008, R-auth-011 |
| 角色 | 公开 |
| 行级权限 | 无 |
| 幂等 | 否 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Body | email | string | 是 | 邮箱格式 | — |
| Body | password | string | 是 | 非空 | — |
| Header | User-Agent | string | 否 | — | user_sessions.device_info |
| Header | X-Forwarded-For | string | 否 | — | user_sessions.ip_address |

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant DB
  participant SupaAuth as Supabase Auth
  FE->>BE: POST /login {email, password}
  BE->>DB: 查 login_attempts(email, admin)
  alt 已锁定且未过期
    BE-->>FE: 429 账号锁定
  end
  BE->>SupaAuth: signInWithPassword(email, password)
  alt 认证失败
    BE->>DB: 更新 login_attempts(+1)
    alt ≥5次
      BE->>DB: 设 locked_until=now()+30min
      BE->>DB: 写 audit_logs(login_locked)
    end
    BE->>DB: 写 audit_logs(login_failed)
    BE-->>FE: 401 错误(含失败次数)
  end
  BE->>BE: 检查 JWT app_metadata.role
  alt role≠admin
    BE->>DB: 写 audit_logs(login_failed, metadata:{reason:role_mismatch})
    BE-->>FE: 403 无权限
  end
  BE->>DB: 重置 login_attempts(0)
  BE->>DB: 查 user_sessions(user_id, admin, active)
  alt 活跃会话≥2
    BE->>DB: 最早会话 is_active=false
    BE->>DB: 写 audit_logs(session_revoked)
  end
  BE->>DB: INSERT user_sessions(新会话)
  BE->>DB: 写 audit_logs(login)
  BE-->>FE: {code:0, data:{session, profile}}
```

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-002 | 连续5次失败锁定30分钟 | 42901 |
| BR-002a | 第1-2次仅返回错误，第3次起返回失败计数 | 40101 |
| BR-013 | 必须role=admin | 40301 |
| BR-010 | 活跃会话≥2时踢最早设备 | 无(自动处理) |

**成功响应**

```json
{
  "code": 0,
  "data": {
    "access_token": "...",
    "refresh_token": "...",
    "user": { "id": "uuid", "email": "...", "display_name": "...", "role": "admin" }
  },
  "msg": "ok"
}
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 400 | 40001 | 参数校验失败 | 邮箱格式错误 |
| 401 | 40101 | 邮箱或密码错误 | 凭证不匹配(含 failure_count) |
| 403 | 40301 | 无权限 | role≠admin |
| 429 | 42901 | 账号锁定 | 连续≥5次失败(含 locked_until) |

> 角色校验在凭证验证通过后执行。role≠admin 的失败不计入 login_attempts（凭证本身正确）。

**副作用**
- 成功：重置 login_attempts、创建 user_sessions、写 audit_logs(login)
- 密码错误：更新 login_attempts、写 audit_logs(login_failed/login_locked)
- 角色不符：写 audit_logs(login_failed, role_mismatch)
- 超限踢下线：更新旧会话、写 audit_logs(session_revoked)

---

### 3.2 `POST /api/v1/admin/auth/forgot-password` · 发送重置验证码

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-forgot-password |
| SM 转移 | 无 |
| R-ID | R-auth-003 |
| 角色 | 公开 |
| 行级权限 | 无 |
| 幂等 | 否 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Body | email | string | 是 | 邮箱格式 | — |

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant SupaAuth as Supabase Auth
  FE->>BE: POST /forgot-password {email}
  BE->>BE: 校验邮箱格式+60秒冷却检查
  BE->>SupaAuth: resetPasswordForEmail(email)
  BE-->>FE: {code:0, msg:"验证码已发送"}
```

> 无论邮箱是否存在，均返回"已发送"，防止邮箱枚举攻击。

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-004 | 60秒发送冷却 | 42901 |

**成功响应**

```json
{ "code": 0, "data": { "email": "admin@example.com" }, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 400 | 40001 | 参数校验失败 | 邮箱格式错误 |
| 429 | 42901 | 请求过于频繁 | 60秒内重复请求 |

**副作用**
- Supabase 发送 OTP 邮件（邮箱存在时）

---

### 3.3 `POST /api/v1/admin/auth/forgot-password/verify` · 验证重置OTP

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-verify-reset-otp |
| SM 转移 | 无 |
| R-ID | R-auth-003 |
| 角色 | 公开 |
| 行级权限 | 无 |
| 幂等 | 否 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Body | email | string | 是 | 邮箱格式 | — |
| Body | otp | string | 是 | 6位数字 | — |

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant SupaAuth as Supabase Auth
  FE->>BE: POST /forgot-password/verify {email, otp}
  BE->>SupaAuth: verifyOtp(email, otp, type=recovery)
  SupaAuth-->>BE: 验证通过，返回临时session
  BE-->>FE: {code:0, data:{reset_token}}
```

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-003 | 验证码5分钟有效 | 40102 |
| — | 验证码正确性 | 40103 |

**成功响应**

```json
{ "code": 0, "data": { "reset_token": "..." }, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 401 | 40102 | 验证码过期 | OTP超过5分钟 |
| 401 | 40103 | 验证码错误 | OTP不匹配 |

**副作用**
无

---

### 3.4 `POST /api/v1/admin/auth/reset-password` · 重置密码

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-reset-password |
| SM 转移 | 无 |
| R-ID | R-auth-004, R-auth-009 |
| 角色 | 公开(需 reset_token) |
| 行级权限 | 无 |
| 幂等 | 否 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Header | Authorization | string | 是 | Bearer reset_token | — |
| Body | new_password | string | 是 | ≥8字符含字母+数字 | — |

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant SupaAuth as Supabase Auth
  participant DB
  FE->>BE: POST /reset-password {new_password} + Bearer reset_token
  BE->>BE: 验签 reset_token
  BE->>SupaAuth: updateUser({password: new_password})
  BE->>DB: user_sessions 全部 is_active=false(该用户, admin)
  BE->>SupaAuth: signOut(scope=others)
  BE->>DB: 写 audit_logs(password_reset)
  BE-->>FE: {code:0, msg:"密码重置成功"}
```

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-001 | 密码强度 | 40001 |
| BR-009 | 其他设备自动下线 | 无(自动处理) |

**成功响应**

```json
{ "code": 0, "data": null, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 400 | 40001 | 密码强度不足 | 不满足要求 |
| 401 | 40101 | Token无效 | reset_token过期或无效 |

**副作用**
- 该用户 admin 系统的 user_sessions 全部 is_active=false
- Supabase signOut(scope=others)
- 写入 audit_logs(password_reset)

---

### 3.5 `PUT /api/v1/admin/auth/password` · 修改密码

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-change-password |
| SM 转移 | 无 |
| R-ID | R-auth-005, R-auth-009 |
| 角色 | Bearer JWT + admin |
| 行级权限 | auth.uid() = 自身 |
| 幂等 | 否 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Header | Authorization | string | 是 | Bearer JWT | — |
| Body | old_password | string | 是 | 非空 | — |
| Body | new_password | string | 是 | ≥8字符含字母+数字 | — |

> admin 系统无 Google 登录，修改密码始终需要旧密码。

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant SupaAuth as Supabase Auth
  participant DB
  FE->>BE: PUT /password {old_password, new_password}
  BE->>SupaAuth: signInWithPassword(email, old_password)验旧
  alt 旧密码错误
    BE-->>FE: 401 旧密码错误
  end
  BE->>BE: 检查 new≠old
  BE->>SupaAuth: updateUser({password: new_password})
  BE->>DB: 其他 user_sessions(admin) is_active=false
  BE->>SupaAuth: signOut(scope=others)
  BE->>DB: 写 audit_logs(password_change)
  BE-->>FE: {code:0, msg:"密码修改成功"}
```

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-001 | 密码强度 | 40001 |
| BR-007 | 需验证旧密码 | 40104 |
| BR-008 | 新密码≠旧密码 | 40002 |
| BR-009 | 其他设备自动下线 | 无(自动处理) |

**成功响应**

```json
{ "code": 0, "data": null, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 400 | 40001 | 密码强度不足 | 不满足要求 |
| 400 | 40002 | 新密码与旧密码相同 | new=old |
| 401 | 40101 | Token无效 | JWT过期 |
| 401 | 40104 | 旧密码错误 | 旧密码不匹配 |

**副作用**
- 其他 user_sessions(admin) is_active=false + Supabase signOut(scope=others)
- 写入 audit_logs(password_change)

---

### 3.6 `POST /api/v1/admin/auth/logout` · 退出登录

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-logout |
| SM 转移 | SM-auth-001:TR-007 |
| R-ID | R-auth-006 |
| 角色 | Bearer JWT + admin |
| 行级权限 | auth.uid() = 自身 |
| 幂等 | 是 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Header | Authorization | string | 是 | Bearer JWT | — |

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant SupaAuth as Supabase Auth
  participant DB
  FE->>BE: POST /logout (Bearer JWT)
  BE->>DB: 当前 user_sessions is_active=false
  BE->>SupaAuth: signOut(scope=local)
  BE->>DB: 写 audit_logs(logout)
  BE-->>FE: {code:0}
```

**业务规则**

无特殊规则。

**成功响应**

```json
{ "code": 0, "data": null, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 401 | 40101 | Token无效 | JWT验签失败 |

**副作用**
- 当前 user_sessions.is_active=false
- 写入 audit_logs(logout)

---

### 3.7 `GET /api/v1/admin/auth/me` · 获取管理员信息

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-admin-auth-me |
| SM 转移 | 无 |
| R-ID | — |
| 角色 | Bearer JWT + admin |
| 行级权限 | auth.uid() = 自身 |
| 幂等 | 是 |

**请求参数**

| 位置 | 字段 | 类型 | 必填 | 校验(一句) | D01 来源 |
|------|------|------|------|-----------|---------|
| Header | Authorization | string | 是 | Bearer JWT | — |

**业务流程**

```mermaid
sequenceDiagram
  participant FE
  participant BE
  participant DB
  FE->>BE: GET /me (Bearer JWT)
  BE->>BE: 验签+确认role=admin
  BE->>DB: 查 user_profiles(id=user_id)
  BE-->>FE: {code:0, data:{profile}}
```

**业务规则**

无特殊规则。

**成功响应**

```json
{
  "code": 0,
  "data": {
    "id": "uuid",
    "email": "admin@example.com",
    "display_name": "管理员",
    "role": "admin"
  },
  "msg": "ok"
}
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 401 | 40101 | Token无效 | JWT验签失败 |
| 403 | 40301 | 无权限 | role≠admin |

**副作用**
无

---

## 4. 错误码汇总

| code | HTTP | 含义 | 文案 | 触发接口 |
|------|------|------|------|---------|
| 40001 | 400 | 参数校验失败 | 请检查输入内容 | login, forgot-password, reset-password, change-password |
| 40002 | 400 | 新密码与旧密码相同 | 新密码不能与旧密码相同 | change-password |
| 40101 | 401 | 认证失败 | 邮箱或密码错误 | login, me, logout, change-password |
| 40102 | 401 | 验证码过期 | 验证码已过期，请重新发送 | verify-reset-otp |
| 40103 | 401 | 验证码错误 | 验证码错误 | verify-reset-otp |
| 40104 | 401 | 旧密码错误 | 旧密码错误 | change-password |
| 40301 | 403 | 权限不足 | 您没有管理后台访问权限 | login, me |
| 42901 | 429 | 请求限流 | 请求过于频繁/账号已锁定 | login, forgot-password |
| 50301 | 503 | 第三方异常 | 服务暂不可用 | login |

---

## 5. 并发与幂等

| API-ID | 并发场景 | 策略 | 失败处理 |
|--------|---------|------|---------|
| API-admin-auth-login | 同一邮箱并发登录 | login_attempts 行级锁(SELECT FOR UPDATE) | 重试 |

---

## 6. 事件/Webhook

无

---

## 7. 增量融合报告

### 7.1 本轮新增 / 融合点 / 冲突点
首轮产出。共 7 个接口。无融合/冲突。

---

## 8. 自检报告

**R-ID 覆盖**

| R-ID | 承接 API-ID |
|------|------------|
| R-auth-001 邮箱登录 | API-admin-auth-login |
| R-auth-002 登录限流 | API-admin-auth-login (BR-002/BR-002a) |
| R-auth-003 忘记密码 | API-admin-auth-forgot-password + verify-reset-otp |
| R-auth-004 重置密码 | API-admin-auth-reset-password |
| R-auth-005 修改密码 | API-admin-auth-change-password |
| R-auth-006 退出登录 | API-admin-auth-logout |
| R-auth-007 Token过期 | 前端supabase-js自动刷新(B01-09)，不经后端 |
| R-auth-008 角色校验 | API-admin-auth-login (BR-013) |
| R-auth-009 密码强度 | reset-password, change-password 的请求校验 |
| R-auth-010 邮箱格式 | 各接口 email 字段校验 |
| R-auth-011 多设备限制 | API-admin-auth-login 中的会话管理逻辑 |

- [x] 每条 R-ID 均有接口承接（R-auth-007 为前端行为，无需后端接口）

**SM 转移覆盖**

| SM 转移 | 承接 API-ID |
|---------|------------|
| TR-001 未登录→认证中 | API-admin-auth-login |
| TR-002 认证中→已登录 | API-admin-auth-login(成功) |
| TR-003 认证中→登录失败 | API-admin-auth-login(失败) |
| TR-004 登录失败→账号锁定 | API-admin-auth-login(BR-002) |
| TR-005 已登录→Token刷新中 | 前端supabase-js |
| TR-006 Token刷新中→会话过期 | 前端supabase-js |
| TR-007 已登录→未登录(退出) | API-admin-auth-logout |

- [x] 每条 SM 转移均有接口或前端行为承接

**D01 一致性**
- [x] 入参/出参字段名、类型与 D01 实体字段一致
- [x] 校验规则与 D01 BR-ID 一致

**B01 一致性**
- [x] 错误码范围遵守 B01
- [x] URL 命名遵守 B01（/api/v1/admin/auth/...）

**page-id 覆盖**
- [x] 4 个 page-id 100% 来自 C02，不增不减

**边界**
- [x] 未写 UI/HTML
- [x] 未修改 SM
- [x] API-ID 带 admin 前缀
- [x] 不跨系统
- [x] 单文件 < 1200 行

---

## 99. 待确认问题

| 编号 | 问题 | AI 默认方案 | 影响 |
|------|------|-----------|------|
| Q-001 | admin 登录是否需要额外的 IP 白名单校验在 API 层 | 否，由 Nginx 层处理(B01-08) | API 层不做 IP 校验 |
答案：你决定，选择好的。就是我经常连VPN IP是不固定的。综合考虑安全因素，你决定。
| Q-002 | role≠admin 的登录失败是否计入 login_attempts | 否，凭证正确但角色不符不计入失败次数 | 防止合法 app 用户误触 admin 登录被锁 |
答案：你决定，选择好的。

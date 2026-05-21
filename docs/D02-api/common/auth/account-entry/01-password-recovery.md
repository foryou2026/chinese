# 密码找回

## `POST /api/v1/{sys}/auth/forgot-password` · 发送重置验证码

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-common-auth-forgot-password |
| SM 转移 | 无 |
| R-ID | app:R-auth-005, admin:R-auth-003 |
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
  FE->>BE: POST /{sys}/auth/forgot-password {email}
  BE->>BE: 校验邮箱格式+60秒冷却检查(Redis)
  BE->>SupaAuth: resetPasswordForEmail(email)
  BE-->>FE: {code:0, msg:"验证码已发送"}
```

> 无论邮箱是否存在，均返回"已发送"，防止邮箱枚举攻击。

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-004 | 60秒发送冷却(后端Redis兜底) | 42901 |

**成功响应**

```json
{ "code": 0, "data": { "email": "user@example.com" }, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 400 | 40001 | 参数校验失败 | 邮箱格式错误 |
| 429 | 42901 | 请求过于频繁 | 60秒内重复请求 |

**副作用**
- Supabase 发送 OTP 邮件（邮箱存在时）

---

## `POST /api/v1/{sys}/auth/forgot-password/verify` · 验证重置OTP

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-common-auth-verify-reset-otp |
| SM 转移 | 无 |
| R-ID | app:R-auth-005, admin:R-auth-003 |
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
  FE->>BE: POST /{sys}/auth/forgot-password/verify {email, otp}
  BE->>SupaAuth: verifyOtp(email, otp, type=recovery)
  SupaAuth-->>BE: 验证通过，返回临时session
  BE-->>FE: {code:0, data:{reset_token}}
```

> 验证通过后返回 reset_token（Supabase verifyOtp 返回的临时 access_token），用于下一步重置密码。

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

## `POST /api/v1/{sys}/auth/reset-password` · 重置密码

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-common-auth-reset-password |
| SM 转移 | 无 |
| R-ID | app:R-auth-006,010, admin:R-auth-004,009 |
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
  FE->>BE: POST /{sys}/auth/reset-password {new_password} + Bearer reset_token
  BE->>BE: 验签 reset_token
  BE->>SupaAuth: updateUser({password: new_password})
  BE->>DB: user_sessions(user_id, system_id={sys}) 全部 is_active=false
  BE->>SupaAuth: signOut(scope=others)
  BE->>DB: 写 audit_logs(password_reset, system_id={sys})
  BE-->>FE: {code:0, msg:"密码重置成功"}
```

> system_id 从路由上下文取值，仅使当前系统的会话失效。

**业务规则**

| BR-ID | 校验内容 | 失败 code |
|-------|---------|----------|
| BR-001 | 密码强度(≥8字符含字母+数字) | 40001 |

**成功响应**

```json
{ "code": 0, "data": null, "msg": "ok" }
```

**失败响应**

| HTTP | code | 含义 | 触发条件 |
|------|------|------|---------|
| 400 | 40001 | 密码强度不足 | 不满足≥8字符含字母+数字 |
| 401 | 40101 | Token无效 | reset_token过期或无效 |

**副作用**
- 该用户当前系统 user_sessions 全部 is_active=false
- Supabase signOut(scope=others)
- 写入 audit_logs(password_reset)

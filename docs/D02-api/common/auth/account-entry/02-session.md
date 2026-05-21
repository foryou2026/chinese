# 会话管理

## `POST /api/v1/{sys}/auth/logout` · 退出登录

**基础信息**

| 项 | 值 |
|----|-----|
| API-ID | API-common-auth-logout |
| SM 转移 | app:SM-auth-001:TR-010, admin:SM-auth-001:TR-007 |
| R-ID | app:R-auth-008, admin:R-auth-006 |
| 角色 | Bearer JWT |
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
  FE->>BE: POST /{sys}/auth/logout (Bearer JWT)
  BE->>DB: 当前 user_sessions is_active=false
  BE->>SupaAuth: signOut(scope=local)
  BE->>DB: 写 audit_logs(logout, system_id={sys})
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

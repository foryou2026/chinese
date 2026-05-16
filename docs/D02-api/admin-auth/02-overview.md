<!-- TARGET-PATH: docs/D02-api/admin-auth/02-overview.md -->

# D02 · 通用约定 · `admin-auth`

## 1. 响应壳

与 app 完全一致 (B01-04 § 统一响应):

```json
{ "data": ..., "error": null, "meta": { "trace_id": "..." } }
```

## 2. 守卫

| 路径模式 | 中间件链 |
|---------|---------|
| `/admin/v1/auth/cookie/*` `/admin/v1/auth/login-attempt-record` `/admin/v1/auth/forgot-password-throttle` | 仅 `csrfGuard` (写) |
| `/admin/v1/auth/session-register` `/.../session-revoke` `/.../session-status` `/.../logout-global` `/.../me` `/.../password` | `requireAuth` + `requireRole('super_admin')` + `csrfGuard` |

> `requireAuth` 实现见 [`B01-09 §3`](../../B01-architecture/09-auth-infra.md#3-后端鉴权中间件)。

## 3. surface 透传

handler 一律向 service 注入 `{ surface: 'admin' }` 上下文;service 内据此:
- 写 `user_sessions.surface='admin'` / `auth_login_attempts.surface='admin'` / `audit_logs.context->>surface='admin'`
- 选择 `audit_logs.event` 前缀 (admin.* vs auth.*)

## 4. 错误码

- 全部沿用 [`D02-api/app-auth/04-error-codes.md`](../app-auth/04-error-codes.md)
- 仅新增 1 个:`AUTH_USE_USER_ENTRY` (admin 登录时检测到 user 角色)
- 详见 [`04-error-codes.md`](./04-error-codes.md)

## 5. 审计

每个写 endpoint 必须落 `audit_logs`;event 见 [`06-events.md`](./06-events.md)。

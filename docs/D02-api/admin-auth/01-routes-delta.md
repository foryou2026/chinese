<!-- TARGET-PATH: docs/D02-api/admin-auth/01-routes-delta.md -->

# D02 · 路由增量 · `admin-auth`

> 相对 [`_global-routes.md`](../_global-routes.md) 的增量。admin 路径全部前缀 `/admin/v1`。

## 1. 公开 (无守卫)

| Method | 路径 | 复用 service |
|--------|------|-------------|
| POST | `/admin/v1/auth/cookie/get` | `cookieService.get` |
| POST | `/admin/v1/auth/cookie/set` | `cookieService.set` |
| POST | `/admin/v1/auth/cookie/clear` | `cookieService.clear` |
| POST | `/admin/v1/auth/login-attempt-record` | `loginAttemptService.record` (surface='admin') |
| POST | `/admin/v1/auth/forgot-password-throttle` | `forgotService.throttle` (surface='admin') |

## 2. 需登录 + super_admin 守卫

| Method | 路径 | 复用 service |
|--------|------|-------------|
| POST | `/admin/v1/auth/session-register` | `sessionService.register` (surface='admin', cap=3) |
| POST | `/admin/v1/auth/session-revoke` | `sessionService.revoke` |
| GET | `/admin/v1/auth/session-status` | `sessionService.status` |
| POST | `/admin/v1/auth/logout-global` | `sessionService.logoutGlobal` |
| GET | `/admin/v1/auth/me` | 新写薄包装 (返回脱敏 email + role + sessionsCount + lastSignInAt) |
| POST | `/admin/v1/auth/password` | `passwordService.change` (复用 `me/password`) |

## 3. 不暴露 (相对 app)

| app 路径 | 不在 admin 暴露原因 |
|---------|--------------------|
| `POST /v1/auth/register-throttle` | admin 无注册 |
| `POST /v1/auth/resend-verify` | admin 无邮箱验证 |
| `GET /v1/me` | 用 `/admin/v1/auth/me` 替代 |
| `PATCH /v1/me` | admin 不允许改 display_name/avatar/locale |
| `POST /v1/me/password` | 用 `/admin/v1/auth/password` 替代 |
| `POST /internal/auth-hook` | 全局唯一,不 admin 化 |

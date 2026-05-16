<!-- TARGET-PATH: docs/D02-api/_global-routes.md -->

# D02 · 全局路由表

> **职责**：所有 feature 的对外路由在这里集中登记；每行包含「feature / method / path / 守卫 / 详情链接」。  
> **维护**：每个 feature 在 D02 阶段必须 append 自己的全部路由；冲突由本表统一裁决。  
> **冻结状态**：滚动更新

## 应用端 API（`apps/api-app`，Hono）· prefix `/v1/`

| method | path | feature | 守卫 | 详情 |
|--------|------|---------|------|------|
| POST | `/v1/auth/cookie/get` | app-auth | 无 | [→](./app-auth/03-endpoints/POST-auth-cookie-get.md) |
| POST | `/v1/auth/cookie/set` | app-auth | 无 (CSRF check) | [→](./app-auth/03-endpoints/POST-auth-cookie-set.md) |
| POST | `/v1/auth/cookie/clear` | app-auth | 无 | [→](./app-auth/03-endpoints/POST-auth-cookie-clear.md) |
| POST | `/v1/auth/register-throttle` | app-auth | 无 | [→](./app-auth/03-endpoints/POST-auth-register-throttle.md) |
| POST | `/v1/auth/login-attempt-record` | app-auth | 无 | [→](./app-auth/03-endpoints/POST-auth-login-attempt-record.md) |
| POST | `/v1/auth/forgot-password-throttle` | app-auth | 无 | [→](./app-auth/03-endpoints/POST-auth-forgot-password-throttle.md) |
| POST | `/v1/auth/resend-verify` | app-auth | 无 | [→](./app-auth/03-endpoints/POST-auth-resend-verify.md) |
| POST | `/v1/auth/session-register` | app-auth | authRequired | [→](./app-auth/03-endpoints/POST-auth-session-register.md) |
| POST | `/v1/auth/session-revoke` | app-auth | authRequired | [→](./app-auth/03-endpoints/POST-auth-session-revoke.md) |
| GET | `/v1/auth/session-status` | app-auth | authRequired | [→](./app-auth/03-endpoints/GET-auth-session-status.md) |
| POST | `/v1/auth/logout-global` | app-auth | authRequired | [→](./app-auth/03-endpoints/POST-auth-logout-global.md) |
| GET | `/v1/me` | app-auth | authRequired + roleRequired('user') | [→](./app-auth/03-endpoints/GET-me.md) |
| PATCH | `/v1/me` | app-auth | authRequired + roleRequired('user') | [→](./app-auth/03-endpoints/PATCH-me.md) |
| POST | `/v1/me/password` | app-auth | authRequired + roleRequired('user') | [→](./app-auth/03-endpoints/POST-me-password.md) |

## 管理端 API（`apps/api-admin`）

（admin-auth feature 在批次 4 时 append）

## 内部 API（Hook）

| method | path | feature | 守卫 | 详情 |
|--------|------|---------|------|------|
| POST | `/internal/auth-hook` | app-auth | HMAC 签名校验 | [→](./app-auth/03-endpoints/POST-internal-auth-hook.md) |

<!-- TARGET-PATH: docs/D02-api/app-auth/01-routes-delta.md -->

# `app-auth` · 路由增量

> 已 append 到 [`docs/D02-api/_global-routes.md`](../_global-routes.md)。
> 本文件作"本 feature 视角"的镜像，便于单 feature 评审。

| method | path | 守卫 | 主要用途 |
|--------|------|------|---------|
| POST | `/v1/auth/cookie/get` | 无 | cookieStorage Adapter 读 |
| POST | `/v1/auth/cookie/set` | 无 (CSRF) | cookieStorage Adapter 写 |
| POST | `/v1/auth/cookie/clear` | 无 | 退出时清 |
| POST | `/v1/auth/register-throttle` | 无 | 注册前置节流 |
| POST | `/v1/auth/login-attempt-record` | 无 | 登录前置节流 + 锁定 |
| POST | `/v1/auth/forgot-password-throttle` | 无 | 忘密前置节流 |
| POST | `/v1/auth/resend-verify` | 无 | 重发验证邮件（受 register-throttle 节流）|
| POST | `/v1/auth/session-register` | authRequired | 登录成功后注册 session + 踢最早 |
| POST | `/v1/auth/session-revoke` | authRequired | 本设备退出删 session |
| GET | `/v1/auth/session-status` | authRequired | 前端轮询是否被踢 |
| POST | `/v1/auth/logout-global` | authRequired | 全部设备退出 |
| GET | `/v1/me` | authRequired | 读自身 profile |
| PATCH | `/v1/me` | authRequired | 改 display_name / avatar_url / locale |
| POST | `/v1/me/password` | authRequired | 改密码 + 踢其他设备 |
| POST | `/internal/auth-hook` | HMAC | GoTrue before_user_created 回调 |

> 守卫定义见 [`B02-permissions/03-authz-mechanism §1`](../../B02-permissions/03-authz-mechanism.md)。

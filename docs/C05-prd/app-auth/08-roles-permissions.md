<!-- TARGET-PATH: docs/C05-prd/app-auth/08-roles-permissions.md -->

# 08 · 角色与权限

| 资源 / 操作 | anonymous | user | super_admin |
|------------|-----------|------|-------------|
| 访问 `/auth/*` | ✅ | ✅ (登录态自动跳走) | ✅ (登录态自动跳走) |
| 访问 `/me/*` | ❌ 守卫 → `/auth/login?redirect=…` | ✅ | ❌ 应使用 admin 端 |
| 调用 `GET/PATCH /v1/me` | ❌ 401 | ✅ 自有数据 | ❌ 403（admin 走 admin-users API）|
| 调用 `POST /v1/me/password` | ❌ | ✅ | ❌ 403 |
| 调用 `POST /v1/auth/login-attempt-record` | ✅ | ✅ | ✅ |
| 调用 `POST /v1/auth/session-register` | — | 内部由前端在登录成功后调 | 内部 |
| 调用 `POST /v1/auth/cookie/*` | ✅ | ✅ | ✅ |
| 调用 `POST /v1/auth/logout-global` | ❌ | ✅ 自身 | ❌ 403 |

> 落地实现：
> - 中间件 `authRequired`、`roleRequired('user')` 详见 [`B02-permissions/03-authz-mechanism §1`](../../B02-permissions/03-authz-mechanism.md)；
> - 路由层每条 endpoint 应用守卫见 [`D02-api/app-auth/03-endpoints/`](../../D02-api/app-auth/03-endpoints/)。

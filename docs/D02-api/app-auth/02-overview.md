<!-- TARGET-PATH: docs/D02-api/app-auth/02-overview.md -->

# `app-auth` · 接口概览

## 1. 分组

| 分组 | prefix | 路径数 | 鉴权 |
|------|--------|--------|------|
| Cookie Adapter | `/v1/auth/cookie/*` | 3 | 无（cookie/set 内做 CSRF）|
| 节流 / 锁定 | `/v1/auth/{register-throttle,login-attempt-record,forgot-password-throttle,resend-verify}` | 4 | 无 |
| 会话管理 | `/v1/auth/{session-register,session-revoke,session-status,logout-global}` | 4 | authRequired |
| Profile | `/v1/me*` | 3 | authRequired + roleRequired('user') |
| Hook（内部）| `/internal/auth-hook` | 1 | HMAC 签名校验 |

## 2. 统一响应壳

按 [`B01-architecture/04-api-conventions §1`](../../B01-architecture/04-api-conventions.md)：

```jsonc
// 成功
{ "data": {...}, "error": null, "meta": {...?} }
// 失败
{ "data": null, "error": { "code": "AUTH_XXX", "message": "<i18n key>", "details": {...?} }}
```

## 3. 鉴权机制

- **authRequired**：从 cookie 读 `zhiyu-at` → JWT 校验 → 用户 id 注入 `c.var.user`；失败 401 `AUTH_NOT_AUTHED`；
- **roleRequired(role)**：在 authRequired 之后，从 `c.var.user` 取 role 比对；失败 403 `AUTH_FORBIDDEN`；
- **disabledCheck**：authRequired 内置 30s LRU 兜底；
- **CSRF Double-Submit**：所有 `state-changing` 接口（非 GET）必须 header `X-Csrf-Token` 与 cookie `zhiyu-csrf` 相等；
- **HMAC**：`/internal/auth-hook` 校验 `X-Webhook-Signature: sha256=<hex(hmac(body, secret))>`，secret = `SUPABASE_AUTH_HOOK_SECRET`。

## 4. 通用 header

| header | 用途 | 必须? |
|--------|------|------|
| `Cookie: zhiyu-at=...; zhiyu-rt=...; zhiyu-csrf=...` | 鉴权 / refresh / CSRF | 受保护接口必带 |
| `X-Csrf-Token` | CSRF 双提交 | state-changing 必带 |
| `Accept-Language` | i18n | 推荐 |
| `User-Agent` | 写入 user_sessions.device_info | 推荐 |

## 5. 通用 query / body 规范

- 所有 POST body 走 `application/json`；
- zod schema 在 `packages/shared-schemas/auth/*.ts` 集中维护；
- 错误码全部走 [`04-error-codes.md`](./04-error-codes.md)。

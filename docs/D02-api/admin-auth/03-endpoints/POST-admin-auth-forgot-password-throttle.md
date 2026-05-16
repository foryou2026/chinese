<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/POST-admin-auth-forgot-password-throttle.md -->

# POST /admin/v1/auth/forgot-password-throttle

## 1. 概述

admin 忘密前置节流:60s / 邮箱 + 1h / IP ≤ 5。

## 2. 入参 / 出参

```json
{ "email": "ops@zhiyu.app" }
→
{ "data": { "ok": true }, "error": null }
```

错误:`AUTH_FORGOT_RATE_LIMITED { retryAfter }`

## 3. 逻辑

复用 app 同名 service,仅多传 `surface='admin'` 作为 Redis key 前缀 (`throttle:forgot:admin:<email>`)。

## 4. 后续动作

通过节流后,handler 不直接发邮件;返回 ok,前端再调 `supabase.auth.resetPasswordForEmail` (浏览器侧)。

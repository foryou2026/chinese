<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/POST-admin-auth-login-attempt-record.md -->

# POST /admin/v1/auth/login-attempt-record

## 1. 概述

admin 登录前置:节流 + 禁用账号检查 (与 app 同 service,surface='admin')

## 2. 入参

```json
{ "email": "ops@zhiyu.app" }
```

zod:`{ email: z.string().email() }`

## 3. 出参

```json
{ "data": { "ok": true }, "error": null, "meta": {...} }
```

或错误:`AUTH_LOGIN_RATE_LIMITED` / `AUTH_ACCOUNT_DISABLED`

## 4. 逻辑

1. 查 30s LRU disabledCache;命中 disabled → 立即返 `AUTH_ACCOUNT_DISABLED`;
2. 查 `auth_login_attempts` 最近 15min where email AND surface='admin' AND result='fail';
3. ≥ 5 → 返 `AUTH_LOGIN_RATE_LIMITED` (retryAfter = 距 oldest attempt + 15min);
4. 否则返 ok。

## 5. 守卫

仅 `csrfGuard`;不需要 auth。

## 6. 审计

不写 (前置检查,无意义)。

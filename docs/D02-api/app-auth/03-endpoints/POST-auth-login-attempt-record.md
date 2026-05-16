<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-login-attempt-record.md -->

# `POST /v1/auth/login-attempt-record`

## 用途
登录前置：先校验是否已锁定 + 是否被禁用，再让前端真正调 `signInWithPassword`；登录后（成功 / 失败）再次调本接口写一行 `auth_login_attempts`。

## 请求（前置查询模式）

```json
{ "phase": "before", "email": "...", "ip": "auto" }
```

返回：
```json
{ "data": { "locked": false, "disabled": false }, "error": null }
```

如锁定 → 429：
```json
{ "data": null, "error": { "code": "AUTH_LOGIN_RATE_LIMITED", "details": { "unlockAt": "2026-05-16T05:30:00Z" }}}
```
如禁用 → 401：
```json
{ "data": null, "error": { "code": "AUTH_ACCOUNT_DISABLED", "details": { "reason": "..." }}}
```

## 请求（事后记录模式）

```json
{ "phase": "after", "email": "...", "succeeded": false, "reason": "invalid_credentials" }
```

返回 `{ "data": null, "error": null }`，INSERT 一行 `auth_login_attempts`。

## 规则
- 锁定判定：`SELECT count(*) FROM auth_login_attempts WHERE email=? AND ip=? AND succeeded=false AND created_at > now()-'15min'` >= 5 → 锁；
- 锁定剩余 = `15min - (now - oldest_failed_at)`；
- 禁用判定：查 `profiles.is_disabled` 走 30s LRU 缓存。

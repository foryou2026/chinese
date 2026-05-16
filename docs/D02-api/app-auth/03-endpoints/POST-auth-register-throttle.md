<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-register-throttle.md -->

# `POST /v1/auth/register-throttle`

## 用途
注册前置节流，先于 `supabase.auth.signUp` 调用；同时被「重发验证邮件」复用。

## 请求

```json
{ "email": "user@example.com" }
```

## 响应

```json
{ "data": { "allowed": true, "retryAfter": 0 }, "error": null }
```

429：
```json
{ "data": null, "error": { "code": "AUTH_REGISTER_RATE_LIMITED", "details": { "retryAfter": 1234 }}}
```

## 规则
- email 维度：1h 滚动窗口 ≤ 3 次；
- IP 维度（取 `X-Forwarded-For` 首段）：1h ≤ 10 次；
- 计数键：`throttle:register:email:{email}` / `throttle:register:ip:{ip}`，TTL 3600。

## 错误码
- 429 `AUTH_REGISTER_RATE_LIMITED`

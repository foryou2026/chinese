<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-forgot-password-throttle.md -->

# `POST /v1/auth/forgot-password-throttle`

## 用途
忘记密码前置节流；通过后服务端转调 `supabase.auth.resetPasswordForEmail`。

## 请求

```json
{ "email": "..." }
```

## 响应

```json
{ "data": { "allowed": true }, "error": null }
```

429：`AUTH_FORGOT_RATE_LIMITED` + `retryAfter`。

## 规则
- email 维度：60s 内 1 次；
- IP 维度：1h 内 ≤ 5 次；
- **不**根据邮箱是否存在区分响应（一律 200，避免存在性探测）。

## 备注
- 实际发送邮件动作由本接口（成功后）调 Supabase Auth API 完成；前端不再单独调；
- 同时审计 `auth.password_reset_requested`。

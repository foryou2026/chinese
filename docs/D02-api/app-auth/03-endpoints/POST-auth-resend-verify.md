<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-resend-verify.md -->

# `POST /v1/auth/resend-verify`

## 用途
"重新发送验证邮件"按钮触发；复用 `register-throttle` 计数。

## 请求

```json
{ "email": "..." }
```

## 流程
1. 先调 `register-throttle` 同款节流逻辑；
2. 通过则调 `supabase.auth.admin.inviteUserByEmail` 或 `supabase.auth.resend({type:'signup', email})`；
3. 落审计 `auth.verify_email_resent`。

## 响应

`{ "data": null, "error": null }`，429 时 `AUTH_REGISTER_RATE_LIMITED`。

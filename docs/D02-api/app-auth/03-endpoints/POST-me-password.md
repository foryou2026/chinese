<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-me-password.md -->

# `POST /v1/me/password`

## 用途
改密码 + 自动踢其他设备。

## 鉴权
authRequired + roleRequired('user') + CSRF。

## 请求

```json
{ "oldPassword": "...", "newPassword": "..." }
```

## 流程
1. zod：new ≥ 8 + 字母 + 数字 + `!= old`；
2. 内部调 `supabase.auth.signInWithPassword(email, oldPassword)` 验旧密；失败 → 401 `AUTH_INVALID_OLD_PASSWORD`；
3. `supabase.auth.admin.updateUserById(id, { password: newPassword })`；
4. `supabase.auth.admin.signOut(id, { scope: 'others' })`；
5. `DELETE FROM user_sessions WHERE user_id=? AND id <> $current_session_id`；
6. 审计 `auth.password_changed` + `auth.signout_global { trigger:'password_change' }`。

## 节流
- session 维度：5min 内 ≤ 3 次（防止误操作 / 防自动化）；超 → 429 `AUTH_PASSWORD_CHANGE_RATE_LIMITED`。

## 响应
`{ "data": null, "error": null }`。

## 错误码
- 400 `VALIDATION_FAILED` / `AUTH_SAME_AS_OLD_PASSWORD`
- 401 `AUTH_INVALID_OLD_PASSWORD`
- 429 `AUTH_PASSWORD_CHANGE_RATE_LIMITED`

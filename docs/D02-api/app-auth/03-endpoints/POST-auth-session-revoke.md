<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-session-revoke.md -->

# `POST /v1/auth/session-revoke`

## 用途
本设备退出删 `user_sessions` 行（不影响其他设备）。

## 鉴权
authRequired。

## 请求

```json
{ "sessionId": "<uuid>" }
```

> 必须等于当前 cookie 对应的 session（后端自校验）；试图删别人的 → 403。

## 流程
1. 校验 `sessionId` 属于当前 user；
2. `DELETE FROM user_sessions WHERE id = ? AND user_id = ?`；
3. `supabase.auth.admin.signOut(refresh_token)`；
4. 审计 `auth.signout_local`。

## 响应

`{ "data": null, "error": null }`，失败 403 `AUTH_FORBIDDEN`。

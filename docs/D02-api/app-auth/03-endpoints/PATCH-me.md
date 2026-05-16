<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/PATCH-me.md -->

# `PATCH /v1/me`

## 用途
改 display_name / avatar_url / locale 三个字段（白名单）。

## 鉴权
authRequired + roleRequired('user') + CSRF。

## 请求

```json
{ "displayName": "Linh", "avatarUrl": "https://...", "locale": "vi" }
```

- 全部字段可选；至少一个；
- 任何额外字段（如 `role`、`isDisabled`）一律忽略（zod `.strict()`）。

## 响应

返回更新后的 GET /v1/me 同 shape。

## 错误码
- 400 `VALIDATION_FAILED`（字段级 `details`）
- 401 `AUTH_NOT_AUTHED`
- 403 `AUTH_FORBIDDEN`
- 5xx 全局

## 审计
`me.profile_updated { fields: [...] }`。

<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/GET-me.md -->

# `GET /v1/me`

## 用途
读自身 profile。

## 鉴权
authRequired + roleRequired('user')。

## 响应

```json
{
  "data": {
    "id": "uuid",
    "email": "u***@example.com",
    "displayName": "Linh",
    "avatarUrl": "https://...",
    "locale": "vi",
    "role": "user",
    "createdAt": "2026-05-01T..."
  },
  "error": null,
  "meta": { "etag": "..." }
}
```

- `email` 字段已脱敏（前 3 + `***@<domain>`）；
- `meta.etag` 用于条件 GET（v2 评估，v1 客户端不强求带）。

## 实现
`SELECT id, email, display_name, avatar_url, locale, role, created_at FROM profiles JOIN auth.users USING (id) WHERE id = $current_user_id`。

## 错误码
401 / 403 / 5xx 全局。

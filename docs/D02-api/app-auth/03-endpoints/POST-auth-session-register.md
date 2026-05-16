<!-- TARGET-PATH: docs/D02-api/app-auth/03-endpoints/POST-auth-session-register.md -->

# `POST /v1/auth/session-register`

## 用途
登录 / OAuth / token-refresh 成功后调用：写入 `user_sessions`；若 > 3，踢最早。

## 鉴权
authRequired。

## 请求

```json
{ "refreshTokenHash": "<sha256(refresh_token)>", "deviceInfo": { "ua": "...", "platform": "..." }}
```

## 流程
```sql
BEGIN;
INSERT INTO user_sessions (user_id, refresh_token_hash, device_info, last_active_at, created_at)
VALUES ($user_id, $hash, $info, now(), now())
RETURNING id AS new_session_id;

WITH excess AS (
  SELECT id, refresh_token_hash FROM user_sessions
  WHERE user_id = $user_id ORDER BY created_at LIMIT GREATEST(
    (SELECT count(*) FROM user_sessions WHERE user_id = $user_id) - 3, 0
  )
)
DELETE FROM user_sessions WHERE id IN (SELECT id FROM excess) RETURNING refresh_token_hash;
COMMIT;
```

对每个被删的 `refresh_token_hash` 调 `supabase.auth.admin.signOut(refresh_token)`（GoTrue admin API）作废其 refresh。

## 响应

```json
{ "data": { "sessionId": "<uuid>", "kicked": ["<old session id>"] }, "error": null }
```

## 审计
- `auth.signin_success`（一定写）
- `auth.session_kicked`（kicked 非空时每个写一行）

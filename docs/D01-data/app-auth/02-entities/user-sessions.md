<!-- TARGET-PATH: docs/D01-data/app-auth/02-entities/user-sessions.md -->

# Entity · `public.user_sessions`

- 完整 DDL：[`B02-permissions/04-data-model §2.2`](../../../B02-permissions/04-data-model.md)。
- 用途：实现"多设备活跃硬上限 3"+ 全局登出。
- 写入：
  - `POST /v1/auth/session-register` 每次登录成功后 INSERT；INSERT 后立即 `count > 3 → DELETE` 最早一行；
  - `POST /v1/auth/session-revoke` 本设备退出时 DELETE 当前行；
  - `POST /v1/auth/logout-global` DELETE `WHERE user_id = ?`；
  - admin 禁用时 DELETE `WHERE user_id = ?`。
- 读取：
  - `GET /v1/auth/session-status` 校验当前 session_id 是否仍存在。
- 删除策略：refresh_token_hash 一旦无效，行必删；不保留历史（审计走 audit_logs）。

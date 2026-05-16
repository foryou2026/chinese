<!-- TARGET-PATH: docs/D01-data/app-auth/02-entities/audit-logs.md -->

# Entity · `public.audit_logs`

- 完整 DDL：[`B02-permissions/04-data-model §2.4`](../../../B02-permissions/04-data-model.md)。
- 本 feature 产生的 `action` 值：

| action | 触发点 | meta 关键字段 |
|--------|--------|--------------|
| `auth.signin_success` | signInWithPassword 成功 | ip, ua, provider='password' |
| `auth.signin_failed` | signInWithPassword 失败 | ip, ua, reason |
| `auth.oauth_signin` | OAuth callback exchange 成功 | ip, ua, provider='google' |
| `auth.signout_local` | 本设备退出 | session_id |
| `auth.signout_global` | 全设备退出 | trigger='user' \| 'admin_disable' \| 'password_change' |
| `auth.session_kicked` | 第 4 设备登录 → 踢最早 | kicked_session_id |
| `auth.password_reset_requested` | POST /v1/auth/forgot-password-throttle 通过 | email |
| `auth.password_reset_completed` | reset-password 成功 | — |
| `auth.password_changed` | POST /v1/me/password 成功 | — |
| `me.profile_updated` | PATCH /v1/me | fields[] |

> 全部审计写入异步（背压由 BullMQ 队列承担，v1 可直接 fire-and-forget）。

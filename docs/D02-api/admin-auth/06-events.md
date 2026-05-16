<!-- TARGET-PATH: docs/D02-api/admin-auth/06-events.md -->

# D02 · 审计事件 · `admin-auth`

> 全部写入 `public.audit_logs`,`actor_role='super_admin'`,`context->>surface='admin'`。

| event | 触发 endpoint | payload (必带字段) |
|-------|--------------|------------------|
| `admin.signin_success` | session-register | `{ kicked: [...], ip_hint_hash }` |
| `admin.signin_failed` | login-attempt-record (失败累计写入) | `{ reason, email_hash, ip_hint_hash }` |
| `admin.signin_locked` | login-attempt-record (触锁) | `{ email_hash, retry_after_min }` |
| `admin.signout` | session-revoke / logout-global | `{ scope: 'local' \| 'global' }` |
| `admin.session_kicked` | session-register 副作用 | `{ kicked_session_id, kicked_created_at }` |
| `admin.password_change_requested` | forgot-password-throttle 通过 | `{ email_hash }` |
| `admin.password_reset` | reset 流程后 (由 supabase 触发器 + DB trigger 落) | `{ via:'reset' }` |
| `admin.password_changed` | POST /password | `{ via:'me' }` |
| `admin.account_disabled` | (运维 SQL) | `{ by:'ops' }`(由 DB trigger 落,本 feature 不主动写) |
| `admin.account_enabled` | (运维 SQL) | 同上 |

## 不写

- session-status (读)
- cookie/* (高频读写)
- 任何 GET 接口

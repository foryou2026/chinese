<!-- TARGET-PATH: docs/D02-api/app-auth/06-events.md -->

# `app-auth` · 事件

> 全部事件落 `public.audit_logs`，异步写。

| event (`action`) | 触发 | meta |
|------------------|------|------|
| `auth.signin_success` | session-register 成功 | `{ ip, ua, provider }` |
| `auth.signin_failed` | login-attempt-record phase=after & !succeeded | `{ ip, ua, reason }` |
| `auth.oauth_signin` | callback exchange 成功 | `{ ip, ua, provider:'google' }` |
| `auth.signout_local` | session-revoke | `{ session_id }` |
| `auth.signout_global` | logout-global / 改密 / admin 禁用 | `{ trigger }` |
| `auth.session_kicked` | session-register 踢 | `{ kicked_session_id }` |
| `auth.password_reset_requested` | forgot-password-throttle 通过 | `{ email }` |
| `auth.password_reset_completed` | reset-password 成功 | — |
| `auth.password_changed` | me/password 成功 | — |
| `auth.verify_email_resent` | resend-verify | — |
| `me.profile_updated` | PATCH /v1/me | `{ fields: [...] }` |

## 跨 feature 消费者（v2）

- `analytics` feature 订阅这些 action 做漏斗 / 留存分析；
- `notifications` feature（v2）订阅 `auth.signin_success` 触发"安全提醒"邮件（异地登录）。

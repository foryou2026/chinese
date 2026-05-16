<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/POST-admin-auth-session-revoke.md -->

# POST /admin/v1/auth/session-revoke

## 1. 概述

本设备退出:删 `user_sessions` 当前 session_id + cookie/clear + 审计。

## 2. 入参

无 (session_id 由 cookie 推出)

## 3. 出参

```json
{ "data": { "ok": true }, "error": null }
```

## 4. 逻辑

```sql
DELETE FROM user_sessions WHERE session_id = $current_sid;
INSERT INTO audit_logs (... 'admin.signout', payload={scope:'local'});
```

后续 handler 调 `cookieService.clear` 三只 cookie + `supabase.auth.signOut({ scope:'local' })`。

## 5. 守卫

`requireAuth` + `requireRole('super_admin')` + `csrfGuard`

## 6. 审计

`admin.signout` (scope=local)

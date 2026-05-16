<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/POST-admin-auth-session-register.md -->

# POST /admin/v1/auth/session-register

## 1. 概述

admin 登录成功后挂会话 + 3 设备硬上限 (surface='admin' 独立计数);**额外做 role 守卫**:若 jwt.role≠'super_admin' → 立即返 `AUTH_USE_USER_ENTRY` 并不挂会话。

## 2. 入参

```json
{ "fingerprint": "<sha256 of UA + accept-lang>", "ua": "Mozilla/...", "ip_hint": "1.2.3.4" }
```

## 3. 出参

```json
{
  "data": {
    "session_id": "<uuid>",
    "kicked": [{ "session_id": "...", "created_at": "..." }]
  },
  "error": null
}
```

## 4. 逻辑

```sql
BEGIN;
  -- role 守卫 (handler 层 requireRole + service 层二次校验)
  IF jwt.app_metadata->>'role' <> 'super_admin' THEN
    RAISE EXCEPTION 'AUTH_USE_USER_ENTRY';
  END IF;

  SELECT * FROM user_sessions
   WHERE user_id = $uid AND surface='admin'
   ORDER BY created_at ASC
   FOR UPDATE SKIP LOCKED;
  -- 若 count >= 3,DELETE oldest;
  INSERT INTO user_sessions (user_id, surface, fingerprint, ua, ip_hint) VALUES (...);
  INSERT INTO audit_logs (actor_user_id, actor_role, event, payload) VALUES
    ($uid, 'super_admin', 'admin.signin_success', jsonb_build_object('kicked', $kicked));
COMMIT;
```

## 5. 守卫

`requireAuth` + `requireRole('super_admin')` + `csrfGuard`

## 6. 错误码

- `AUTH_USE_USER_ENTRY` (双保险;前端登录页主流程也已 signOut)
- 5xx → 通用 Toast

## 7. 审计

`admin.signin_success` (payload 含 kicked 列表 + ip_hint 哈希)

<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/POST-admin-auth-logout-global.md -->

# POST /admin/v1/auth/logout-global

## 1. 概述

全部设备退出:撤销该 user 所有 surface 的全部 refresh + 删该 user 所有 user_sessions + cookie/clear。

## 2. 入参 / 出参

```json
{}
→
{ "data": { "ok": true }, "error": null }
```

## 3. 逻辑

```ts
await supabase.auth.admin.signOut(uid, { scope: 'global' });
await db`DELETE FROM user_sessions WHERE user_id = ${uid}`;
await db`INSERT INTO audit_logs ... 'admin.signout' payload={scope:'global'}`;
await cookieService.clear(['zhiyu-at','zhiyu-rt','zhiyu-csrf']);
```

## 4. 守卫

`requireAuth` + `requireRole('super_admin')` + `csrfGuard`

## 5. 审计

`admin.signout` (scope=global) · 1 条

## 6. 注意

- 删除 user_sessions 时**包括** app surface 的会话 (该超管也是 user 角色场景):scope=global 的语义就是"所有地方都退出";
- v2 若有"仅 admin 设备退出"需求,新增 endpoint `POST /admin/v1/auth/logout-surface`,scope='surface'。

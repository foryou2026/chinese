<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/GET-admin-auth-session-status.md -->

# GET /admin/v1/auth/session-status

## 1. 概述

前端启动时 + 10s 轮询调用;用于检测"被踢"。

## 2. 入参

无

## 3. 出参

```json
{ "data": { "active": true, "kicked_at": null }, "error": null }
```

或 401 + `AUTH_NOT_AUTHED` (token 已失效 / session 已被删 / role 已改)

## 4. 逻辑

1. 从 jwt 取 user_id + 当前 session_id (cookie);
2. 查 `user_sessions` 是否还存在该 session_id AND surface='admin';
3. 不存在 → 视为被踢;返 401 `AUTH_SESSION_KICKED`;
4. 否则返 active=true。

## 5. 守卫

`requireAuth` + `requireRole('super_admin')`

## 6. 审计

不写 (高频)

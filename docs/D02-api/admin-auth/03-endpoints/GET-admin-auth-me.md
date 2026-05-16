<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/GET-admin-auth-me.md -->

# GET /admin/v1/auth/me

## 1. 概述

`/admin/me` 页加载所需:脱敏 email + role + 活跃设备数 + 上次登录时间。

## 2. 入参 / 出参

```json
{}
→
{
  "data": {
    "email_masked": "op***@zhiyu.app",
    "role": "super_admin",
    "active_sessions_count": 2,
    "last_sign_in_at": "2026-05-16T09:30:00Z"
  },
  "error": null
}
```

## 3. 逻辑

```ts
const u = await db`SELECT email FROM auth.users WHERE id=${uid}`;
const lastSignIn = await db`SELECT max(created_at) FROM user_sessions WHERE user_id=${uid} AND surface='admin'`;
const count = await db`SELECT count(*) FROM user_sessions WHERE user_id=${uid} AND surface='admin'`;
return { email_masked: mask(u.email), role:'super_admin', active_sessions_count: count, last_sign_in_at: lastSignIn };
```

`mask(email)`:前 2 字符 + `***` + `@domain`。

## 4. 守卫

`requireAuth` + `requireRole('super_admin')`

## 5. 审计

不写 (读操作)

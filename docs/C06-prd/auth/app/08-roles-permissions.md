<!-- TARGET-PATH: docs/C06-prd/auth/app/08-roles-permissions.md -->

# 08 · 角色 · auth / **app**

| 角色 | 说明 |
|------|------|
| anonymous | 可调 session-status / cookie / throttle / register / login |
| learner | 注册成功即获;可 me / me/password / session-revoke |

无内部角色细分。多端会话由 `auth_sessions` 表记录,`logout-global` 通过 `pgmq` 广播。

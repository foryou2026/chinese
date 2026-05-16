<!-- TARGET-PATH: docs/C05-prd/admin-auth/admin/08-roles-permissions.md -->

# 08 · 角色 · admin-auth / **admin**

| 角色 | 自身权限 |
|------|---------|
| readonly | 只可登录 / me / 改自己密码 |
| content_admin | 同上 |
| super | + 重置他人密码 / 邀请管理员 / 锁解锁 / 触发全局登出 |

> 与 [G3 角色定义](../../../../grules/G3-权限与认证规范/01-角色定义.md) 一致;角色字段存 `admin_users.role`,JWT claims 反射。

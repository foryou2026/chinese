<!-- TARGET-PATH: docs/C05-prd/admin-auth/08-roles-permissions.md -->

# C05 · 08 角色权限 · `admin-auth`

| 行为 | guest | user | super_admin |
|------|-------|------|-------------|
| 访问 `/admin/auth/login` | ✅ | ✅ | ✅ (已登录 → redirect /admin) |
| 登录成功 (role=user) | — | ❌ 立即 signOut | — |
| 登录成功 (role=super_admin) | — | — | ✅ |
| 访问 `/admin/me` | ❌ → 跳 login | ❌ → 跳 login | ✅ |
| 改密 | — | — | ✅ (仅自己) |
| 改他人密 / 改邮箱 / 删账号 | ❌ | ❌ | ❌ (v1 无此功能) |
| 创建新管理员 | ❌ | ❌ | ❌ (运维 SQL) |
| 退出 (本设备 / 全部) | — | — | ✅ |

## 守卫实现

- 前端:`web-admin` `_admin` 根 loader → `assertSession({ role:'super_admin' })`
- 后端:`api-admin` 全路由挂 `requireAuth + requireRole('super_admin')`
- 双重校验缺一不可

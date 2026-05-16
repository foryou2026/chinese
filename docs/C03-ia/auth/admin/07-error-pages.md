<!-- TARGET-PATH: docs/C03-ia/auth/admin/07-error-pages.md -->

# C02 · 错误页 · `auth`

| 错误 | 处理 |
|------|------|
| 未登录 / token 失效 | 守卫跳 `/admin/auth/login?redirect=...` |
| 非 super_admin (含 user 角色) | 立即 signOut + 跳 `/admin/auth/login?error=not_admin` (P-001 not-admin 态) |
| 重置链接过期 | P-003 token-invalid 内嵌态 (不另开页) |
| 锁定 | P-001 locked 内嵌态 |
| 禁用账号 | P-001 error + Toast |
| 服务器 5xx | 全局 Toast (复用 B04-05),不另开页 |
| 路由 404 | 全局 `/admin/404` (不归本 feature) |
| 403 | 全局 `/admin/403` (不归本 feature) |

<!-- TARGET-PATH: docs/C02-ia-interaction/auth/07-error-pages.md -->

# 错误与兜底处理

> **阶段**：C02-IN · **功能**：`auth`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端

| 兜底情况 | 承载方式 | 入口 |
|---------|---------|------|
| 401 未登录访问受保护页 | **不**渲染独立兜底页：守卫直接 redirect 到 P-app-auth-001（带 `redirect=<full-url>`）| TanStack Router `_auth/` loader |
| 403 已登录但访问 admin 入口 | 复用全局 `/403` 毛玻璃页（B02-experience-design/design-system）| api-app 中间件返 `AUTH_FORBIDDEN` |
| 404 路径不存在 | 复用全局 `/404` 毛玻璃页 | router fallback |
| 邮件 / 重置链接过期 | **不**独立成路由，作为 P-app-auth-004 与 P-app-auth-006 的子状态 `token-invalid` | SM-auth-app-04 |
| OAuth provider 异常 | P-app-auth-004 的 `failed` 子状态 + 「重试 / 用邮箱登录」 | SM-auth-app-04 |
| 多设备被踢 | P-app-auth-001 的 `kicked-back` 子状态 + Toast | SM-auth-app-03 reason=kicked |
| 账号已禁用 | P-app-auth-001 的 `error` 子状态 + Toast 提示账号已停用 + 客服入口 | SM-auth-app-03 reason=disabled |
| 网络 / 5xx | 顶部全局 Toast「服务异常」，表单值保留 | SM-auth-app-01 idle_error |

> 维护本功能时**不新增**全局兜底页。

---

## admin 端

| 错误 | 处理 |
|------|------|
| 未登录 / token 失效 | 守卫跳管理端登录页（含回跳参数）|
| 非 admin（含 user 角色）| 立即 signOut + 跳管理端登录页（含回跳参数）（P-admin-auth-001 not-admin 态）|
| 重置链接过期 | P-admin-auth-003 token-invalid 内嵌态（不另开页）|
| 锁定 | P-admin-auth-001 locked 内嵌态 |
| 禁用账号 | P-admin-auth-001 error + Toast |
| 服务器 5xx | 全局 Toast（复用 B02-experience-design design-system），不另开页 |
| 路由 404 | 全局 `/admin/404`（不归本功能）|
| 403 | 全局 `/admin/403`（不归本功能）|

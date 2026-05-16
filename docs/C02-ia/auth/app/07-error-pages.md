<!-- TARGET-PATH: docs/C02-ia/auth/app/07-error-pages.md -->

# `auth` · 系统兜底页

> **冻结状态**：已冻结 · 2026-05-16

| 兜底情况 | 承载方式 | 入口 |
|---------|---------|------|
| 401 未登录访问受保护页 | **不**渲染独立兜底页：守卫直接 redirect 到 `P-auth-001`（带 `redirect=<full-url>`）| TanStack Router `_auth/` loader |
| 403 已登录但访问 admin 入口 | 复用全局 `/403` 毛玻璃页（B04 §02）| api-app 中间件返 `AUTH_FORBIDDEN` |
| 404 路径不存在 | 复用全局 `/404` 毛玻璃页（B04 §02）| router fallback |
| 邮件 / 重置链接过期 | **不**独立成路由，作为 `P-004` 与 `P-006` 的子状态 `token-invalid` | SM-auth-app-04 |
| OAuth provider 异常 | `P-004` 的 `failed` 子状态 + 「重试 / 用邮箱登录」 | SM-auth-app-04 |
| 多设备被踢 | `P-001` 的 `kicked-back` 子状态 + Toast | SM-auth-app-03 reason=kicked |
| 账号已禁用 | `P-001` 的 `error` 子状态 + Toast 含 disabled_reason + 客服入口 | SM-auth-app-03 reason=disabled |
| 网络 / 5xx | 顶部全局 Toast「服务异常」，表单值保留 | SM-auth-app-01 idle_error |

> 维护本 feature 时**不新增**新的全局兜底页。

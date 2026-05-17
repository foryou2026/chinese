<!-- TARGET-PATH: docs/C02-ia-interaction/auth/admin-entry/04-pages.md -->

# 页面清单 · admin-entry

> **阶段**：C02-IN · **模块**：`auth` · **功能**：`admin-entry`
> **冻结状态**：已冻结 · 2026-05-16

---

## admin 端页面（3 页）

| page-id | 名称 | 守卫 | 关联 R-ID | 主要状态 |
|---------|------|------|-----------|---------|
| P-admin-auth-001 | 登录 | 公开 | R-auth-003/004/005/006/016 | idle · submitting · error · not-admin · locked · kicked-back |
| P-admin-auth-002 | 忘记密码 | 公开 | R-auth-007 | idle · submitting · sent · throttled |
| P-admin-auth-003 | 重置密码 | 公开 | R-auth-007/013 | exchanging · idle · submitting · success · token-invalid |

> admin 端 P-001~003 使用居中 GlassCard 布局（无侧边栏）。

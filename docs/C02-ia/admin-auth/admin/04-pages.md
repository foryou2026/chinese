<!-- TARGET-PATH: docs/C02-ia/admin-auth/admin/04-pages.md -->

# C02 · 页面清单 · `admin-auth`

| page-id | slug | 状态 | 守卫 | 覆盖 R-ID |
|---------|------|------|------|-----------|
| P-admin-admin-auth-001 | 登录 | idle / submitting / error / not-admin / locked / kicked-back | 公开 | R-001/002/004/005/009 |
| P-admin-admin-auth-002 | 忘密 | idle / submitting / sent / throttled | 公开 | R-006 |
| P-admin-admin-auth-003 | 重置密码 | exchanging / idle / submitting / success / token-invalid | 公开 | R-006 |
| P-admin-admin-auth-004 | 账号与安全 | view / changing-password / done | super_admin | R-003/007/008 |

> 路径见 [`B02-05 §2.2`](../../B02-permissions/05-auth-feature-guideline.md#22-admin-authadmin)
> 4 页全部使用居中 GlassCard 布局,但 `/admin/me` 嵌在 admin 主框架内 (左侧导航 + 右上头像)。

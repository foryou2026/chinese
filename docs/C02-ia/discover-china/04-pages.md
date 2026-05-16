<!-- TARGET-PATH: docs/C02-ia/discover-china/04-pages.md -->

# 04 · Page 清单

| page-id | 路由 | surface | 角色可见 | 名称 | 覆盖 R-ID |
|---------|------|---------|---------|------|----------|
| `P-app-discover-china-001` | `/china` | app | 任意(04-12 需登录) | 12 类目卡片 | R-001, R-020 |
| `P-app-discover-china-002` | `/china/categories/:code` | app | 公开(01-03) / 登录(04-12) | 类目下文章列表 | R-002, R-007 |
| `P-app-discover-china-003` | `/china/articles/:code` | app | 同上 | 文章逐句详情 + TTS | R-003..006 |
| `P-admin-discover-china-001` | `/admin/china` | admin | super_admin | 12 类目管理卡片 | R-008, R-016, R-018 |
| `P-admin-discover-china-002` | `/admin/china/categories/:code` | admin | super_admin | 类目下文章管理列表 | R-009, R-013, R-014, R-016, R-019 |
| `P-admin-discover-china-003` | `/admin/china/articles/:id` | admin | super_admin | 文章编辑(基本信息 + 句子) | R-010..R-015, R-017, R-019 |
| `P-admin-discover-china-004` | `/admin/china/search` | admin | super_admin | 全局搜索结果聚合 | R-016 |

> **嵌入 / 弹窗清单**详见 [`07-error-pages.md §6`](./07-error-pages.md):D-1..D-8。

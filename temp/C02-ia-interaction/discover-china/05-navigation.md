<!-- TARGET-PATH: docs/C02-ia-interaction/discover-china/05-navigation.md -->

# 导航结构

> **阶段**：C02-IN · **功能**：`discover-china`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端

底部 Tab 中"发现"进入 `/discover` 首页；无独立 Tab 时为 home 卡片入口。

### 路由表

| Path | page-id |
|------|---------|
| `/discover` | P-app-discover-china-001 |
| `/discover/c/:cat` | P-app-discover-china-002 |
| `/discover/a/:slug` | P-app-discover-china-003 |

文章详情面包屑：`首页 / 分类名 / 文章标题`（可点击）。

---

## admin 端

左侧栏顶级「发现中国」：分类（P-001）/ 文章（P-002 → P-003）/ 搜索运维（P-004）。

### 路由表

| Path | page-id |
|------|---------|
| `/admin/discover/categories` | P-admin-discover-china-001 |
| `/admin/discover/articles` | P-admin-discover-china-002 |
| `/admin/discover/articles/:id` | P-admin-discover-china-003 |
| `/admin/discover/search` | P-admin-discover-china-004 |

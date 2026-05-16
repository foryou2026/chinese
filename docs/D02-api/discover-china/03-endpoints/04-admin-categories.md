<!-- TARGET-PATH: docs/D02-api/discover-china/03-endpoints/04-admin-categories.md -->

# 管理端 · 类目(A1)

> 类目固定 12 项,**只读**(PM 答 Q6);无 POST / PUT / DELETE。
> 详见 [F2-04](../../../../function/01-china/ai/F2-AI-接口规范/04-管理端-类目.md)。

## OP-A1 · GET `/admin/v1/china/categories`

| 项 | 内容 |
|----|------|
| 权限 | super_admin |
| 入参 | 无 |
| 出参 | `items[12]`:`{id, code, name_i18n, description_i18n, sort_order, article_count_total, article_count_published}` |
| 字段说明 | `article_count_total`=含 draft + published,**不含**软删;`article_count_published`=仅 published |
| 缓存 | 应用层 30s(管理端 SWR) |
| 错误 | 40100 / 40300 |
| 来源需求 | C01 R-009 |

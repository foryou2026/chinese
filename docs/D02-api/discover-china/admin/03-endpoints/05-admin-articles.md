<!-- TARGET-PATH: docs/D02-api/discover-china/admin/03-endpoints/05-admin-articles.md -->

# 管理端 · 文章 CRUD(A2 .. A8)

> 详细 schema / JSON 见 [F2-05](../../../../function/01-china/ai/F2-AI-接口规范/05-管理端-文章CRUD.md)。

## OP-A2 · GET `/admin/v1/china/categories/:code/articles`

| 项 | 内容 |
|----|------|
| 权限 | super_admin |
| 入参 | path `code`;query `page` / `page_size` / `status∈{draft\|published\|all}` / `q`(全 5 语 + code + title_pinyin + 句子内容 ILIKE) / `sort∈{updated_at\|created_at\|published_at}` ± |
| 出参 | `category{}` + `summary{total,draft,published}` + `items[*]{id,code,title_pinyin,title_i18n,status,sentence_count,published_at,updated_at,updated_by}` + `pagination` |
| 不变量 | code 直接显示(PM Q7);summary 即类目总数 |
| 来源需求 | C01 R-010 |

## OP-A3 · GET `/admin/v1/china/articles/:id`

| 项 | 内容 |
|----|------|
| 用途 | 编辑页顶部基本信息;**不含**句子(走 A9 分页) |
| 出参 | id / code / category{} / title_pinyin / title_i18n / status / sentence_count / 时间字段 / created_by / updated_by |
| 来源需求 | C01 R-011 |

## OP-A4 · POST `/admin/v1/china/articles`

| 项 | 内容 |
|----|------|
| 入参 body | `{category_id, title_pinyin, title_i18n}` |
| 强制 | `status='draft'`;`code` 由 `fn_gen_article_code()` 生成(不接受前端) |
| 出参 | 201 + 同 A3 结构(`sentence_count=0`) |
| 错误 | `CHINA_ARTICLE_TITLE_I18N_MISSING` / `CHINA_ARTICLE_TITLE_TOO_LONG` / `CHINA_ARTICLE_CATEGORY_NOT_FOUND` |
| 来源需求 | C01 R-012 |

## OP-A5 · PATCH `/admin/v1/china/articles/:id`

| 项 | 内容 |
|----|------|
| 允许更新 | `title_pinyin` / `title_i18n` / `category_id`;`code` / `status` 不可改 |
| 并发 | LWW(详 [`../05-concurrency.md`](../05-concurrency.md)) |
| 已发布文章被编辑 | 保持 `published`(不强制回 draft),通过缓存失效在应用端下次请求生效 |
| 来源需求 | C01 R-013 |

## OP-A6 · POST `/admin/v1/china/articles/:id/publish`

| 项 | 内容 |
|----|------|
| 实现 | RPC `fn_publish_article(p_id)` |
| 前置 | status=draft + 未删 + 标题 5 语完整 + sentence_count≥1 + 每句 pinyin + content 5 语 ≤ 上限 |
| 副作用 | 审计;`pg_notify('china_article_published', id::text)` 触发应用层 invalidate;**不**预生成 TTS(PM Q10) |
| 错误 | 409 `CHINA_ARTICLE_STATUS_CONFLICT` / 422 `CHINA_ARTICLE_PUBLISH_NO_SENTENCES` / 422 `CHINA_ARTICLE_PUBLISH_INCOMPLETE_TRANSLATION` |
| 来源需求 | C01 R-014,BR-02,BR-05 |

## OP-A7 · POST `/admin/v1/china/articles/:id/unpublish`

| 项 | 内容 |
|----|------|
| 实现 | RPC `fn_unpublish_article(p_id)` |
| 前置 | status=published + 未删 |
| 副作用 | 审计 + 缓存 invalidate + **`fn_clear_progress_by_article(id)`**(PM Q5,BR-04) |
| 错误 | 409 `CHINA_ARTICLE_STATUS_CONFLICT` |
| 来源需求 | C01 R-015,BR-04 |

## OP-A8 · DELETE `/admin/v1/china/articles/:id`

| 项 | 内容 |
|----|------|
| 行为 | `UPDATE ... SET deleted_at=now(), status='draft', published_at=null`;原 published 同 A7 副作用 |
| 不支持恢复 | (PM Q9);30 天后 cron 物理删,CASCADE 句子 |
| 出参 | 204 |
| 错误 | 404 |
| 来源需求 | C01 R-017,BR-03,BR-06 |

## 通用错误(全管理端)

| HTTP | code |
|------|------|
| 401 | 40100 未登录 |
| 403 | 40300 非 super_admin |
| 400 | 40001 schema 校验失败(详 `errors[]`) |
| 500 | 50000 未捕获异常 |

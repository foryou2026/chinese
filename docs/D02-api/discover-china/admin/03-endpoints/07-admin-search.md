<!-- TARGET-PATH: docs/D02-api/discover-china/admin/03-endpoints/07-admin-search.md -->

# 管理端 · 全局搜索(A15)

> 详见 [F2-10](../../../../function/01-china/ai/F2-AI-接口规范/10-管理端-全局搜索.md)。
> 配套页面 P-A-4(C02 信息架构)。

## OP-A15 · GET `/admin/v1/china/search`

| 项 | 内容 |
|----|------|
| 权限 | super_admin;用户 30 / min 单独限流(防拖库) |
| 入参 | query `q`(必填 1-60) / `scope∈{all\|articles\|sentences}` / `category_code?` / `status?` / `page` / `page_size`(上限 50) |
| 搜索范围 | 文章 `code` + `title_pinyin` + `title_i18n.{zh,en,vi,th,id}` + 句子 `pinyin` + `content_{zh,en,vi,th,id}` ILIKE / GIN trigram |
| 软删过滤 | `articles.deleted_at IS NULL` AND `sentences.deleted_at IS NULL` |
| 出参 | `summary{articles_total,sentences_total,scope}` + `articles[*]{...,highlights[]}` + `sentences[*]{article{},seq_no,seq_label,highlights[]}` + `pagination` |

### 排序规则(PM F3-Q2)
1. 命中文章标题 / 编码优先于命中句子;
2. 同组按 relevance 降序:精确匹配 > 整词匹配 > 子串匹配;
3. 平局按 `updated_at desc`。

### `highlights` 安全
服务端做匹配片段抽取并 `<em>` 包裹;**前端只渲染 `<em>` 白名单**,其余 HTML 全部 escape — 防 XSS。

### 错误

| HTTP | code |
|------|------|
| 400 | `CHINA_SEARCH_QUERY_TOO_SHORT`(45029) |
| 400 | `CHINA_SEARCH_QUERY_TOO_LONG`(45030) |
| 400 | 40002 sort 越界 |
| 504 | 50400 查询超时(3s) |

### 性能
DB statement_timeout 3s;`gin_trgm_ops` 索引覆盖 `content_zh` + `content_en/vi/th/id`(详 [`../../../D01-data/discover-china/06-indexes.md`](../../../D01-data/discover-china/06-indexes.md))。

来源需求:C01 R-016(扩展)、F3-Q2。

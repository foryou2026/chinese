<!-- TARGET-PATH: docs/D02-api/discover-china/app/03-endpoints/01-app-browse.md -->

# 应用端 · 浏览(C1 / C2 / C3 / C5)

> 完整请求 / 响应示例见信息源:
> - [F2-01](../../../../function/01-china/ai/F2-AI-接口规范/01-应用端-类目与文章浏览.md)
> 本文件聚焦端点摘要 + 业务不变量 + 错误清单。

## OP-C1 · GET `/api/v1/china/categories`

| 项 | 内容 |
|----|------|
| 权限 | 公开 |
| 入参 | 无;按 `sort_order asc` 固定顺序 |
| 出参 | `items[12]`:`{code, name_i18n, description_i18n, sort_order}` |
| 缓存 | `public, max-age=3600` |
| 错误 | 仅 5xx |
| 来源需求 | C01 R-001,R-019 |

## OP-C2 · GET `/api/v1/china/categories/:code/articles`

| 项 | 内容 |
|----|------|
| 权限 | 分级公开;`code ≥ '04'` 未登录 → 401 + `redirect_to=/login` |
| 入参 | path `code`(01..12);query `page` / `page_size` / `sort∈{published_at\|-published_at\|title_pinyin}` / `q`(1-60) |
| 搜索范围 | `title_i18n.zh` **OR** `title_i18n.{accept-language}` **OR** 句子 `content_zh` **OR** `content_{accept-language}` ILIKE |
| 出参 | `items[*]`:`{code, title_pinyin, title_i18n, category_code, sentence_count, published_at}` + `pagination` |
| RLS | 仅 `status='published' AND deleted_at IS NULL` |
| 错误 | 40001 / 40101 / 40400 |
| 来源需求 | C01 R-002,R-007 |

## OP-C3 · GET `/api/v1/china/articles/:code`

| 项 | 内容 |
|----|------|
| 权限 | 分级公开(同 C2) |
| 入参 | path `code`(12 位) |
| 出参 | 文章基本信息 + `category{}` + `sentences[*]{id,seq_no,seq_label,pinyin,content{5},audio{status,url,duration_ms}}` + `prev/next`(同类目相邻已发布文章) |
| RLS | 文章 published + 未删 → 404 不暴露 draft / 已删存在 |
| 不变量 | 仅返回 **中文** `audio.url`(F1 Q4);句子按 `seq_no asc`;`prev` / `next` 按 `published_at desc` 取相邻 |
| 错误 | 40001 / 40101 / 40400 |
| 来源需求 | C01 R-003,R-018 |

## OP-C5 · GET `/api/v1/china/articles/:code/audio-playlist`

| 项 | 内容 |
|----|------|
| 权限 | 分级公开(同 C3) |
| 入参 | path `code` |
| 出参 | `items[*]`:`{seq_no, audio_url, status}` 仅 `status='ready'` 的句子被打包;`pending` 句子由前端在播放时回到 C4 触发 |
| 来源需求 | C01 R-005(全文朗读) |

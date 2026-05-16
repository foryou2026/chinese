<!-- TARGET-PATH: docs/D02-api/discover-china/03-endpoints/06-admin-sentences.md -->

# 管理端 · 句子 CRUD(A9 .. A14)

> 详见 [F2-06](../../../../function/01-china/ai/F2-AI-接口规范/06-管理端-句子CRUD.md)。
> **关键约定**:所有"删除 / 插入 / 重排"完成后由 RPC 自动 `fn_resequence_sentences(article_id)` 重排 + 清音频缓存(PM Q8)。
> **跨域进度副作用见 [`../../../D01-data/discover-china/03-business-rules.md §3`](../../../D01-data/discover-china/03-business-rules.md)**。

## OP-A9 · GET `/admin/v1/china/articles/:id/sentences`

| 项 | 内容 |
|----|------|
| 入参 | path `id`;query `page` / `page_size` / `q`(pinyin + content_5lang ILIKE) / `sort∈{seq_no\|-seq_no}` |
| 出参 | `article{}` + `summary{total_sentences}` + `items[*]{id,seq_no,seq_label,pinyin,content{5},audio{...},updated_at,updated_by}` + `pagination` |
| 来源需求 | C01 R-008 |

## OP-A10 · GET `/admin/v1/china/sentences/:id`

| 项 | 内容 |
|----|------|
| 出参 | 单句结构同 A9 `items[*]` |

## OP-A11 · POST `/admin/v1/china/articles/:id/sentences`

| 项 | 内容 |
|----|------|
| body | `{position∈{start\|end\|after}, after_seq_no?, pinyin, content{5}}` |
| 实现 | RPC `fn_insert_sentence_at` + 视位置选择性 `fn_resequence_sentences` |
| 进度副作用 | `position='end'` → **不**清;`'start'/'after'` → **调** `fn_clear_progress_by_article`(PM F3-Q4/Q12,BR-09) |
| 音频副作用 | 受重排影响句子 `audio_status='pending'`,`audio_url_zh=null` |
| 出参 | 201 + `{sentence, affected_sentence_ids[]}` |
| 错误 | `CHINA_SENTENCE_PINYIN_LEN` / `CHINA_SENTENCE_CONTENT_*_LEN` / 40001(after_seq_no 缺) / 404 / 409 `CHINA_SENTENCE_SEQ_OVERFLOW` |
| 来源需求 | C01 R-016 |

## OP-A12 · PATCH `/admin/v1/china/sentences/:id`

| 项 | 内容 |
|----|------|
| body | `{pinyin?, content?{*}}`(部分更新) |
| 不可改 | `seq_no`(走 A14) |
| 副作用 | `content_zh` 变化 → `audio_status='pending'`、`audio_url_zh=null`(其他语言不影响中文 TTS);触发详情缓存失效 |
| **不**清进度 | 仅改内容 / 拼音 / 翻译(BR-09 例外) |
| 来源需求 | C01 R-016 |

## OP-A13 · DELETE `/admin/v1/china/sentences/:id`

| 项 | 内容 |
|----|------|
| 行为 | 软删 → `fn_resequence_sentences` → `fn_clear_progress_by_article` |
| 副作用 | 剩余句子 seq_no 从 1 重排,全 `audio_status='pending'`;所有用户进度清空 |
| 出参 | 200 + `{deleted_sentence_id, affected_sentence_ids[]}` |
| 来源需求 | C01 R-016,BR-04,BR-09 |

## OP-A14 · POST `/admin/v1/china/articles/:id/sentences:reorder`

| 项 | 内容 |
|----|------|
| body | `{ordered_ids: uuid[]}`,长度 = 该文章未删句子数 |
| 实现 | RPC `fn_reorder_sentences(article_id, ordered_ids)` |
| 副作用 | 全句子 seq_no 重写 + 全音频清空 + `fn_clear_progress_by_article` |
| 出参 | `{article_id, items[*]{id,seq_no}}` |
| 错误 | 400 `CHINA_REORDER_IDS_MISMATCH` / 404 |
| 来源需求 | C01 R-016,BR-09 |

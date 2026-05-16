<!-- TARGET-PATH: docs/D01-data/discover-china/06-indexes.md -->

# 06 · 索引清单

## china_categories

| 索引 | 字段 | 类型 | 用途 |
|------|------|------|------|
| `uq_china_categories_code` | `(code)` | UNIQUE | 业务唯一键 |
| `idx_china_categories_sort_order` | `(sort_order)` | B-Tree | 列表排序 |

## china_articles

| 索引 | 字段 | 条件 | 用途 |
|------|------|------|------|
| `uq_china_articles_code` | `(code)` | `WHERE deleted_at IS NULL` | 部分唯一 |
| `idx_china_articles_category_id` | `(category_id)` | 同 | 类目下文章列表 |
| `idx_china_articles_status` | `(status)` | 同 | 状态筛选 |
| `idx_china_articles_published_at` | `(published_at DESC)` | `WHERE status='published' AND deleted_at IS NULL` | 应用端列表按发布时间倒序 |
| `idx_china_articles_created_by` | `(created_by)` | — | 管理端审计 |
| `idx_china_articles_deleted_at` | `(deleted_at)` | — | cron 清理 |

## china_sentences

| 索引 | 字段 | 条件 | 用途 |
|------|------|------|------|
| `uq_china_sentences_article_seq` | `(article_id, seq_no)` | `WHERE deleted_at IS NULL` | 唯一编号 |
| `idx_china_sentences_article_id` | `(article_id)` | 同 | 句子列表 |
| `idx_china_sentences_audio_status` | `(audio_status)` | `WHERE audio_status IN ('pending','processing','failed')` | TTS 调度筛选 |
| `idx_china_sentences_deleted_at` | `(deleted_at)` | — | cron 清理 |

## 全局搜索(管理端 / R-016)

| 索引 | 字段 | 类型 | 用途 |
|------|------|------|------|
| `gin_china_articles_title_zh` | `to_tsvector('simple', title_i18n->>'zh')` | GIN | 文章标题中文模糊 |
| `gin_china_sentences_content_zh` | `to_tsvector('simple', content_zh)` | GIN | 句子中文全文 |

> 仅建中文 GIN;其他语种使用 ILIKE 范围扫描即可(管理员搜索量低,优先节省存储)。

## 不建索引的字段

- `title_i18n` 整 jsonb:仅按 key 校验,无范围查;
- `content_en/vi/th/id`:管理端搜索按需 ILIKE;
- `audio_url_zh` / `audio_provider`:无查询场景。

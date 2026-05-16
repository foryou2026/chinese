<!-- TARGET-PATH: docs/D01-data/discover-china/03-business-rules.md -->

# 03 · 业务规则与状态机

## 1. `china_articles.status` 状态机

```
              ┌──── 创建(默认) ────┐
              ▼                    │
           ┌──────┐  发布   ┌──────────┐
(创建)──▶ │draft │ ──────▶ │published │
           │待发布│ ◀────── │ 已发布   │
           └──────┘  下架   └──────────┘
```

| 从 | 到 | 触发 | 校验 | 字段变化 |
|----|----|------|------|---------|
| (无) | `draft` | 新建文章 | — | `status='draft'`,`published_at=null` |
| `draft` | `published` | `fn_publish_article` | ① 5 语标题非空且 ≤40;② ≥1 条句子;③ 每句 5 语内容非空且 ≤400;④ 操作者 super_admin | `status='published'`,`published_at=now()`,`updated_by=<admin>` |
| `published` | `draft` | `fn_unpublish_article` | 操作者 super_admin | `status='draft'`,`published_at=null`,`updated_by=<admin>` |

## 2. 禁止转换

- `draft → draft` / `published → published`:无意义,前端按钮置灰;
- 任何状态 → 删除:软删独立于 status 字段,不计为状态转换;
- 普通用户:仅 super_admin 可调 `fn_publish_article` / `fn_unpublish_article`;后端绝不信任前端直接写 `status`。

## 3. 跨域副作用(必须事务内执行)

| 触发 | 副作用 |
|------|--------|
| `draft → published`(发布) | ① 审计日志;② 失效 `category_id` 列表缓存;③ **不预生成** TTS,用户首次点击才触发(C01 R-004 / Q10) |
| `published → draft`(下架) | ① 审计;② 缓存失效;③ **`fn_clear_progress_by_article(article_id)` 清空所有用户该文章进度**(C01 BR-04) |
| 软删(任意 → `deleted_at`) | ① 同步置 `status='draft'`;② 同样调 `fn_clear_progress_by_article`;③ 30 天后 cron 物理删 |
| `fn_insert_sentence_at(position='start'\|'after')` | seq_no 位移 → **必须**清进度 |
| `fn_delete_sentence` | seq_no 前移 → **必须**清进度 |
| `fn_reorder_sentences` | seq_no 全洗 → **必须**清进度 |
| `fn_insert_sentence_at(position='end')`(末尾追加) | **不**清进度 |
| `fn_update_sentence`(仅改单句内容/拼音/翻译) | **不**清进度 |

> `fn_clear_progress_by_article` 由 learning-engine 域(`learning_progress` 表所在域)提供;本域 RPC 通过 `SECURITY DEFINER` 调用,参数仅 `article_id`。

## 4. 软删窗口

| 表 | 软删字段 | 物理清理时机 | 触发 |
|----|---------|-------------|------|
| `china_articles` | `deleted_at` | 30 天后 | `cron_china_purge_soft_deleted`(daily 03:00) |
| `china_sentences` | `deleted_at` | 30 天后 | 同上(同时 CASCADE 来自文章删除) |
| Storage 中孤儿 TTS | — | 每周 | `cron_china_purge_orphan_audio` |

不支持恢复(无"恢复"按钮);UI 提示文案统一"删除后 30 天不可恢复"。

## 5. 多语言一致性

- `name_i18n` / `description_i18n` / `title_i18n`:必含 `{zh,en,vi,th,id}` 5 key,jsonb CHECK 约束;
- 句子内容拆 5 列,均 NOT NULL;
- 显示兜底:`<用户 locale>` → `en` → `zh`(与 grules/G1 §八对齐)。

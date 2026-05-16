<!-- TARGET-PATH: docs/D01-data/discover-china/01-er-diagram.md -->

# 01 · ER 图

```
auth.users (id)
   │ created_by / updated_by   ON DELETE SET NULL
   ▼
china_categories (1) ───< (N) china_articles (1) ───< (N) china_sentences
                  category_id                    article_id
                  ON DELETE RESTRICT             ON DELETE CASCADE
```

## 关系明细

| 父表 | 子表 | 外键 | 删除策略 | 理由 |
|------|------|------|---------|------|
| `china_categories` | `china_articles` | `category_id` | **RESTRICT** | 类目固定字典,有引用即拒绝删除(C01 BR-01) |
| `china_articles` | `china_sentences` | `article_id` | **CASCADE** | 句子是文章内嵌结构;软删时通过 `deleted_at` 过滤,物理删除时一并清理 |
| `auth.users` | `china_articles` | `created_by`, `updated_by` | **SET NULL** | 管理员账户被删时保留文章,仅清空操作人字段(弱审计引用) |

## 软删与级联协同

- `china_articles.deleted_at IS NOT NULL` → 列表 / 详情接口默认过滤,其句子不再下发;
- 不支持恢复;`deleted_at` 仅作为物理清理时间锚;
- cron `cron_china_purge_soft_deleted` 每日 03:00 执行:
  - `DELETE FROM china_articles WHERE deleted_at < now() - interval '30 days'`(CASCADE 一并删句子);
  - `DELETE FROM china_sentences WHERE deleted_at < now() - interval '30 days'`(兜底);
  - 同步清理 Storage 中已无外键引用的 TTS 音频文件。

## 跨域副作用(详 [`03-business-rules.md §3`](./03-business-rules.md))

文章 `published → draft` / 软删 + 句子结构变化(插入起始或中间 / 删除 / 重排)→ 调用 learning-engine 域 `fn_clear_progress_by_article(p_article_id)`。

## 基数

- 一篇 `published` 文章至少 1 条 sentence;由 RPC `fn_publish_article` 业务校验,不写 CHECK 避免循环依赖。

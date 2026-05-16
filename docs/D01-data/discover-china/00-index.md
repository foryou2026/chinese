<!-- TARGET-PATH: docs/D01-data/discover-china/00-index.md -->

# D01 · 数据规范 · discover-china

> **阶段**:D01-D · **feature**:`discover-china` · **冻结状态**:已冻结 · 2026-05-16
> **schema**:`zhiyu` · **DB**:自托管 Supabase Postgres 16

| 文件 | 内容 |
|------|------|
| [01-er-diagram.md](./01-er-diagram.md) | ER 图 + 关系明细 + 级联策略 |
| [02-entities/china_categories.md](./02-entities/china_categories.md) | 12 条固定字典 |
| [02-entities/china_articles.md](./02-entities/china_articles.md) | 文章主表(draft/published + 软删) |
| [02-entities/china_sentences.md](./02-entities/china_sentences.md) | 句子表(拼音 + 5 语内容 + TTS 字段) |
| [03-business-rules.md](./03-business-rules.md) | 状态机 / 软删 / 跨域副作用 |
| [04-validations.md](./04-validations.md) | Zod 校验规则与错误码 |
| [05-calculations.md](./05-calculations.md) | RPC 函数:编号生成 / 重排 / 发布 |
| [06-indexes.md](./06-indexes.md) | 索引清单与说明 |
| [07-volume-growth.md](./07-volume-growth.md) | 容量估算 |
| [08-seed-data.md](./08-seed-data.md) | 12 类目 + dev 示例文章 |
| [99-open-questions.md](./99-open-questions.md) | 待确认问题 |

## 命名约定
- 表名前缀 `china_`;
- 多语言字段后缀 `_i18n`,jsonb 必含 `{zh,en,vi,th,id}` 5 key;
- RPC 前缀 `fn_*`,触发器 `tg_<table>_*`,策略 `<table>_<action>_<role>`。

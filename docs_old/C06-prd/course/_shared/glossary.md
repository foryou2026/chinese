<!-- TARGET-PATH: docs/C06-prd/course/_shared/glossary.md -->

# course feature · 共享术语表

> **跨 surface 共享术语表(Round 2 从 PRD.md 第 2 章迁出)。** app/admin 双端均引用本文件。

## 2. 术语表

| 术语 | 说明 |
|------|------|
| 主题(Track)| 5 个固定主题码 `share / ec / fc / hsk / dl` |
| 阶段(Stage)| 主题下 6 级阶段(Stage 0..6);`share` 提供共享 Stage 0 一次性预备 |
| 章(Chapter)| 每阶段 6 章 |
| 节(Lesson)| 每章 6 节;节 code 格式 `{track}-{stage}-{chapter}-{lesson}` |
| KP(Knowledge Point)| 7 类:pinyin / hanzi / word / phrase / grammar / sentence / dialog;code 格式 `kp_{track}_{type_initial}_{seq5}` |
| 题目(Question)| 12 种:mcq_meaning / mcq_zh / listen_pick / listen_pinyin / tone_pick / match_pairs / sort_words / fill_blank_choice / type_pinyin / type_zh_ime / image_pick / dialog_cloze;code 格式 `q_{track}_{seq8}` |
| 节末小测 | 节学习后 6 题统一交卷,可跳过(`is_quiz_required=false`),通过线 60% |
| 章测 / 阶段考 / HSK 模考 | 见 §7 BR-EXAM 段 |
| SRS | Leitner 5 盒,间隔 1 / 3 / 7 / 14 / 30 天 |
| 5 语 | `zh / en / vi / th / id`,与 discover-china 等其他 feature 全局对齐 |
| Admin 角色 | 仅 `admin`（全局唯一管理员角色，遵从 [C02-permissions/01-roles.md](../../../C02-permissions/01-roles.md)）；course admin 端不再设 scope/readonly 等子角色 |

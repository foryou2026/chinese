<!-- TARGET-PATH: docs/C05-prd/course/admin/02-glossary.md -->

> **本文件为 surface=`admin` 视角的 PRD 章节(Round 2 从 PRD.md 第 2 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

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
| Admin 角色 | `super / content_admin / readonly`,行级 `admins.tracks_scope[]` 过滤可见主题 |

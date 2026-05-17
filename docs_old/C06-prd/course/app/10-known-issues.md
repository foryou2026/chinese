<!-- TARGET-PATH: docs/C06-prd/course/app/10-known-issues.md -->

# 10 · 已知问题 · course / **app**

> 写未发布给学员的、当前阶段已识别的问题。Q-ID 命名:`KI-app-course-NNN`。

## 10.1 当前(2026-05)

| ID | 一句话 | 影响 | 计划处置 |
|----|-------|------|---------|
| KI-app-course-001 | iOS Safari 在弱网下音频缓冲常失败 | 节内 KP 音频 | 切 HLS 分片;Round 9+ 排期 |
| KI-app-course-002 | 5 语切换时,SRS 队列翻译字段未热更 | [P-004](06-page-specs/P-app-course-004.md) | 翻译走客户端 i18n 而非服务端缓存即可解决 |
| KI-app-course-003 | 大答题集(50 题/节)在低端 Android 内存触顶 | [P-003](06-page-specs/P-app-course-003.md) | 改为分批拉取 ≤ 10 题 |
| KI-app-course-004 | 考试中切后台 5 min 时长上限过严,实际地铁场景常超 | [P-007](06-page-specs/P-app-course-007.md) | 评估放宽到 10 min |

## 10.2 已澄清但暂不修

| ID | 一句话 | 原因 |
|----|-------|------|
| KI-app-course-005 | 不支持手写输入 | 与"题型纯静默原则"一致,**不做** |
| KI-app-course-006 | 不支持口语跟读 | 与"明确不做"一致 |

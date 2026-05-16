<!-- TARGET-PATH: docs/C05-prd/course/admin/09-design-summary.md -->

> **本文件为 surface=`admin` 视角的 PRD 章节(Round 2 从 PRD.md 第 9 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

## 9. 数据量级与性能基线

- 课程骨架:5 主题 / 25 阶段 / 148 章 / 888 节 / ~12 000 KP / ~50 000 题 / ~20 000 音频;
- 单节聚合接口 `GET /app/lesson/{code}` 响应体 ≤ 200 KB(`gzip`),P95 ≤ 300ms;
- `GET /app/srs/today` 单用户单次 LIMIT 50 → P95 ≤ 200ms;
- 答题 `POST /app/answer` P95 ≤ 150ms;
- 考试交卷 `POST /app/exam/{attempt}/submit` 批量判分 50 题 P95 ≤ 800ms;
- 限流:`/app/answer` 60 次/分/用户 → 超出 429。

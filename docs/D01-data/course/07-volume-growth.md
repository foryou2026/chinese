<!-- TARGET-PATH: docs/D01-data/course/07-volume-growth.md -->

# 07 · 数据量级与增长 · course

## 7.1 一次性结构数据(冷数据,基本不增)

| 表 | 量级 | 来源 |
|----|------|------|
| `course_tracks` | 5 | seed |
| `course_stages` | 25(share 1 + ec/fc/hsk/dl × 6) | seed |
| `course_chapters` | ~148(平均 6 章/阶段)| 内容运营手工/批量导入 |
| `course_lessons` | ~888(平均 6 节/章)| 同上 |
| `course_lesson_kp` | ~10 656(平均 12 KP/节) | 同上 |
| `course_knowledge_points` | ~11 200(去重后) | 内容导入 |
| `course_questions` | 5–7 万 | 内容导入 |
| `course_exams` | ~40–50(节末/章/阶段/HSK) | 后台手工 + 自动 |

## 7.2 流水类(高写入)

| 表 | 单学员 / 日 | 总量(10 万学员 / 1 年) | 增长方式 |
|----|-----------|--------------------|---------|
| `course_user_progress` | 1–3 行/日(节通过) | 静态 ~10 万 × 888 | 单 row 多次 UPDATE,行数封顶 |
| `course_user_answers` | 100–200 行/日 | **~5–7 亿/年**(50 GB+) | 月分区 |
| `course_user_srs` | 4–8 行/日(KP 上限) | 静态 ~10 万 × 11200(理论) → 实际按学习覆盖 ~100 万 | UPSERT |
| `course_user_exam_attempts` | 0.1–0.5/日 | ~500 万/年 | INSERT-only |
| `course_content_action_log` | 学员举报 + 管理操作 | ~50 万/年 | INSERT-only |
| `course_import_batches` | — | ~100 个/月 | 低 |
| `course_media_assets` | — | ~3 万(hash 去重)| 低 |

## 7.3 分区与归档策略

- **`course_user_answers`**:
  - 月分区,命名 `course_user_answers_yYYYY_mMM`;
  - 0–6 月:in-DB 在线;
  - 7–24 月:in-DB 但建索引精简;
  - > 24 月:导出至对象存储 + DETACH PARTITION(本期保留 stub,P2 实施)。
- **`course_content_action_log`**:90 天保留(沿用平台日志策略),cron 按 `created_at < now() - interval '90 days'` 批删;
- 其余表无归档需求。

## 7.4 物化视图刷新

| MV | 行数 | 刷新 | 用途 |
|----|------|------|------|
| `mv_course_track_stats` | 5 | 10 分钟 CONCURRENTLY | 后台总览 |
| `mv_course_user_daily` | ~10 万 × 7 天滚动 = ~70 万 | 5 分钟 CONCURRENTLY | C 端"今日数据" |

## 7.5 容量警戒线

| 指标 | 阈值 | 处置 |
|------|------|------|
| 单月 `course_user_answers` 行数 | > 8 000 万 | 启动归档评估 |
| 单 KP 关联题数 | > 200 | 内容侧告警 |
| 单 attempt snapshot 题数 | > 200 | 设硬上限,F1 默认 ≤ 100 |
| MV 刷新耗时 | > 30 s | 调度告警 + 增加并发或分桶 |

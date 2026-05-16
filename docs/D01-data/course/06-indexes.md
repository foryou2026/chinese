<!-- TARGET-PATH: docs/D01-data/course/06-indexes.md -->

# 06 · 索引清单 · course

> 全表完整索引;`*` 标注 partial(WHERE `deleted_at IS NULL`)。

## UNIQUE

| 索引名 | 表 | 列 | 备注 |
|--------|----|----|------|
| `uq_course_tracks_code` | tracks | `(code)` | 5 主题 |
| `uq_course_stages_track_stage` | stages | `(track_code, stage_no)` |  |
| `uq_course_chapters_stage_no` * | chapters | `(stage_id, chapter_no)` |  |
| `uq_course_lessons_code` * | lessons | `(code)` |  |
| `uq_course_lessons_chapter_no` * | lessons | `(chapter_id, lesson_no)` |  |
| `uq_course_kp_code` * | kp | `(kp_code)` |  |
| `uq_course_q_code` * | questions | `(q_code)` |  |
| `uq_course_q_kp_qtype_hash` * | questions | `(kp_id, q_type, payload_hash)` | 去重 Q9 |
| `uq_course_exams_code` * | exams | `(code)` |  |
| `uq_course_exams_unique_per_scope` ** | exams | `(scope_type, scope_ref_id)` WHERE `deleted_at IS NULL AND scope_type IN ('lesson_quiz','chapter_test','stage_exam')` | 一节/章/阶段一卷 |
| `uq_course_import_batch_code` | import_batches | `(batch_code)` |  |
| `uq_course_ma_hash` | media_assets | `(hash)` | sha256 去重 |
| `uq_course_uea_attempt_no` | user_exam_attempts | `(user_id, exam_id, attempt_no)` |  |

## 常规 B-tree

| 表 | 列 | 用途 |
|----|----|------|
| stages | `track_code`, `is_published` | 列表 |
| chapters | `stage_id`, `is_published`, `deleted_at` | 列表 + 软删扫描 |
| lessons | `chapter_id`, `is_published`, `published_at`, `deleted_at` | 学习地图、cron |
| kp | `kp_type`, `primary_track`, `is_published`, `difficulty`, `title_zh`, `source_batch_id`, `deleted_at` | 后台筛选 |
| questions | `kp_id`, `q_type`, `is_published`, `difficulty`, `source_batch_id`, `report_count`, `deleted_at` | 抽题 + 后台 |
| lesson_kp | `(lesson_id, position)`, `(kp_id)` | 节内列出 + 反查 |
| exams | `scope_type`, `scope_ref_id`, `is_published`, `deleted_at` | 模板查询 |
| user_progress | `(user_id, status)`, `(lesson_id)`, `(lesson_id, passed_at) WHERE status='passed'` | 个人地图 |
| user_answers | `(user_id, kp_id)`, `(user_id, answered_at DESC)`, `(question_id)`, `(context_type, context_ref_id)`, `(answered_at)` | 错题/SRS/统计 |
| user_srs | `(user_id, due_at)`, `(user_id, box, due_at)` | 队列发卡 |
| user_exam_attempts | `(user_id)`, `(exam_id)`, `(user_id, passed)`, `(state, expires_at) WHERE state='in_progress'` | 个人 + cron |
| import_batches | `import_type`, `track`, `status`, `created_by`, `created_at`, `payload_hash` | 后台 |
| content_action_log | `(target_type, target_id, created_at DESC)`, `(action)`, `(actor_id)`, `(created_at)` | 审计 |
| media_assets | `kind`, `source`, `ref_kp_id`, `ref_q_id` | 后台 |

## GIN(JSON / 数组)

| 索引 | 表 | 列 |
|------|----|----|
| `idx_course_kp_tags_gin` | kp | `tags` |
| `idx_course_kp_content_gin` | kp | `content` |
| `idx_course_q_exam_scope` | questions | `exam_scope` |
| `idx_course_exams_blueprint_gin` | exams | `blueprint` |

## 全文搜索(管理端 `OP-course-admin-023`)

- 后台搜索基于 PG `to_tsvector('simple', title_zh || ' ' || coalesce(translations->>'en',''))` 临时表达式;
- 若后续命中性能阈值 → 增加表达式索引 `using gin (to_tsvector(...))`(本期不预建,留观察);
- 不支持拼音搜索(F2 Q7 决策)。

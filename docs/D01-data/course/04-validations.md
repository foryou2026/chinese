<!-- TARGET-PATH: docs/D01-data/course/04-validations.md -->

# 04 · 字段校验汇总 · course

## 4.1 通用正则

| 模式 | 含义 | 应用字段 |
|------|------|---------|
| `^(share\|ec\|fc\|hsk\|dl)$` | 5 主题白名单 | `course_tracks.code`, FK 外键到该字段的列 |
| `^(share\|ec\|fc\|hsk\|dl)-\d{1,2}-\d{1,2}-\d{1,2}$` | 节 code | `course_lessons.code` |
| `^kp_(share\|ec\|fc\|hsk\|dl)_(p\|h\|w\|ph\|g\|s\|d)_\d{6}$` | KP code | `course_knowledge_points.kp_code` |
| `^q_(share\|ec\|fc\|hsk\|dl)_\d{8}$` | 题 code | `course_questions.q_code` |
| `^exam_(lq\|ct\|se\|hm)_\d{6}$` | 试卷 code | `course_exams.code` |
| `^imp_(kp\|question\|media)_\d{8}_\d{4}$` | 导入批次 code | `course_import_batches.batch_code` |
| `^[a-f0-9]{64}$` | sha256 hex | `course_media_assets.hash`, `course_questions.payload_hash`, `course_import_batches.payload_hash` |
| `^HSK[1-6]$` | HSK 映射 | `course_stages.hsk_mapping` |

## 4.2 范围 / 枚举

| 字段 | 约束 |
|------|------|
| `course_stages.stage_no` | 0–6;`stage_no=0` 仅允许 `track_code='share'` |
| `course_chapters.chapter_no` | 1–20 |
| `course_lessons.lesson_no` | 1–30 |
| `course_lessons.est_minutes` | 5–30 |
| `course_lesson_kp.position` | 1–50 |
| `course_knowledge_points.difficulty` | 1–6 |
| `course_knowledge_points.hsk_level` | NULL 或 1–6 |
| `course_knowledge_points.version` | ≥ 1 |
| `course_knowledge_points.kp_type` | 7 枚举 |
| `course_questions.q_type` | 12 枚举 |
| `course_questions.exam_scope` | 子集 `{practice,lesson_quiz,chapter_test,stage_exam,hsk_mock}` 且长度 ≥ 1 |
| `course_questions.report_count` | ≥ 0 |
| `course_exams.scope_type` | 4 枚举 |
| `course_exams.pass_score` | 0–100 且 ≤ total_score |
| `course_exams.total_score` | > 0 且 ≤ 1000 |
| `course_exams.time_limit_minutes` | NULL 或 0–180 |
| `course_user_progress.status` | 4 枚举;`passed` 时 `passed_at NOT NULL` |
| `course_user_progress.best_score` | NULL 或 0–100 |
| `course_user_progress.last_position` | 0–100 |
| `course_user_answers.context_type` | 6 枚举 |
| `course_user_answers.score` | 0–10 |
| `course_user_answers.duration_ms` | NULL 或 0–600000 |
| `course_user_srs.box` | 1–5 |
| `course_user_exam_attempts.state` | 4 枚举;非 in_progress 时 `finished_at NOT NULL` |
| `course_import_batches.status` | 6 枚举 |
| `course_import_batches.import_type` | 3 枚举 |
| `course_media_assets.kind` | 5 枚举 |
| `course_media_assets.source` | 4 枚举 |
| `course_media_assets.url` | 长度 1–500 |
| `course_content_action_log.action` | 7 枚举 |
| `course_content_action_log.actor_role` | 3 枚举 |
| `course_content_action_log.report_type` | NULL 或 5 枚举;且 `action='report' ⇔ NOT NULL` |
| `course_content_action_log.reason` | 长度 ≤ 500 |

## 4.3 长度

| 字段 | 长度 |
|------|------|
| `*.name_zh / title_zh` | 1–20 / 1–40 / 1–60(按表)|
| `*.pinyin` | 1–200 |
| `*.title_i18n / desc_i18n / goal_i18n` 各 lang 值 | ≤ 200 / 80 字符(按表)|

## 4.4 5 语 jsonb 必填集

CHECK `<col> ?& array['zh','en','vi','th','id']`,应用于:
- `course_tracks.name_i18n`
- `course_stages.title_i18n` `desc_i18n`(可选时跳过)
- `course_chapters.title_i18n`
- `course_lessons.title_i18n`,`goal_i18n`(可空,有则全)
- `course_knowledge_points.translations`(可空,有则全)
- `course_exams.title_i18n`(可空,有则全)

## 4.5 跨字段一致性

| 字段对 | 约束 |
|--------|------|
| `is_published / published_at` | 同时为真或同时为假(`(published AND NOT NULL) OR (NOT published AND NULL)`)|
| `course_lessons.code` | 须匹配 `<lesson.chapter.stage.track>-<stage_no>-<chapter_no>-<lesson_no>`(应用层校验)|
| `course_exams.pass_score ≤ total_score` | CHECK |
| `course_exams.scope_type vs scope_ref_id` 类型 | 应用层强制(lesson_quiz→lessons.id 等)|
| `course_content_action_log.action='report' ⇔ report_type NOT NULL` | CHECK |
| `course_user_exam_attempts.state='in_progress' ⇔ finished_at IS NULL` | CHECK |

## 4.6 RPC 入口校验

- `fn_submit_answer`:校验 `user_id = auth.uid()`、`question.is_published=true`、`question.deleted_at IS NULL`、`payload` 与 `q_type` 匹配 → 否则返 `COURSE_PAYLOAD_SCHEMA_MISMATCH`;
- `fn_start_exam`:校验前置 stage 已通过(BR-CC-04);
- `fn_lesson_pass`:校验小测分 ≥ pass_score;
- `fn_get_srs_queue`:校验今日 `srs_review` 计数 < 50。

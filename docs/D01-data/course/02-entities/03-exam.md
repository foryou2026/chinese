<!-- TARGET-PATH: docs/D01-data/course/02-entities/03-exam.md -->

# 02-3 · 考试(2 表) · course

> 直读 F1:[03-表定义-考试与作答.md](../../../../function/02-course/ai/F1-AI-数据模型规范/03-表定义-考试与作答.md)。

---

## T08 · `course_exams`(试卷模板,~40-50 条)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| code | text | partial-UNIQUE;CHECK `~ '^exam_(lq|ct|se|hm)_\d{6}$'` |
| scope_type | text | CHECK `IN ('lesson_quiz','chapter_test','stage_exam','hsk_mock')` |
| scope_ref_id | uuid | 多态弱引用(lesson_quiz→lesson.id / chapter_test→chapter.id / stage_exam,hsk_mock→stage.id);无 FK,应用层校验 |
| title_zh | text | 1–60 |
| title_i18n | jsonb |  | 5 语 `?& {...}`(可空)|
| pass_score | numeric(5,2) | CHECK 0–100,默认 60;且 ≤ total_score |
| total_score | numeric(5,2) | CHECK > 0 且 ≤ 1000,默认 100 |
| time_limit_minutes | int | CHECK NULL OR 0–180 |
| blueprint | jsonb | 出卷规则:`{items:[{q_type, count, kp_filter, difficulty_range}]}`;GIN 索引 |
| is_published | bool | 默认 false |
| created_by | uuid | FK `auth.users(id)` ON DELETE SET NULL |
| created_at / updated_at | timestamptz |  |
| deleted_at | timestamptz | 软删 |

**索引**:
- `uq_course_exams_code` UNIQUE (WHERE deleted_at NULL);
- `uq_course_exams_unique_per_scope (scope_type, scope_ref_id)` UNIQUE (WHERE deleted_at NULL AND `scope_type IN ('lesson_quiz','chapter_test','stage_exam')`)——一节/章/阶段一卷;
- `idx_course_exams_scope / scope_ref / published / deleted_at`;
- GIN `idx_course_exams_blueprint_gin (blueprint)`。

**RLS**:`select` authed → `is_published=true AND deleted_at IS NULL`;写 `service_role`。

**试抽预览**:`OP-course-admin-022` 仅渲染,**不写** `course_user_exam_attempts`(决策对应 BR-E07)。

---

## T09 · `course_user_exam_attempts`(学员答卷)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid | PK |
| user_id | uuid | FK `auth.users(id)` ON DELETE CASCADE |
| exam_id | uuid | FK `course_exams(id)` ON DELETE RESTRICT |
| attempt_no | int | CHECK ≥ 1 |
| score | numeric(5,2) | CHECK NULL OR 0–100 |
| passed | bool |  |
| snapshot | jsonb | `{q_ids:[uuid], q_versions:{uuid:int}, blueprint_copy:{...}, started_blueprint_at:ts}` |
| state | text | CHECK `IN ('in_progress','submitted','expired','abandoned')` |
| started_at | timestamptz | 默认 now() |
| expires_at | timestamptz | `started_at + exam.time_limit_minutes` 或 NULL |
| finished_at | timestamptz | CHECK `(state='in_progress' AND NULL) OR (state<>'in_progress' AND NOT NULL)` |

- UNIQUE `(user_id, exam_id, attempt_no)`;
- 索引:`idx_course_uea_user / exam / passed`、`idx_course_uea_state (state, expires_at) WHERE state='in_progress'`(cron 超期扫);
- RLS:`select` authed → `user_id = auth.uid()`;写 `service_role`;
- 软删:无(学员答卷不删);
- 决策 H5(阶段考过不可重考)由应用层校验:`scope_type='stage_exam'` 且存在 `passed=true` 的 attempt → 创建新 attempt 时返 `COURSE_STAGE_EXAM_ALREADY_PASSED`。

## 评分快照(BR-E02)
- 满分恒 = `course_exams.total_score`(默认 100);
- 单题分 = `total_score / array_length(snapshot.q_ids)`;
- 题目下架不重算已存 attempt(snapshot 固化)。

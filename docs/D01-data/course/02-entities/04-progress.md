<!-- TARGET-PATH: docs/D01-data/course/02-entities/04-progress.md -->

# 02-4 · 学员进度 + 流水 + SRS(3 表) · course

> 直读 F1:[04-表定义-学员进度.md](../../../../function/02-course/ai/F1-AI-数据模型规范/04-表定义-学员进度.md)。

---

## T10 · `course_user_progress`(节级进度)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| user_id | uuid | PK 一部分;FK `auth.users(id)` ON DELETE CASCADE |
| lesson_id | uuid | PK 一部分;FK `course_lessons(id)` ON DELETE CASCADE |
| status | text | CHECK `IN ('locked','unlocked','in_progress','passed')` |
| last_kp_id | uuid | FK `course_knowledge_points(id)` ON DELETE SET NULL;断点续学 |
| last_position | int | CHECK 0–100;节内卡片序号 |
| best_score | numeric(5,2) | CHECK NULL OR 0–100 |
| attempts | int | 默认 0;CHECK ≥ 0 |
| passed_at | timestamptz | CHECK `(status='passed' AND NOT NULL) OR status<>'passed'` |
| started_at | timestamptz |  |
| updated_at | timestamptz |  |

- 索引:`idx_course_up_status (user_id, status)`、`idx_course_up_lesson (lesson_id)`、`idx_course_up_passed (lesson_id, passed_at) WHERE status='passed'`;
- RLS:自读自写(`user_id = auth.uid()`),写入走 RPC;
- 触发器:`tg_after_lesson_pass_unlock_next` 在 `status` 变 `passed` 时为同章下一节 / 阶段考通过后下一阶段所有节插入 `status='unlocked'`。

## T11 · `course_user_answers`(答题流水,月分区)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| id | uuid |  |
| answered_at | timestamptz | PK = `(id, answered_at)`;分区键 |
| user_id | uuid | FK `auth.users(id)` ON DELETE CASCADE |
| question_id | uuid | FK `course_questions(id)` ON DELETE RESTRICT |
| question_version | int | CHECK ≥ 1;**保留作答时 version,后续修订不追溯**(BR-RP04)|
| kp_id | uuid | FK `course_knowledge_points(id)` ON DELETE RESTRICT |
| context_type | text | CHECK `IN ('practice','lesson_quiz','chapter_test','stage_exam','hsk_mock','srs_review')` |
| context_ref_id | uuid | 多态:lesson_id 或 attempt_id |
| is_correct | bool |  |
| score | numeric(5,2) | CHECK 0–10(连线题可 0.25 步长)|
| user_answer | jsonb | 学员答案结构 |
| duration_ms | int | CHECK NULL OR 0–600000(10 分钟)|

- 索引:`idx_course_ua_user_kp (user_id, kp_id)`(SRS / 错题统计)、`idx_course_ua_user_ans (user_id, answered_at DESC)`、`idx_course_ua_question / context (context_type, context_ref_id) / answered_at`;
- 分区:`pg_partman` 月分区,自动建分区;
- RLS:`select` authed → `user_id = auth.uid()`;`insert` authed via RPC `fn_submit_answer`(校验 user_id);`update/delete` 禁;
- 副作用:除 `context_type='practice'` 外,均触发 `fn_srs_update`。

## T12 · `course_user_srs`(SRS Leitner 5 盒)

| 字段 | 类型 | 关键约束 |
|------|------|---------|
| user_id | uuid | PK 一部分 |
| kp_id | uuid | PK 一部分;FK ON DELETE CASCADE |
| box | smallint | CHECK 1–5 |
| due_at | timestamptz | 下次到期 |
| correct_streak | int | CHECK ≥ 0 |
| wrong_count | int | CHECK ≥ 0 |
| last_seen_at | timestamptz |  |
| last_q_type | text | CHECK NULL OR `IN (12 题型枚举)` |

- 索引:`idx_course_srs_due (user_id, due_at)`、`idx_course_srs_box (user_id, box, due_at)`;
- RLS:自读自写;
- 更新规则:见 [05-calculations.md §SRS](../05-calculations.md);
- UPSERT 原子:`INSERT ... ON CONFLICT (user_id, kp_id) DO UPDATE SET ...`(无双计)。

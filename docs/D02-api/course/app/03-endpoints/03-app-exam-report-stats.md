<!-- TARGET-PATH: docs/D02-api/course/app/03-endpoints/03-app-exam-report-stats.md -->

# 03-3 · 学员端 · 考试 / 举报 / 统计 (OP-C13..C19)

## OP-course-app-013 · `GET /exams`
- 用途:列出可参加考试
- Query:`?track=&scope_type=stage_exam`
- 响应:`{ items:[{exam_id, scope_type, title_i18n, pass_score, total_score, time_limit_minutes, question_count, my_status:{best_score,passed,attempts}}] }`
- 算法:`course_exams JOIN scope_ref → progress / attempts`;RLS 过滤已发布

## OP-course-app-014 · `POST /exams/:exam_id:start`
- 用途:开始考试
- 副作用(`fn_start_exam`):
  1. 校验前置 stage 通过 / 阶段考未通过过(BR-EX-03);
  2. 按 blueprint 抽题(`exam_scope` 匹配 + KP 范围 + 难度/题型分布);
  3. INSERT `course_user_exam_attempts(state='in_progress', snapshot)`;
- 响应:`{ attempt_id, started_at, expires_at, question_ids:[uuid] }`
- 错误:
  - 403 `COURSE_PREREQUISITE_NOT_MET` / `COURSE_STAGE_EXAM_ALREADY_PASSED` / `COURSE_EXAM_LOCKED`;
  - 409 `COURSE_EXAM_EFFECTIVE_QUESTION_EMPTY`(有效题不足)

## OP-course-app-015 · `GET /exam-attempts/:attempt_id`
- 用途:取 attempt 题目(进行中续答)
- 响应:`{ attempt, questions:[{id,q_type,payload}], remaining_sec }`
- 校验:`user_id = auth.uid()`;`state='in_progress' AND now() < expires_at`,否则:
  - `state='expired' or now()>expires_at` → 自动补算 + 返 410 `COURSE_EXAM_EXPIRED`;
  - `state='submitted'` → 200 返历史(只读)

## OP-course-app-016 · `POST /exam-attempts/:attempt_id:submit`
- 用途:提交考试
- Request:`{ answers:[{question_id, user_answer, duration_ms}] }`
- 副作用(`fn_submit_exam` 内 `SELECT FOR UPDATE`):
  1. 行锁后检查 state='in_progress' 且未过期;
  2. 逐题写 `course_user_answers(context_type=<scope_type>, context_ref_id=attempt_id)`;
  3. 算分,UPDATE `course_user_exam_attempts(state='submitted', score, passed, finished_at)`;
  4. 若 `scope_type='stage_exam' AND passed=true` → 解锁下一阶段;
- 响应:`{ score, passed, wrong_questions:[...], unlocked_next_stage?: stage_id }`
- 错误:`COURSE_EXAM_EXPIRED` 410 / `COURSE_INVALID_PUBLISH_ACTION` 400(state 不允许)

## OP-course-app-017 · `POST /exam-attempts/:attempt_id:abandon`
- 用途:放弃考试
- 副作用:UPDATE state='abandoned', score=0, passed=false, finished_at=now()
- 响应:`{ abandoned: true }`

## OP-course-app-018 · `POST /questions/:q_id:report`
- 用途:学员举报题目
- Request:`{ report_type: 'wrong_answer|wrong_translation|wrong_audio|wrong_image|other', reason }`
- 副作用(`fn_report_question`):
  1. 24h 去重检查 → 否则 409 `COURSE_REPORT_DUPLICATE`;
  2. INSERT `course_content_action_log(action='report')`;
  3. UPDATE `course_questions.report_count += 1`;
- 响应:`{ reported: true }`
- 错误:`COURSE_REPORT_TYPE_REQUIRED` 400

## OP-course-app-019 · `GET /me/stats`
- 用途:个人首页 / Profile 统计卡
- 响应:`{ current_stage, lessons_passed, kp_mastered, accuracy, streak_days, today:{answered, correct, srs_done} }`
- 数据源:`mv_course_user_daily` + 实时计算 streak

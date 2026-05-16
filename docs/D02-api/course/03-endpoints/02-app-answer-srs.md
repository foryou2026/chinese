<!-- TARGET-PATH: docs/D02-api/course/03-endpoints/02-app-answer-srs.md -->

# 03-2 · 学员端 · 作答 / SRS / 错题本 (OP-C9..C12)

## OP-course-app-009 · `POST /answers`
- 用途:提交单题作答(节内 / 小测 / 考试 / SRS 复习 / 练习 共用)
- 鉴权:登录;`user_id = auth.uid()`
- 限流:600/分/UID
- Request:
  ```json
  {
    "question_id": "uuid",
    "context_type": "practice|lesson_quiz|chapter_test|stage_exam|hsk_mock|srs_review",
    "context_ref_id": "uuid",
    "user_answer": { ... },
    "duration_ms": 4500
  }
  ```
- 副作用(RPC `fn_submit_answer`):
  1. 校验 question 已发布且未软删 + payload schema 匹配 q_type → 否则 `COURSE_PAYLOAD_SCHEMA_MISMATCH`;
  2. 评分 → INSERT `course_user_answers`(`question_version = course_questions.version` 快照);
  3. 若 `context_type != 'practice'` → 调 `fn_srs_update`;
- 响应 200:
  ```json
  { "is_correct": true, "score": 8.5, "explanation": "...", "srs_after": {"box":3,"due_at":"..."} }
  ```
- 错误:
  - 400 `COURSE_PAYLOAD_SCHEMA_MISMATCH` / `COURSE_ITEM_SCORE_OUT_OF_RANGE` / `COURSE_DURATION_OUT_OF_RANGE`;
  - 403 `COURSE_LESSON_NOT_ENTERED`(quiz 上下文未进过节)、`COURSE_FORBIDDEN_OTHER_USER`;
  - 410 `COURSE_QUIZ_EXPIRED` / `COURSE_EXAM_EXPIRED`;
  - 429 `COURSE_RATE_LIMIT`。

## OP-course-app-010 · `POST /lessons/:lesson_id/quiz:submit`
- 用途:提交节末小测,触发节通过判定
- Request:`{ quiz_id, answers:[{question_id, user_answer, duration_ms}] }`
- 副作用:批量调 `fn_submit_answer` (context='lesson_quiz') + 调 `fn_lesson_pass(user, lesson, score)`;
- 响应:`{ score, passed, attempts, best_score, next_lesson_id, wrong_questions:[{q_id, correct_answer, explanation}] }`
- 错误:`COURSE_QUIZ_INCOMPLETE_ANSWERS` 400 / `COURSE_QUIZ_EXPIRED` 410

## OP-course-app-011 · `GET /srs/queue`
- 用途:取今日 SRS 队列
- Query:`?limit=20&track=hsk`
- 响应:`{ items:[{kp_id, kp_type, due_at, last_q_type}], remaining_today: 35 }`
- 算法:`SELECT * FROM course_user_srs WHERE user_id=auth.uid() AND due_at<=now() [AND kp.primary_track=$1] ORDER BY box, due_at LIMIT min($limit, remaining_today)`
- 错误:`COURSE_SRS_DAILY_LIMIT_EXCEEDED` 429(remaining_today=0)

## OP-course-app-012 · `GET /me/wrong-questions`
- 用途:错题本(按 KP 聚合)
- Query:`?track=&kp_type=&page=1&page_size=20&sort=wrong_count:desc|last_wrong:desc`
- 响应:`{ items:[{kp_id, kp_title_zh, wrong_count, last_wrong_at, has_recent_correct}], pagination }`
- 算法:基于 `course_user_answers` + `course_user_srs` LEFT JOIN 聚合;实时(不走 mv)
- 副作用:无;仅只读

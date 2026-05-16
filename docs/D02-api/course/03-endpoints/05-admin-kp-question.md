<!-- TARGET-PATH: docs/D02-api/course/03-endpoints/05-admin-kp-question.md -->

# 03-5 · 管理端 · KP / 题目 CRUD (OP-A5..A14)

## OP-course-admin-005 · `GET /kps`
- 角色:readonly+
- Query:`?track=&stage_id=&kp_type=&is_published=&q=&page=&page_size=&sort=`
- 响应:`{ items:[{kp_id, kp_code, kp_type, title_zh, is_published, version, linked_lesson_count, q_count}], pagination }`

## OP-course-admin-006 · `GET /kps/:id`
- 响应:`{ kp, linked_lessons:[{lesson_id, code, title_zh}], questions_brief:[{id, q_type}], version_history:[{version, updated_at, updated_by}] }`

## OP-course-admin-007 · `POST /kps`
- 角色:content_admin+
- Request:`{ kp_type, primary_track, title_zh, pinyin?, difficulty?, hsk_level?, content, translations?, tags? }`
- 副作用:INSERT;`kp_code` 由触发器生成;
- 响应:`{ kp_id, kp_code, version:1 }`
- 错误:`COURSE_KP_CONTENT_SCHEMA_MISMATCH` 400 / `COURSE_INVALID_KP_TYPE` 400

## OP-course-admin-008 · `PATCH /kps/:id`
- Header:`If-Match: <updated_at>` 必填
- Request:仅差异字段
- 副作用:若 content 变 → `version += 1`(触发器);
- 响应:`{ version }`
- 错误:`COURSE_STALE_VERSION` 409 / `COURSE_FIELD_IMMUTABLE` 400(改 kp_code/track)

## OP-course-admin-009 · `DELETE /kps/:id`
- 软删
- 引用检查:存在 `course_lesson_kp` / `course_questions(kp_id=...)` → 409 `COURSE_KP_STILL_REFERENCED`(`force=true` 时级联软删题目)
- 响应:`{ soft_deleted: true, cascade_questions: 12 }`

## OP-course-admin-010 · `GET /questions`
- Query:`?kp_id=&q_type=&is_published=&exam_scope=&difficulty=&q=&report_count_gte=&page=&sort=`

## OP-course-admin-011 · `GET /questions/:id`
- 响应:`{ q, payload, explanation, accuracy:{total, correct, rate}, version_history }`(accuracy 走 `course_user_answers` 聚合,7 天 cache)

## OP-course-admin-012 · `PATCH /questions/:id`
- If-Match 必填
- 副作用:payload 变 → `version += 1`;旧 attempt 不追溯改分(BR-RP04)
- 错误:`COURSE_STALE_VERSION` 409 / `COURSE_PAYLOAD_SCHEMA_MISMATCH` 400

## OP-course-admin-013 · `POST /questions`
- Request:`{ kp_id, q_type, exam_scope[], difficulty?, payload, audio_url?, image_url? }`
- 副作用:`payload_hash` 由后端计算 → `(kp_id, q_type, payload_hash)` 唯一冲突 → 409 `COURSE_IMPORT_DUPLICATE`(题级)
- 响应:`{ q_id, q_code, version:1 }`

## OP-course-admin-014 · `DELETE /questions/:id`
- 软删
- 流水保留:不影响 `course_user_answers`(FK RESTRICT 不 cascade,软删字段不影响 FK 实体)
- 注意:若 `course_user_exam_attempts.snapshot.q_ids` 包含该 id,允许软删但 attempt 内题仍可看;新 attempt 不再抽到。

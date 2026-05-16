<!-- TARGET-PATH: docs/D02-api/course/admin/03-endpoints/08-admin-media-exam.md -->

# 03-8 · 管理端 · 媒资 / 考试中心 (OP-A20..A22)

## OP-course-admin-020 · `/media`
- `POST /media` (multipart) → hash 计算 → 命中 `course_media_assets.hash` UNIQUE → 返已有 `{id, url, duplicate:true}`;否则上传 CDN + INSERT
- `GET /media` query `?kind=&source=&q=&page=`
- `DELETE /media/:id` 仅 super:反查 `ref_kp_id / ref_q_id` 引用 → 409 `COURSE_MEDIA_STILL_REFERENCED`;无引用 → 入待清队列(7 天后 cron 物理删)
- Request `POST`:form `{ file, kind, source, voice_profile?, ref_kp_id?, ref_q_id? }`

## OP-course-admin-021 · `/exams[/:id]`
- 方法:CRUD
- Request `POST`:`{ scope_type, scope_ref_id, title_zh, title_i18n?, pass_score?, total_score?, time_limit_minutes?, blueprint }`
- 唯一约束:同 (scope_type, scope_ref_id) 已有未删 exam → 409 `COURSE_IMPORT_DUPLICATE`(exam 级,hsk_mock 除外)
- `PATCH` If-Match 必填
- `DELETE`:存在 `state='in_progress'` 的 attempt → 409 `COURSE_EXAM_HAS_ACTIVE_ATTEMPTS`

## OP-course-admin-022 · `POST /exams/:id:preview`
- 用途:试抽题(管理员预览,不写 attempt)
- 副作用:无;仅按 blueprint 抽题渲染
- 响应:`{ questions:[...], effective_count, blueprint_evaluated }`
- 错误:`COURSE_EXAM_EFFECTIVE_QUESTION_EMPTY` 409

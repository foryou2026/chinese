<!-- TARGET-PATH: docs/D02-api/course/03-endpoints/10-internal.md -->

# 03-10 · 内部接口 (OP-I1..I3)

> Prefix:`/internal/v1/course`。鉴权 `X-Internal-Token`(env `CRON_TOKEN`)。无 RLS(`service_role`)。

## OP-course-internal-001 · `GET /health`
- 公开(用于探针),无需 token
- 响应:`{ ok:true, version, db:'reachable', mv_lag_s: 32 }`

## OP-course-internal-002 · `POST /exam-attempts:expire`
- 调用:cron 每分钟 (`scripts/cron/expire-exam-attempts.ts`)
- 副作用:
  ```sql
  UPDATE course_user_exam_attempts
     SET state='expired', finished_at=now()
   WHERE state='in_progress' AND expires_at < now()
   RETURNING id, user_id;
  ```
- 响应:`{ expired_count }`
- 评分:expire 不主动算分,学员下次查看 attempt 详情时按 snapshot 补算 + UPDATE score/passed

## OP-course-internal-003 · `POST /media:purge-pending`
- 调用:cron 每天 02:00
- 副作用:
  - DELETE `course_media_assets WHERE pending_purge_at < now() - interval '7 days'`(假设新增 `pending_purge_at` 字段;若 F1 未建则改为 join 标记表 — 本期通过 `course_content_action_log(action='archive', target_type='media')` 时间戳判定);
  - 同时清 CDN 对应 object;
- 响应:`{ purged_count }`

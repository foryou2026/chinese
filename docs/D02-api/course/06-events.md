<!-- TARGET-PATH: docs/D02-api/course/06-events.md -->

# 06 · 事件 / 频道 / cron · course

## 6.1 pg_notify 频道

| Channel | 触发 | Payload | 消费者 |
|---------|------|---------|--------|
| `course_import_status` | `course_import_batches` UPDATE status | `{batch_id, status, summary?}` | 管理端 SSE / WebSocket 订阅(本期可由前端轮询替代,频道为未来扩展)|

## 6.2 cron 任务

| Job | 频率 | 入口 | 调用 endpoint | 作用 |
|-----|------|------|---------------|------|
| 考试超期标记 | 每分钟 | `system/scripts/cron/expire-exam-attempts.ts` | `POST /internal/v1/course/exam-attempts:expire` | UPDATE `state='expired'` |
| 内容物理清理 | 每天 00:30 | `system/scripts/cron/purge-soft-deleted-course.ts` | 直接 SQL | DELETE `WHERE deleted_at < now() - interval '30 days'` for kp/question/lesson/chapter/exam |
| 媒资 CDN 清理 | 每天 02:00 | `system/scripts/cron/purge-pending-media.ts` | `POST /internal/v1/course/media:purge-pending` | 7 天保留窗后物理删 |
| MV `mv_course_user_daily` 刷新 | 每 5 分钟 | postgres native cron(pg_cron 或 supabase scheduled function) | `REFRESH MATERIALIZED VIEW CONCURRENTLY` | C 端今日统计 |
| MV `mv_course_track_stats` 刷新 | 每 10 分钟 | 同上 | 同上 | 后台总览 |
| 分区维护 | 每天 02:00 | `pg_partman.run_maintenance_proc()` | 直接 SQL | 预创 3 个月分区 |

## 6.3 异步任务(应用层 queue)

| Task | 触发 | 处理 |
|------|------|------|
| TTS 异步生成 | `POST /api/v1/course/kps/:id/audio` 未命中缓存时 | 入 queue → mock TTS adapter → 完成后 UPDATE `course_knowledge_points.audio_url` + INSERT `course_media_assets`;前端轮询同接口 |
| 导入文件解析 | `POST /admin/v1/course/import-batches:preview` | 入 queue → worker 解析 + 行级校验 → UPDATE `course_import_batches.status` + `validation_errors` + pg_notify |
| 题目准确率聚合 | 7 天周期 | 后台任务,UPDATE 后台 cache(可选 P2)|

## 6.4 Webhook / 外部回调

- 本期无外部回调;
- 导入完成可考虑邮件 / IM 通知,留 P2(F2 决策);
- 支付 / 续费等外部 webhook 不在 course 域。

## 6.5 监控埋点

| 指标 | 上报 |
|------|------|
| `exam_attempts_expired_total` | counter,每次 cron 完成 |
| `course_answers_total{context_type}` | counter,每次 `fn_submit_answer` |
| `course_srs_due_pending` | gauge,5 分钟采样 |
| `mv_refresh_duration_seconds` | histogram |
| `import_batch_failed_total` | counter |

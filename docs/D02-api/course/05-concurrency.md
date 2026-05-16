<!-- TARGET-PATH: docs/D02-api/course/05-concurrency.md -->

# 05 · 并发与冲突处理 · course

| 场景 | 策略 | 实现 | 错误码 |
|------|------|------|--------|
| 管理端编辑 KP/Question/Lesson/Exam | 乐观锁 + 提示 | Header `If-Match: <updated_at>` → SQL `UPDATE ... WHERE updated_at=$1` rowcount=0 → 409 | `COURSE_STALE_VERSION` |
| 内容导入 | 幂等(payload_hash + import_type) | `idx_course_import_hash` UNIQUE-ish + EXISTS 检查;命中返已有批次 | — / 409 `COURSE_IMPORT_DUPLICATE` |
| 学员作答 | INSERT-only,无冲突 | 月分区表,append-only | — |
| 学员单题限流 | 600/分/UID | Redis token bucket | `COURSE_RATE_LIMIT` |
| 节末小测提交 | quiz_id 内存 TTL 10 分钟 | `quiz_id → {lesson_id, question_ids, expires_at}` 存 Redis | `COURSE_QUIZ_EXPIRED` |
| 考试提交 vs cron 超期 | 行锁串行 | `fn_submit_exam` 内 `SELECT ... FOR UPDATE`;后到者看到 `state='expired'` | `COURSE_EXAM_EXPIRED` |
| 考试放弃 vs cron 超期 | 行锁串行 | 同上 | `COURSE_EXAM_EXPIRED` |
| SRS 更新(并发答题) | UPSERT 原子 | `INSERT ... ON CONFLICT (user_id,kp_id) DO UPDATE SET box=..., due_at=..., correct_streak=..., wrong_count=...` | — |
| 课程目录调序 | 事务 + 全行锁 | `BEGIN; SELECT ... WHERE stage_id=$1 FOR UPDATE; UPDATE batch; COMMIT;` LWW | — |
| 节绑定 KP | 事务 DELETE+INSERT | `BEGIN; DELETE FROM course_lesson_kp WHERE lesson_id=$1; INSERT ...; COMMIT;` LWW | — |
| 发布/下架 | 事务 + 级联 + 日志一致 | 单事务内切 is_published + 级联 + INSERT action_log | `COURSE_CASCADE_TARGET_EMPTY` |
| 媒资上传(并发同 hash) | UNIQUE 自然去重 | `INSERT ... ON CONFLICT (hash) DO NOTHING RETURNING id` → 后查 | — |
| 举报 24h 去重 | EXISTS 检查 + RPC 内联事务 | `fn_report_question` 起 advisory lock(user_id, question_id) 串行化 | `COURSE_REPORT_DUPLICATE` |
| 学员选主题 | LWW | `UPDATE auth_user_profiles SET current_track=$1` | — |
| Idempotency-Key | 写入 24h 缓存 | Redis key = `idemp:<endpoint>:<key>:<uid>` → 命中返同响应 | — |

## RLS 与并发

- RLS policy 嵌入查询计划,锁粒度与一般 SQL 等同,无额外开销;
- service_role 路径不走 RLS,中间件强制叠加 `tracks_scope`,SQL 层 `WHERE primary_track = ANY($tracks_scope)`。

## 行锁热点

- `course_user_srs (user_id, kp_id)`:UPSERT 原子,KP 维度热点低;
- `course_user_progress (user_id, lesson_id)`:同上;
- `course_questions (id)`:`report_count += 1` 时短时行锁,可接受(报告频率低)。

## 死锁防范

- 多表事务按固定顺序 `tracks → stages → chapters → lessons → kp → questions`;
- 调序事务先 `ORDER BY id FOR UPDATE` 一次性锁所有目标行;
- 发布级联事务获取顺序:父表 → 子表(自上而下);避免逆向。

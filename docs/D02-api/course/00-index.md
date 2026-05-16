<!-- TARGET-PATH: docs/D02-api/course/00-index.md -->

# D02 · 接口规范索引 · course

> **阶段**:D02-L · **feature**:`course` · **状态**:已冻结 · 2026-05-16
> **上游**:[D01 数据](../../D01-data/course/00-index.md) · F2 课程接口规范 · [C05 PRD](../../C05-prd/course/PRD.md)
> **下游**:D03 校验

## 子文件导航

| 文件 | 内容 |
|------|------|
| [01-routes-delta.md](./01-routes-delta.md) | 与 discover-china 路由增量与命名约定 |
| [02-overview.md](./02-overview.md) | 鉴权 / 限流 / 分页 / 错误信封 |
| [03-endpoints/01-app-map-lesson.md](./03-endpoints/01-app-map-lesson.md) | 学员端 OP-C1..C8 (学习地图 / 节学习 / TTS / 断点 / 节末小测)|
| [03-endpoints/02-app-answer-srs.md](./03-endpoints/02-app-answer-srs.md) | 学员端 OP-C9..C12 (作答 / SRS / 错题本)|
| [03-endpoints/03-app-exam-report-stats.md](./03-endpoints/03-app-exam-report-stats.md) | 学员端 OP-C13..C19 (考试 / 举报 / 个人统计)|
| [03-endpoints/04-admin-catalog.md](./03-endpoints/04-admin-catalog.md) | 管理端 OP-A1..A4 (主题/阶段/章/节 CRUD)|
| [03-endpoints/05-admin-kp-question.md](./03-endpoints/05-admin-kp-question.md) | 管理端 OP-A5..A14 (KP/题目 CRUD)|
| [03-endpoints/06-admin-import.md](./03-endpoints/06-admin-import.md) | 管理端 OP-A15 (内容导入)|
| [03-endpoints/07-admin-publish-report-log.md](./03-endpoints/07-admin-publish-report-log.md) | 管理端 OP-A16..A19 (发布/下架/操作日志/举报处理)|
| [03-endpoints/08-admin-media-exam.md](./03-endpoints/08-admin-media-exam.md) | 管理端 OP-A20..A22 (媒资 / 考试中心)|
| [03-endpoints/09-admin-search-stats.md](./03-endpoints/09-admin-search-stats.md) | 管理端 OP-A23..A24 (全局搜索 / 统计大屏)|
| [03-endpoints/10-internal.md](./03-endpoints/10-internal.md) | 内部 OP-I1..I3 (健康 / 超期 / 媒资清理)|
| [04-error-codes.md](./04-error-codes.md) | ~55 个 `COURSE_*` 错误码 |
| [05-concurrency.md](./05-concurrency.md) | 乐观锁 / 行锁 / UPSERT / 幂等 |
| [06-events.md](./06-events.md) | pg_notify 频道 + cron 调用面 |
| [99-open-questions.md](./99-open-questions.md) | (已清空)|

## 全局约定速览

- **学员端 prefix**:`/api/v1/course`
- **管理端 prefix**:`/admin/v1/course`
- **内部 prefix**:`/internal/v1/course`
- **鉴权**:
  - C 端:`Authorization: Bearer <jwt>`,所有 `/api/v1` 走 Supabase Auth(`auth.uid()` 透传 RLS);
  - 管理端:`Authorization: Bearer <jwt>` + 中间件校验 `admin_role + tracks_scope`;实际 DB 操作走 `service_role`;
  - 内部:`X-Internal-Token: <env CRON_TOKEN>`;
- **响应信封**:成功 `{ ok:true, data:... }`;失败 `{ ok:false, error:{ code, message, details? } }`;
- **限流**:
  - 默认 120/分/IP+UID;
  - `POST /answers` 600/分;
  - `POST /kps/:id/audio` 20/分;
  - `GET /admin/search` 30/分;
- **分页**:`?page=&page_size=&sort=` 或 `?cursor=&limit=`(高基数列表用 cursor);
- **乐观锁**:管理端 PATCH 要求 `If-Match: <updated_at ISO8601>`;不一致返 409 `COURSE_STALE_VERSION`;
- **幂等**:写入类 RPC 接 `Idempotency-Key` header(可选);相同 key 24h 内重放返同结果。

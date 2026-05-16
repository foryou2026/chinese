<!-- TARGET-PATH: docs/D01-data/app-auth/07-volume-growth.md -->

# `app-auth` · 量级预估

> v1 上线 12 个月预估（保守口径）：

| 表 | 行数预估 | 增长速率 | 影响 |
|----|---------|---------|------|
| `auth.users` | 50k - 200k | ~500 / day | 极小，全表 < 100MB |
| `profiles` | 同 auth.users | 同 | 极小 |
| `user_sessions` | 最大 = users × 3 = 600k | 起伏明显 | 中；refresh 续期可能日变动 100k+ |
| `auth_login_attempts` | 90d 滚动窗口约 200k - 500k | ~3-5k / day | 中；索引读写较频繁 |
| `audit_logs` | 1 - 5M（按 v1 估）| ~30k / day | 大；需要分区策略（v2）|

## 性能关注点

1. `auth_login_attempts` 锁定计数查询走复合索引，p95 应 < 5ms；
2. `user_sessions` 写入"踢最早"用 `SELECT ... ORDER BY created_at LIMIT 1 FOR UPDATE SKIP LOCKED` 防止并发踢错；
3. `audit_logs` 写入异步（fire-and-forget），不阻塞 API 返回。

## v2 规划

- `audit_logs` 按月分区；
- `auth_login_attempts` 改为 90 天分区表（pg_partman）；
- 启用 PgBouncer transaction mode（已规划在 `B01-architecture/06-deploy-env.md`）。

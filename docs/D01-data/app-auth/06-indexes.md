<!-- TARGET-PATH: docs/D01-data/app-auth/06-indexes.md -->

# `app-auth` · 关键索引依赖

> 全部索引已在 [`B02-permissions/04-data-model.md`](../../B02-permissions/04-data-model.md) 创建；本节列出本 feature 强依赖的索引，禁止 admin DBA 在不通知本 feature 维护者的情况下删除。

| 表 | 索引 | 用途 |
|----|------|------|
| `auth_login_attempts` | `(email, ip, created_at desc)` 复合 | 5/15min 锁定计数 |
| `auth_login_attempts` | `(created_at)` | pg_cron 清理 90 天前数据 |
| `user_sessions` | `(user_id, created_at)` | 找最早 session 踢之 |
| `user_sessions` | `(refresh_token_hash)` 唯一 | session-status 校验 |
| `profiles` | `(role)` partial WHERE role<>'user' | admin-users 列表（用得少）|
| `profiles` | PK `(id)` | 跨 feature 默认连接 |
| `audit_logs` | `(actor_id, created_at desc)` | admin 看用户行为时间线 |
| `audit_logs` | `(action, created_at desc)` | 按行为类型聚合分析 |

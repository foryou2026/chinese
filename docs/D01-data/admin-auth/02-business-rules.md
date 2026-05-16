<!-- TARGET-PATH: docs/D01-data/admin-auth/02-business-rules.md -->

# D01 · 业务规则 · `admin-auth`

> 大部分复用 [`D01-data/app-auth/03-business-rules.md`](../app-auth/03-business-rules.md);本文仅列 admin 特化的 D-BR。

| D-BR | 规则 | 落地 |
|------|------|------|
| D-BR-admin-01 | profiles.role 终生只读 (运行时不允许产品代码 update);仅 seed 脚本或运维 SQL 可改 | DB 触发器 [`migrations/0003_handle_new_user_trigger.sql`](../../../system/supabase/migrations/0003_handle_new_user_trigger.sql) 内已校验 |
| D-BR-admin-02 | super_admin 不允许自助删除自己的 auth.users 行;`POST /admin/v1/auth/account/delete` v1 不存在 | (无 endpoint) |
| D-BR-admin-03 | user_sessions 按 (user_id, surface) 复合分桶计数 3 | D02-03 session-register §逻辑 |
| D-BR-admin-04 | audit_logs.actor_role 永远从服务端 JWT 派生;严禁前端传入 | D02 各 endpoint 写入处 |
| D-BR-admin-05 | profiles.is_disabled=true → admin login 30s LRU 缓存命中即拒登 | D02-03 login-attempt-record |
| D-BR-admin-06 | seed 脚本必须设 `email_confirmed_at=now()` + `raw_app_metadata->>role='super_admin'` 两项;缺一则脚本报错 | [`seed.sql`](../../../system/supabase/seed.sql) |

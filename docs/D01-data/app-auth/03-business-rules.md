<!-- TARGET-PATH: docs/D01-data/app-auth/03-business-rules.md -->

# `app-auth` · 数据业务规则

| ID | 规则 | 落地位置 |
|----|------|---------|
| D-BR-01 | `profiles.role` 默认 'user'，仅由 Hook / seed 写；API 层任何 PATCH 必须 zod whitelist 排除 role | API 中间件 + zod schema |
| D-BR-02 | `profiles.is_disabled = true` 后 30s 内必须使本用户全部 API 401 | disabledCache LRU TTL 30s |
| D-BR-03 | `user_sessions` 每 user 最多 3 行；INSERT 后 trigger 或 API 内 transaction 删最早 | API `/auth/session-register` transaction |
| D-BR-04 | `auth_login_attempts` 保留 90 天 | pg_cron `delete_old_login_attempts` |
| D-BR-05 | `auth_login_attempts` succeeded=true 写入后**不触发**锁定计算（只用失败次数）| API `/auth/login-attempt-record` |
| D-BR-06 | OAuth 注册触发 Hook 时若 `provider_id` 已被另一 email 占用 → 拒绝（避免账号合并）| `/internal/auth-hook` 校验 |
| D-BR-07 | `profiles.locale` 必须在枚举 `['zh','en','vi','th','id']` 内 | DB CHECK 约束 + zod |
| D-BR-08 | 密码改动后 `auth.users.encrypted_password` 由 GoTrue 写；不允许 SQL 直接 UPDATE | 仅 admin.updateUserById 写 |

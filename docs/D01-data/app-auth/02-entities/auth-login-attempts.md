<!-- TARGET-PATH: docs/D01-data/app-auth/02-entities/auth-login-attempts.md -->

# Entity · `public.auth_login_attempts`

- 完整 DDL：[`B02-permissions/04-data-model §2.3`](../../../B02-permissions/04-data-model.md)。
- 用途：错密锁定（5/15min）+ 审计登录失败原因。
- 写入：
  - `POST /v1/auth/login-attempt-record` 在每次 signIn 前后 INSERT 一行（succeeded + reason）。
- 读取：
  - 同上接口在 INSERT 前先 `SELECT count(*) WHERE email=? AND ip=? AND succeeded=false AND created_at > now()-'15min'`；
  - admin-users 看用户登录历史（admin-users feature，v2）。
- 保留：90 天自动清理（pg_cron job 在 `B01-architecture/03-database.md` 维护）。
- 索引：复合 `(email, ip, created_at desc)`（已在 B02-04 创建）。

<!-- TARGET-PATH: docs/D02-api/admin-auth/05-concurrency.md -->

# D02 · 并发约束 · `admin-auth`

| C-ID | 场景 | 约束 |
|------|------|------|
| C-admin-1 | 同一 admin 同时在 2 个浏览器登录 | `session-register` `SELECT ... FOR UPDATE SKIP LOCKED`,串行化;两次都返成功但其中一个可能因 3 设备上限被踢另一个早会话 |
| C-admin-2 | 改密与新登录并发 | 改密后 revoke `surface='admin' AND session_id != current`;新登录的 session 视写库先后:若改密事务在新登录之前提交,新会话视新密码;否则新会话用旧密成功 → 紧接被改密事务 revoke |
| C-admin-3 | 全局退出与新登录并发 | logout-global 删全部 sessions;新登录的事务后提交 → 新 session 留存;前端轮询 session-status 不会 false-positive |
| C-admin-4 | 同邮箱 5 次错密同时发生 | login-attempt-record `INSERT` + 计数 SELECT 在同一事务;Postgres 默认隔离 (RC) 下计数可能 race,允许 ±1 的容错;锁定边界由前端 retryAfter 兜底 |
| C-admin-5 | seed 脚本与登录并发 | seed 期间运维通常停服;若不停服,UPSERT 后立即生效;并发登录请求若拿到旧 jwt 也能继续工作 (jwt 已签,不重验) |

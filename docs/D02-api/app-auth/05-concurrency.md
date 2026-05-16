<!-- TARGET-PATH: docs/D02-api/app-auth/05-concurrency.md -->

# `app-auth` · 并发约束

## C-1 · `session-register` 踢最早

- 多设备并发登录可能同时进入 INSERT；
- 用 **单事务 + `FOR UPDATE SKIP LOCKED`** 保证踢出唯一最早行；
- 防止"3+1+1 同时进 → 留下 2 行"的竞态。

```sql
SELECT id FROM user_sessions
WHERE user_id = $user_id
ORDER BY created_at FOR UPDATE SKIP LOCKED
OFFSET 3;
DELETE FROM user_sessions WHERE id = ANY($ids);
```

## C-2 · `me/password` 改密 + 踢

- 改密期间若同账号其他设备同时调 refresh，可能在踢动作执行前抢一拍 refresh 成功；
- 容忍：踢动作 100% 完成后那台设备的下次刷新一定失败；上限延迟 = refresh 间隔（最长 access TTL = 1h）；
- 加强：可在改密 transaction 内同时 INSERT `user_sessions` 一行"哨兵"用 RETURN，但 v1 不做。

## C-3 · `login-attempt-record` phase=after 写入

- 高并发下 `INSERT auth_login_attempts` 可能 spike；
- 走专用连接池 + 异步写（非阻塞业务）；
- 写失败不影响登录主流程（最多锁定算少了几次，可接受）。

## C-4 · `forgot-password-throttle`

- email 维度 60s 用 Redis `SET key NX EX 60` 简单实现；
- IP 维度 1h 5 次用 sliding window；
- 两条规则任一命中即拒。

## C-5 · cookie/set 并发

- 同一浏览器多 tab 同时刷新 → cookieStorage Adapter 都会写；
- HttpOnly cookie 写覆盖语义 = 最后一次为准，不破坏；
- access token 重复无危害（同样的 user_id）。

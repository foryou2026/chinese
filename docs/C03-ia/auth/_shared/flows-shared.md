<!-- TARGET-PATH: docs/C03-ia/auth/_shared/flows-shared.md -->

# auth · `_shared/flows-shared.md` · 跨端共享流程不变式

> **作用**：列出 auth feature 中**所有 surface 必须遵守**的流程不变式；端独有的流程见各自 `app/02-flows.md` / `admin/02-flows.md`。
> **冻结**：2026-05-17（批次 16 多端合并）

---

## 1. 共享流程一览

| 流程 ID | 名称 | 适用端 |
|--------|------|--------|
| `FL-auth-shared-01` | 登入成功 → 颁发 session + 注册设备 | app + admin |
| `FL-auth-shared-02` | 登出 → 撤销 session + 清 cookie | app + admin |
| `FL-auth-shared-03` | 密码修改 → 可选「踢全部其它设备」 | app + admin |
| `FL-auth-shared-04` | 忘记密码 → 邮件链接 → 重置 → 自动登入 + 踢其它设备 | app + admin |

> 端独有的流程（注册 / OAuth / 邮箱验证 / profile 编辑等）：`FL-auth-app-NN` 在 [`app/02-flows.md`](../app/02-flows.md)；admin seed 通过运维脚本，不进 C02。

---

## 2. `FL-auth-shared-01` 登入成功

1. POST `/api/<surface>/auth/login` body `{email, password, captcha?}`，header `X-CSRF-Token`
2. 服务端：`signInWithPassword` → 拿到 supabase session
3. **admin 端额外**：查 `profiles.role`；非 `super_admin` 立即 `signOut` + 返回 `AUTH_USE_USER_ENTRY`
4. 查 `user_sessions where user_id=? and surface=? and revoked_at is null`：≥ 3 → 撤销最旧
5. INSERT `user_sessions(...)`，写 cookie，返回 `{me, devices}`

## 3. `FL-auth-shared-02` 登出

| 子流程 | 入口 | 行为 |
|--------|------|------|
| 本设备退出 | POST `/api/<surface>/auth/logout` | revoke 当前 session + 清当前 surface cookie |
| 全部设备退出 | POST `/api/<surface>/auth/logout?scope=global` | revoke `user_id+surface` 全部 session + 清当前 cookie；**不**影响另一端 |

## 4. `FL-auth-shared-03` 密码修改（已登录态）

1. POST `/api/<surface>/me/password` body `{old, new, revokeOthers: bool}`
2. 服务端：`signInWithPassword` 复核旧密 → 失败即 `INVALID_OLD_PASSWORD`
3. `updateUser({password: new})`
4. `revokeOthers=true` → revoke 同端其余 session（不影响另一端）

## 5. `FL-auth-shared-04` 忘记密码

1. POST `/api/<surface>/auth/forgot-password` body `{email}` → 节流 60s/IP + 3 次/h
2. 服务端响应固定 `{ok: true}`（不暴露邮箱是否存在）
3. 邮件包含 `?token=...&surface=<app|admin>` 一次性链接（15min TTL）
4. GET `<surface>/auth/reset-password?token=...` → 校验 → 设新密
5. 成功 → 自动 `signInWithPassword(new)` + revoke `user_id+surface` 其它 session

---

## 99. 上游引用

- [C02-permissions/02-authz-mechanism.md](../../../C02-permissions/02-authz-mechanism.md)
- [C02-permissions/02-authz-mechanism.md](../../../C02-permissions/02-authz-mechanism.md)
- [_shared/state-machines.md](./state-machines.md)
- [C01-requirements/auth/baseline.md](../../../C01-requirements/auth/baseline.md) R-auth-003 / 005 / 007 / 008 / 009

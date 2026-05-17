<!-- TARGET-PATH: docs/C02-ia-interaction/auth/02-flows.md -->

# 业务流程

> **阶段**：C02-IN · **功能**：`auth`
> **冻结状态**：已冻结 · 2026-05-16

---

## 一、跨端共享流程（FL-auth-shared-NN）

以下流程不变式在 app 与 admin 两端均适用。

| 流程 ID | 名称 | 适用端 |
|--------|------|--------|
| FL-auth-shared-01 | 登入成功 → 颁发 session + 注册设备 | app + admin |
| FL-auth-shared-02 | 登出 → 撤销 session + 清 cookie | app + admin |
| FL-auth-shared-03 | 密码修改 → 可选「踢全部其它设备」 | app + admin |
| FL-auth-shared-04 | 忘记密码 → 邮件链接 → 重置 → 自动登入 + 踢其它设备 | app + admin |

### FL-auth-shared-01 · 登入成功

1. POST `/api/<surface>/auth/login` body `{email, password, captcha?}`，header `X-CSRF-Token`
2. 服务端：登录 → 拿到会话
3. **admin 端额外**：查 `用户角色字段`；非 `admin` 立即登出 + 返回 `AUTH_USE_USER_ENTRY`
4. 查 `会话记录` where user_id=? and surface=? and revoked_at is null：≥ 3 → 撤销最旧
5. INSERT `会话记录(...)`，写 cookie，返回 `{me, devices}`

### FL-auth-shared-02 · 登出

| 子流程 | 入口 | 行为 |
|--------|------|------|
| 本设备退出 | POST `/api/<surface>/auth/logout` | revoke 当前 session + 清当前 surface cookie |
| 全部设备退出 | POST `/api/<surface>/auth/logout?scope=global` | revoke `user_id+surface` 全部 session + 清当前 cookie；不影响另一端 |

### FL-auth-shared-03 · 密码修改（已登录态）

1. POST `/api/<surface>/me/password` body `{old, new, revokeOthers: bool}`
2. 服务端登录复核旧密 → 失败即 `INVALID_OLD_PASSWORD`
3. `更新用户资料`
4. `revokeOthers=true` → revoke 同端其余 session（不影响另一端）

### FL-auth-shared-04 · 忘记密码

1. POST `/api/<surface>/auth/forgot-password` body `{email}` → 节流 60s/IP + 3 次/h
2. 服务端响应固定 `{ok: true}`（不暴露邮箱是否存在）
3. 邮件包含 `?token=...&surface=<app|admin>` 一次性链接（15min TTL）
4. GET `<surface>/auth/reset-password?token=...` → 校验 → 设新密
5. 成功 → 自动登录 + revoke `user_id+surface` 其它 session

---

## 二、app 端流程（FL-auth-app-NN）

### 主流程

| Flow ID | 名称 | 类型 |
|---------|------|------|
| FL-auth-app-01 | 邮箱注册主流程 | main |
| FL-auth-app-02 | 登录主流程（密码 / 节流 / 禁用 / 角色错位）| main |
| FL-auth-app-03 | 个人中心 - 修改资料 | main |
| FL-auth-app-04 | 修改密码 + 退出登录 | main |

### 异常流程

| Flow ID | 名称 |
|---------|------|
| FL-auth-app-05 | 错密 5/15min 锁定 |
| FL-auth-app-06 | 第 4 设备登录被踢 |
| FL-auth-app-07 | 账号被禁用 |
| FL-auth-app-08 | OAuth 失败 / 取消 / 角色错位 |
| FL-auth-app-09 | 邮件 / 重置链接过期 |
| FL-auth-app-10 | 网络断 / 5xx |
| FL-auth-app-11 | 守卫拦截未登录 |

---

## 三、admin 端流程（FL-auth-admin-NN）

### 主流程

| Flow-ID | 标题 |
|---------|------|
| FL-auth-admin-01 | 邮密登录 |
| FL-auth-admin-02 | 忘密 → 重置 |
| FL-auth-admin-03 | 改密 |
| FL-auth-admin-04 | 退出 |

### 异常流程

| Flow-ID | 标题 |
|---------|------|
| FL-auth-admin-05 | 非 admin 登录拦截 |
| FL-auth-admin-06 | 锁定 |
| FL-auth-admin-07 | 禁用账号 |
| FL-auth-admin-08 | 第 4 设备踢最早 |
| FL-auth-admin-09 | 重置链接过期 |
| FL-auth-admin-10 | 守卫拦截 + redirect |
| FL-auth-admin-11 | 5xx 兜底 |

<!-- TARGET-PATH: docs/C02-ia-interaction/auth/03-state-machines.md -->

# 状态机

> **阶段**：C02-IN · **功能**：`auth`
> **冻结状态**：已冻结 · 2026-05-16

---

## 一、跨端共享状态机（SM-auth-shared-NN）

### SM-auth-shared-01 · session 生命周期

```text
[anonymous] --login_ok--> [active]
[active] --idle≥30min--> [expiring] --refresh_ok--> [active]
[active] --idle≥7d--> [expired]
[active] --explicit_logout--> [revoked]
[active] --global_logout--> [revoked × N]
[active] --kicked_by_4th_device--> [revoked]
[active] --disable_account--> [revoked × all_user]
```

- cookie：`access_token`（30min jwt）+ `refresh_token`（7d，rotation）
- 存储：`HttpOnly; Secure; SameSite=Lax; Path=/`
- 服务端登记：`会话记录(id, user_id, surface, device_label, created_at, last_seen_at, revoked_at)`
- 跨端不共享 cookie name（app 用 `sb-access`、admin 用 `sb-admin-access`）

### SM-auth-shared-02 · CSRF 双提交

```text
[anonymous] --GET /any--> [issued]
[issued] --POST with X-CSRF-Token header--> [valid] | [rejected]
[rejected] --new GET--> [issued]
```

- header 必须与 cookie `csrf` 值字节级相等
- 仅状态变更接口（POST/PUT/PATCH/DELETE）校验
- OAuth callback / 鉴权后端回调走签名校验，不走 CSRF

### SM-auth-shared-03 · 设备名册（按端独立计数）

```text
device_count(user_id, surface) ≤ 3
```

- 第 4 台登入 → 找 `last_seen_at` 最早一台 revoke → 写入新 session
- 被踢端下次心跳 → 进入 `[revoked]` → 客户端清 cookie 跳登录页（payload `kicked_at_<ts>`）

### SM-auth-shared-04 · 锁定 / 禁用

```text
失败次数(user_id, ip, 15min窗口) ≥ 5 --> [locked 15min]
[locked] --15min超时--> [normal]
profiles.启用态 = false --> [globally revoked]
[globally revoked] --管理员置 启用态=true--> [normal]
```

- 计数表：`auth_failed_attempts(user_id, ip, ts)`，TTL 60min
- 锁定不区分 surface：admin 错锁也连带 app 端

---

## 二、app 端状态机（SM-auth-app-NN）

### SM-auth-app-01 · 通用提交按钮（注册 / 登录 / 忘密 / 重置 / 改资料 / 改密）

| 状态 | 按钮 | 输入 | UI 反馈 |
|------|------|------|---------|
| idle | 可点 / 校验通过才高亮 | 可写 | — |
| submitting | loading + disabled | readonly | 自身 spinner |
| idle_error | 可点 | 可写 | 字段下内联红字（4xx）或顶部 Toast（5xx） |
| done | — | — | Toast 或跳转 |

### SM-auth-app-02 · 重发验证邮件 / 忘密发送按钮

> 文案：`重新发送 (NNs)`，倒计时实时刷新；按钮 disabled 期间禁止点击。

### SM-auth-app-03 · 用户会话（前端鉴权 SDK + Cookie 存储适配）

- 转 `anon` 时统一动作：清 Cookie 存储适配 + clear Zustand authStore + 跳 `/auth/login?reason=<kicked|disabled|expired|signout>`
- `reason=signout` 不弹 Toast；其他 reason 在登录页根据 query 弹 Toast

### SM-auth-app-04 · 验证邮件 / 重置链接 token 校验

```text
[pending] --GET token--> [exchanging]
[exchanging] --valid--> [success]
[exchanging] --expired|invalid--> [token-invalid]
```

---

## 三、admin 端状态机（SM-auth-admin-NN）

| SM-ID | 标题 | 状态转移 | 应用范围 |
|-------|------|---------|---------|
| SM-auth-admin-01 | 通用提交（复用 SM-app-01 语义）| `idle → submitting → (success / error / locked / not-admin / token-invalid)` | 4 页全部表单 |
| SM-auth-admin-02 | 重发 / 找回 cooldown（复用 SM-app-02 语义）| `enabled → throttled(retryAfter) → enabled` | `/admin/auth/forgot` |
| SM-auth-admin-03 | admin 会话 | `signed-out → signed-in (admin) → (kicked / expired / disabled / signout)` | 全局；与 app 会话隔离（surface 维度） |

> admin 端无独立的 SM-04 token-exchange：reset 走与 app 同一份回调换会话，复用 SM-auth-app-04 语义，不重复定义。

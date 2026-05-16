<!-- TARGET-PATH: docs/B02-permissions/02-auth-flow.md -->

# 02 · 认证流程

> **阶段**：B02-P  
> **上游**：`B01-architecture/09-auth-infra.md`、`01-roles.md`  
> **下游**：`auth` / `auth` feature 的 C/D 阶段、所有 D02 L 中的 `/api/auth/*` 路由实现  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 后端 = 自托管 Supabase Auth（GoTrue v≥2.130）；前端 = `@supabase/supabase-js` v2 + **自定义 cookieStorage adapter**。
- access 1h / refresh 30d；HttpOnly Cookie + CSRF Double-Submit；不写 localStorage。
- 多设备硬上限 3，第 4 次踢最早；不暴露"我的设备"页。
- 禁用账号 → 撚销全部 refresh + 删 user_sessions + 全局登出。
- 不自动登出；不上 2FA；邮件本期 mock。

---

## 1. 登录

### 1.1 邮箱 + 密码（应用端 + 管理端）

```
1. /auth/login 提交 { email, password }
2. 前置：POST /api/auth/login-attempt-record { email, ip } —— 命中 5/15min 锁定立即返 429 AUTH_LOGIN_RATE_LIMITED
3. 前置：查 profiles where email=? 若 is_disabled=true → 401 AUTH_ACCOUNT_DISABLED
4. supabase.auth.signInWithPassword({ email, password })
5. 成功：
   - cookieStorage adapter 拦截 session，调 POST /api/auth/cookie/set
     → Hono 下发 zhiyu-at (HttpOnly 3600s) + zhiyu-rt (HttpOnly 2592000s) + zhiyu-csrf (非 HttpOnly 32B 随机)
   - Zustand authStore 写入 { id, email, role }
   - 调 POST /api/auth/session-register（详见 §4）
   - super_admin → /admin；user → ?redirect 或 /
6. 失败映射 → §AUTH_INVALID_CREDENTIALS / AUTH_EMAIL_NOT_VERIFIED / AUTH_ACCOUNT_DISABLED / AUTH_UNKNOWN
```

### 1.2 Google OAuth（仅应用端）

```
1. /auth/login 点 "Google 继续"
2. supabase.auth.signInWithOAuth({ provider:'google', options:{ redirectTo: '/auth/callback' } })
3. /auth/callback 调 exchangeCodeForSession(code) → 同 §1.1 step 5
4. 首次登录：Supabase Auth 自动创建 auth.users 行；GoTrue before_user_created hook 注入
   raw_app_meta_data = { role:'user', provider:'google' }；DB trigger 自动 insert profiles。
5. 失败：oauth_provider_error → AUTH_OAUTH_FAILED；用户拒绝 → 静默回 /auth/login。
```

### 1.3 管理端登录限制

- `/admin/auth/login` 仅展示邮箱密码（**不**展示 Google 按钮）；
- 登录成功后立即检查 `app_metadata.role`；不为 `super_admin` → 立即 `signOut` + Toast `AUTH_NOT_ADMIN`；
- **本期不上 TOTP / 2FA**。

---

## 2. Token 策略（与 [`B01-09 §2`](../B01-architecture/09-auth-infra.md) 一致）

| 项 | 值 |
|----|---|
| 类型 | JWT HS256，密钥 `SUPABASE_JWT_SECRET` |
| Access 有效期 | 3600s（1h）|
| Refresh 有效期 | 2592000s（30d 滚动；refresh 后旧 refresh 立即失效）|
| 存储 | **HttpOnly Cookie**：`zhiyu-at` + `zhiyu-rt`；都为 `HttpOnly; Secure; SameSite=Lax; Path=/` |
| Cookie 适配器 | supabase-js `auth.storage` 自定义实现，读写都走同域 `POST /api/auth/cookie/get|set|clear`（详见 [03-authz-mechanism §2.4](./03-authz-mechanism.md)）|
| 携带方式 | 同域请求浏览器自动携带；Hono 中间件优先从 `c.req.cookie('zhiyu-at')` 读，兼容 `Authorization: Bearer` Header（服务间调用）|
| CSRF | 同时下发非 HttpOnly `zhiyu-csrf` (32B 随机)；POST/PUT/PATCH/DELETE 必须在 `X-CSRF-Token` Header 回传一致 |
| 后端验签 | `jose.jwtVerify`，校 `exp` + `signature` + `profiles.is_disabled`（30s LRU 缓存）|
| 自动刷新 | supabase-js 在 access 到期前 60s 触发；连续失败 3 次 → 全局登出 |
| Token 黑名单 | 不做。撚销通过 Supabase Admin API revoke refresh 实现；access 自然过期内（最长 1h）仍有效，接受风险 |

JWT payload 关键字段：`sub` (user.id, UUID) / `email` / `app_metadata.role` / `app_metadata.provider` / `exp` / `iat`。

---

## 3. 登出

```
1. 用户点击「退出登录」
2. 前端 supabase.auth.signOut({ scope:'local' })
3. cookieStorage adapter 调 POST /api/auth/cookie/clear → Set-Cookie Max-Age=0 清三个 cookie
4. 同时 POST /api/auth/session-revoke { sessionId } 删除 user_sessions 行
5. authStore.reset(); 跳 /auth/login（或 /admin/auth/login）
6. signOut 失败：忽略，依然清本地 + 跳页
```

---

## 4. 会话管理（多设备 3 上限）

### 4.1 策略

- 不自动登出；refresh 未过期就保持。
- 同 `user_id` 最多 **3 个活跃会话**；第 4 次登录踢**最早创建**的会话。

### 4.2 实现

详细表结构 → [04-data-model §3](./04-data-model.md)。登录成功后：

```
POST /api/auth/session-register
  body: { device:'web'|'mobile-web', ua: navigator.userAgent }
  Cookie: zhiyu-at（自动）

后端：
1. authRequired 解 user_id
2. 通过 service_role 查 auth.refresh_tokens where user_id=?
3. 在 user_sessions 插入 { user_id, refresh_token_hash, device, ua, ip, created_at, last_seen_at }
4. count > 3 → 取 created_at 最早 oldest
   - supabase.auth.admin.signOut(oldest.refresh_token)  ← revoke
   - delete from user_sessions where id = oldest.id
5. 返回 { sessionId }
```

### 4.3 被踢端体验

- 被踢端 access 仍最长 1h 有效；下次自动 refresh 失败 → `onAuthStateChange('SIGNED_OUT')` → 全局登出 → `/auth/login?reason=kicked`；
- 登录页 Toast：**"您的账号在其他设备登录，已被退出"**；
- 优化：authStore 启动时调 `GET /api/auth/session-status`，`{ valid:false, reason:'kicked' }` 立即登出。

### 4.4 不提供"我的设备"页

- `user_sessions` 仅用于（1）登录时检查会话数；（2）禁用账号时一次性 revoke + 删除。
- 不上心跳接口；`last_seen_at` 仅在调需鉴权接口时顺手更新。

---

## 5. 密码安全

| 项 | 值 |
|----|---|
| 存储 | bcrypt cost=10（GoTrue 默认）|
| 规则 | ≥ 8 位、含字母 + 数字；前端 zod 校验 + GoTrue 服务端再校 |
| 强度提示 | 弱 / 中 / 强（长度 + 字符多样性）；纯前端，不阻塞 |
| 登录失败限制 | 同 `email + ip` 5 次 / 15 min → 锁定到窗口结束（表 `auth_login_attempts`）|
| 解锁 | 自动到期；管理端可手动清除 |
| 防爆破补充 | 本期不接第三方验证码；仅靠节流（锁定 + 忘密 60s/1h + 注册 IP 1h ≤ 5）|

---

## 6. 被禁用账号

### 6.1 标记 & 联合效果

`profiles.is_disabled boolean default false` + `disabled_reason text` + `disabled_by uuid` + `disabled_at timestamptz`。

管理端「禁用」动作：

1. `update profiles set is_disabled=true, disabled_reason=?, disabled_by=?, disabled_at=now() where id=?`
2. `supabase.auth.admin.signOut(userId, { scope:'global' })` — 全 refresh revoke
3. `delete from user_sessions where user_id=?`
4. `disabledCache.delete(userId)` 让其他 Hono 进程立即感知
5. 写 `audit_logs` `action='user.disable'`

「启用」：`update profiles set is_disabled=false, disabled_reason=null where id=?` + 清缓存 + `audit_logs` `action='user.enable'`。

### 6.2 拦截位置

- **登录前置**：`POST /api/auth/login-attempt-record` 查 profiles → `is_disabled=true` 直接 401 `AUTH_ACCOUNT_DISABLED`，前端不再调 supabase；
- **每次请求**：`authRequired` 30s LRU 缓存内查 `profiles.is_disabled`；命中 `true` → 401 + 强制登出。

### 6.3 前端展示

登录页 Toast：**"账号已被停用，原因：{disabled_reason}。如有疑问请通过客服工单联系我们。"**（含跳转 `/help/contact`）。已登录用户被禁 → 下次 API 调用 `AUTH_ACCOUNT_DISABLED` → 全局登出 → 同上提示页。

---

## 7. 忘记密码

### 7.1 流程

```
1. /auth/forgot 提交 { email }
2. 前置：POST /api/auth/forgot-password-throttle（同 email 60s ≤ 1，同 IP 1h ≤ 5）
3. supabase.auth.resetPasswordForEmail(email, { redirectTo: '/auth/reset-password' })
4. 即使 email 不存在也返回成功（防枚举），统一提示"如该邮箱已注册，重置链接已发送"
5. 用户点邮件链接 → /auth/reset-password?access_token=...&type=recovery
6. 页面调 exchangeCodeForSession 进入 recovery session → 输入新密码 → updateUser({ password })
7. 成功：
   - 自动登入并跳 /me
   - 同时 supabase.auth.admin.signOut(userId, { scope:'others' }) 撚销其他设备
   - delete from user_sessions where user_id=? and id<>currentSessionId
8. 失败：链接过期 / 已使用 → AUTH_RESET_TOKEN_INVALID
```

### 7.2 频次限制

- 同 email 60s ≤ 1 次；同 IP 1h ≤ 5 次。
- Hono 路由 `POST /api/auth/forgot-password-throttle`；Redis key `forgot:{email}` / `forgot:ip:{ip}`，TTL 60s / 3600s。

---

## 8. 邮箱验证

- Supabase Auth `MAILER_AUTOCONFIRM=false`（必须验证）；
- Google 注册视为已验证（GoTrue 自动 set `email_confirmed_at`）；
- **本期邮件 mock**：dev / Docker 下写入 `system/.dev/mailbox/{email}-{timestamp}.eml`，控制台打印链接；prod 接真实 SMTP（变量见 `B01-architecture/06-deploy-env.md`）。
- 注册流程详见 [05-auth-feature-guideline §邮箱注册](./05-auth-feature-guideline.md)。

---

## 99. 待确认问题
（无）

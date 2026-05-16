<!-- TARGET-PATH: docs/B01-architecture/09-auth-infra.md -->

# 09 · 鉴权基础设施

> **阶段**：B01-A 架构  
> **角色**：架构师  
> **feature**：全局  
> **上游依赖**：`01-tech-stack.md`、`08-surfaces.md`、[`B02-permissions/02-auth-flow.md`](../B02-permissions/02-auth-flow.md)  
> **冻结状态**：已冻结 · 2026-04-28  
> **下游影响**：B02 权限规范、未来 `auth` / `auth` feature 的 C/D 全阶段

---

## 0. 摘要

- 鉴权底座 = **Supabase Auth (GoTrue)**，自托管；不使用 supabase.com。
- Token = **Supabase JWT（HS256，JWT_SECRET 共享）**；**存放于 httpOnly Cookie**（`zhiyu-at` / `zhiyu-rt`），不写 localStorage，防 XSS 泄露。
- 写请求强制 `X-CSRF-Token` Header + 同名非-HttpOnly Cookie 的 Double-Submit 校验。
- 密码哈希 = GoTrue 默认（bcrypt cost=10）；本项目不实现自管账号系统。
- Provider 接入位：邮箱 + Google OAuth；本期**两者均 mock**（dev 邮件落 `system/.dev/mailbox/`）。
- 会话：access 1h，refresh 30d，supabase-js 自动续期；密码重置 / 账号禁用立即撚销全部 refresh。
- 多设备硬上限 = **3 个活跃会话**，第 4 次登录踢最早。
- **角色仅两种**：`user`（应用端）/ `super_admin`（管理端唯一管理员，技术上允许多个，但本期无 UI 创建入口，按需手工 seed）。
- **不在 B 阶段输出**：登录页 / 注册页 / 找回密码页的具体交互——这些落到 `<surface>-auth` feature 的 C 循环。
- **本期不上 TOTP / 2FA**；防爆破靠后端节流（5 次 / 15 min 锁定 + IP 1h ≤ 5 次注册）。

---

## 1. Auth Provider 矩阵

| Provider | app surface | admin surface | 本期实现 | 未来 |
|----------|------------|--------------|---------|------|
| 邮箱 + 密码 | ✅ 注册 / 登录 | ✅ 邀请制注册 / 登录 | **mock**（任意密码通过 + 发送占位邮件）| Supabase Auth 真用 + SMTP/Resend |
| Google OAuth | ✅ 登录 | ❌ | **mock**（点击即生成假 user）| 真接 Google Cloud OAuth Client |
| 手机号 + OTP | ❌ | ❌ | 暂不实现 | 接腾讯云短信 / 东南亚本地服务商 |
| 微信 / Line / Apple | ❌ | ❌ | 暂不实现 | 视东南亚市场需求 |

> Provider 启用通过 Supabase `config.toml` 的 `[auth.external.*]` 节配置；mock 模式下 Edge Function `auth-google` 直接构造 JWT 返回。

---

## 2. Token 规格

| 项目 | 规格 |
|------|------|
| 签名算法 | HS256 |
| 共享密钥 | `JWT_SECRET`（≥ 32 字符）|
| access token TTL | 3600s（1h）|
| refresh token TTL | 2592000s（30d）|
| Claim 必备 | `sub`（user.id）、`aud`、`exp`、`iat`、`role`（Supabase role：`anon` / `authenticated` / `service_role`）|
| 自定义 Claim | `app_metadata.role: 'user' \| 'super_admin'` + `app_metadata.provider: 'email' \| 'google'`（仅这两种角色，不引入多角色矩阵）|
| 携带方式 | **优先 `zhiyu-at` Cookie**（HttpOnly + Secure + SameSite=Lax）；服务间调用兼容 `Authorization: Bearer` Header |
| CSRF | 登录后下发非-HttpOnly `zhiyu-csrf`（32 字节随机）；写请求必须 `X-CSRF-Token` 回传一致 |
| 刷新 | 前端 supabase-js 自定义 `cookieStorage` adapter，调同域代理 `POST /api/auth/cookie/set` 让 Hono Set-Cookie；access 到期前 60s 自动 refresh |

> **不自管账号**：业务表不存密码 / hash；账号 / 邮箱 / 密码哈希全部归 Supabase Auth 表（`auth.users`）管理。项目业务表 `public.users` 仅存 profile（昵称 / 头像 / 偏好），通过 `id` 1:1 关联 `auth.users.id`。

---

## 3. 后端鉴权中间件

**位置**：`system/apps/api-app/src/middlewares/auth.ts`（同款 `api-admin/middlewares/auth.ts`）

**职责**：
1. 解析 token：优先从 `zhiyu-at` Cookie 读取，回退 `Authorization: Bearer` Header（服务间调用）；
2. 写请求（POST/PUT/PATCH/DELETE）额外校验 CSRF Double-Submit：`X-CSRF-Token` Header 必须与 `zhiyu-csrf` Cookie 一致；
3. 失败 → `AppError(40100, 'unauthorized', 401)` / CSRF 失败 → `AppError(40300, 'csrf_invalid', 403)`；
4. 成功 → 将 `{ id, email, role, surface }` 注入 `c.var.user`（`role` 单数，仅 `'user' | 'super_admin'`）；
5. **角色守卫**：`api-admin` 在 `middlewares/rbac.ts` 强制 `role === 'super_admin'`。

```ts
// 示例（详细行为以 B02-permissions/02-auth-flow.md 为准）
app.use('*', requireAuth({ optional: false }))
app.use('/admin/*', requireRole('super_admin'))
```

> 与 [`B02-permissions/02-auth-flow.md`](../B02-permissions/02-auth-flow.md) 的「Cookie + CSRF」流程一致；任何冲突以 B02 为准。

---

## 4. 前端鉴权 helper

**位置**：`system/packages/supabase-client/src/browser.ts`

- 初始化 `createBrowserClient(SUPABASE_URL, SUPABASE_ANON_KEY)`；
- 暴露 `useSession()` hook（基于 `onAuthStateChange`），返回 `{ user, loading, signOut }`；
- 路由级守卫：TanStack Router 的 `_auth/` 根 loader 中调 `assertSession()`，未登录跳 `<surface>-auth` 的登录页。

---

## 5. Mock 实现规范

- **邮箱注册（mock）**：
  - Edge Function `auth-signup` 接受 `{ email, password }` → 调 `supabase.auth.admin.createUser({ email, password, email_confirm: true })`；
  - 立即返回登录态 token；不发真实验证邮件，仅向 `outbox` 表落一条 `verify_email` 占位（dev 可手动消费）。
- **邮箱登录（mock）**：直接走 Supabase Auth `signInWithPassword`，无额外 mock；缺密码服务时返回固定 fake token。
- **Google OAuth（mock）**：
  - Edge Function `auth-google` 不实际走 Google；
  - 接受 `{ mock_user: { email, name?, avatar? } }` → 构造 Supabase user → 返回登录态；
  - 前端登录页加 "Mock Google Login" 按钮（dev only）。

---

## 6. 会话与登出

- 前端登出：调 `POST /v1/auth/logout` → 后端清 `zhiyu-at` / `zhiyu-rt` / `zhiyu-csrf` 三只 Cookie（`Max-Age=0`）→ 同时 `supabase.auth.signOut()` 清前端 session 缓存 → 跳登录页。
- **不向 localStorage / sessionStorage 写任何 token**（HttpOnly Cookie 是唯一存储）。
- 后端登出 `/v1/auth/logout`：服务端落 Cookie 过期 Header + 调 `auth.admin.signOut(user_id)` revoke refresh token + 落 `auth_audit_log`。
- 强制下线（管理后台 → 学员）：`api-admin` 调 `supabase.auth.admin.signOut(user_id)` + 落审计日志；详见 [`B02-permissions/02-auth-flow.md §7`](../B02-permissions/02-auth-flow.md) 与多设备 3 上限策略。

---

## 7. 密码策略（mock 阶段也要校验）

- 长度 ≥ 8 字符
- 包含至少 1 字母 + 1 数字
- 校验在前端 + Edge Function `auth-signup` 双重执行
- 不暴露具体不符合的规则细节给前端（统一返回"密码强度不足"）

---

## 8. 审计

- 所有登录 / 登出 / 失败尝试都落 `audit_logs` 表（B02 数据结构）：
  - `action`：`auth.signup` / `auth.signin` / `auth.signin_failed` / `auth.signout` / `auth.password_reset`
  - `target_user_id`：被操作账号
  - `actor_user_id`：操作者（管理员强制下线时 ≠ target）
  - `ip` / `user_agent` / `surface`
- 失败登录连续 5 次 / IP / 10min → 触发 IP 临时封禁（中间件层，落 Redis）。

---

## 9. 未来 `<surface>-auth` feature 边界（**不在 B 阶段输出，但在此预告**）

| feature | C/D 阶段需输出 |
|---------|---------------|个人中心（账户信息 / 修改密码 / 修改邮箱 / 头像 / 显示名 / 偏好语言 / 登出）|
| `auth` | 仅邮箱密码登录页（无 Google 按钮）/ 忘密 / 安全设置；**不提供注册入口**（超管由 seed 脚本写入或手工 SQL 逆生）|

每个 auth feature 在自己的 `<surface>/` 子目录下出页面 / 路由 / 接口；公用本文件定义的 Token 规格、Provider 接入、密码策略、Cookie / CSRF 
每个 auth feature 在自己的 `<surface>/` 子目录下出页面 / 路由 / 接口；公用本文件定义的 Token 规格、Provider 接入、密码策略。

---

## 99. 待确认问题
（无）

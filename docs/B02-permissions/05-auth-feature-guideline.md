<!-- TARGET-PATH: docs/B02-permissions/05-auth-feature-guideline.md -->

# 05 · `<surface>-auth` feature 阶段指南

> **阶段**：B02-P  
> **上游**：`01-roles.md` / `02-auth-flow.md` / `03-authz-mechanism.md` / `04-data-model.md`  
> **下游**：`app-auth` / `admin-auth` 两个 feature 的全部 C/D 阶段产物  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 给"未来执行 `app-auth` / `admin-auth` C/D 循环"的同学（包括 AI）的**唯一**前置阅读。
- 列出每个 surface 必须覆盖的页面 / 接口 / 字段 / 错误码 / i18n key；超过本表的功能必须开变更单。
- 对应 `prompt/A-framework/A00-04-文档目录规划.md` 的 "feature 分阶段" 约定。

---

## 1. 两 feature 的范围对比

| 范围 | `app-auth`（surface=`app`）| `admin-auth`（surface=`admin`）|
|------|--------------------------|----------------------------|
| 注册页 | ✅ 邮箱 + Google 一键 | ❌ 无注册入口 |
| 登录页 | ✅ 邮箱密码 + Google 按钮 | ✅ 仅邮箱密码（不展示 Google）|
| 邮箱验证 | ✅ `verify-email-sent` + `auth/callback` | ❌（超管 seed 时已 `email_confirmed_at`）|
| 找回密码 | ✅ forgot + reset 两页 | ✅ 同（管理员忘密走相同流程）|
| 个人中心 / 账户信息 | ✅ 头像 / 显示名 / 邮箱 / 偏好语言 / 修改密码 / 退出 | ✅ 简化版：仅修改密码 / 退出（无头像 / 显示名编辑）|
| 删除账号 | ❌（本期不支持 self-delete）| ❌（超管严禁删自己）|
| 修改邮箱 | ❌ 本期不支持（变更走客服）| ❌ 同 |
| 2FA / TOTP | ❌ | ❌ |
| Onboarding（学习语言、HSK 起点）| ✅（首次登录后跳 `/onboarding`，但表单字段属 `user-account` feature 而非 `app-auth`）| ❌ |

> **以上未列出的功能（如手机号绑定、第三方账号合并、设备管理页…）本期均不实现。**

---

## 2. 两 feature 必须建的页面（C03 N 阶段产物）

### 2.1 `app-auth/app/`

| page-id | 路径 | 4 态 | 备注 |
|---------|------|------|------|
| `P-app-app-auth-001` | `/auth/login` | idle / submitting / error / kicked-back | redirect 参数支持 |
| `P-app-app-auth-002` | `/auth/register` | idle / submitting / error | 密码强度提示 |
| `P-app-app-auth-003` | `/auth/verify-email-sent` | sent / resend-throttled | "重新发送"按钮带 60s 倒计时 |
| `P-app-app-auth-004` | `/auth/callback` | exchanging / success / failed | OAuth + magic link 通用 |
| `P-app-app-auth-005` | `/auth/forgot` | idle / submitting / sent / throttled | — |
| `P-app-app-auth-006` | `/auth/reset-password` | idle / submitting / success / token-invalid | 重置成功后其他设备登出 |
| `P-app-app-auth-007` | `/me` | profile-view / loading / error | 个人中心首页，承载下方子页入口 |
| `P-app-app-auth-008` | `/me/security` | view / changing-password / done | 修改密码 + 退出登录 |
| `P-app-app-auth-009` | `/me/profile` | view / editing / saving | 头像 / 显示名 / 偏好语言 |

### 2.2 `admin-auth/admin/`

| page-id | 路径 | 4 态 | 备注 |
|---------|------|------|------|
| `P-admin-admin-auth-001` | `/admin/auth/login` | idle / submitting / error / not-admin / kicked-back | 仅邮箱密码 |
| `P-admin-admin-auth-002` | `/admin/auth/forgot` | idle / submitting / sent / throttled | — |
| `P-admin-admin-auth-003` | `/admin/auth/reset-password` | idle / submitting / success / token-invalid | 同 app |
| `P-admin-admin-auth-004` | `/admin/me` | view / changing-password / done | 简化账号设置：仅修改密码 + 退出 |

---

## 3. 接口清单（D02 L 阶段产物）

### 3.1 公开（无需 `authRequired`）

| Method | 路径 | 说明 |
|--------|------|------|
| `POST` | `/api/v1/auth/login-attempt-record` | 登录前置：禁用账号 + 节流检查 |
| `POST` | `/api/v1/auth/register-throttle` | 注册前置：IP / email 节流（GoTrue Hook 二次拦截）|
| `POST` | `/api/v1/auth/forgot-password-throttle` | 忘密前置：60s / 1h 节流 |
| `POST` | `/api/v1/auth/cookie/get` | supabase-js 适配器读 |
| `POST` | `/api/v1/auth/cookie/set` | supabase-js 适配器写 |
| `POST` | `/api/v1/auth/cookie/clear` | 登出 |
| `POST` | `/internal/auth-hook` | GoTrue `before_user_created` 回调（HMAC 验签）|

> admin 端使用相同公开接口，路径以 `/admin/v1/auth/*` 同构暴露；handler 复用同一份 service 逻辑，**仅做 surface 标签透传**。

### 3.2 需登录

| Method | 路径 | 说明 |
|--------|------|------|
| `POST` | `/api/v1/auth/session-register` | 登录成功后挂会话 + 3 设备检查 |
| `POST` | `/api/v1/auth/session-revoke` | 登出 |
| `GET`  | `/api/v1/auth/session-status` | 启动时拉一次："被踢" 判定 |
| `GET`  | `/api/v1/me` | 当前用户 profile |
| `PATCH`| `/api/v1/me` | 改 display_name / avatar_url / locale |
| `POST` | `/api/v1/me/password` | 修改密码（先 verify 旧密码）|

### 3.3 admin 专属

| Method | 路径 | 说明 |
|--------|------|------|
| `GET` | `/admin/v1/auth/me` | 管理员自己 profile（含 audit 摘要）|
| `POST` | `/admin/v1/auth/password` | 管理员改密 |

---

## 4. 必须遵守

1. **JWT 字段**：仅信任 `app_metadata.role` 和 `sub`；其他字段（如前端传来的 role hint）一律忽略。
2. **错误码**：完全使用 [03 §4](./03-authz-mechanism.md) 清单；不允许自定义新 `AUTH_*` 码（如必需，先开 B02 变更单加入清单）。
3. **i18n key 命名**：`auth.login.title` / `auth.register.field.password.weak` / `auth.error.AUTH_INVALID_CREDENTIALS` 等；5 语全量。
4. **页面跳转**：未登录守卫拦截 → `/auth/login?redirect=<full-url>`；登录后必须读 `redirect` 跳回。
5. **登录页与注册页底部**："登录" / "注册" 互链文字按钮（`text-button` + 红色文字）。
6. **OAuth 回调**：成功后强制读 `app_metadata.role`；非预期角色（如 admin 端用 Google 登录回来）→ 立即 `signOut` + `AUTH_NOT_ADMIN`。
7. **个人中心展示**：永远展示 `email`（脱敏前 3 字符 + `***@domain`），不展示完整 token / refresh token / 任何敏感字段。
8. **修改密码**：客户端 zod 校验 ≥ 8 + 字母 + 数字；服务端调 GoTrue 二次校验；成功后**保留当前会话**，但 revoke 其他设备 refresh。
9. **退出登录**："本设备退出" 与 "全部设备退出" 两个按钮；后者调 `supabase.auth.admin.signOut(userId, { scope: 'global' })`。
10. **审计**：所有 admin 写动作必须 `INSERT audit_logs`；app 端仅记 `auth.signin_success` / `auth.signout`。

---

## 5. 必须避开的反模式

- ❌ 在前端任何地方持有明文 access / refresh token；
- ❌ 让 admin 端能创建 / 列出其他 admin；
- ❌ "我的设备" 页 / 心跳接口；
- ❌ 第三方验证码（Turnstile / hCaptcha）；
- ❌ TOTP / WebAuthn / Passkey（v1 不上）；
- ❌ 在 `audit_logs` payload 中存明文密码 / token；
- ❌ Google OAuth 出现在管理端登录页；
- ❌ 注册流程跳过邮箱验证（除 Google）。

---

## 99. 待确认问题
（无）

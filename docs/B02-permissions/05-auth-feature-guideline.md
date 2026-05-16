<!-- TARGET-PATH: docs/B02-permissions/05-auth-feature-guideline.md -->

# 05 · `auth` feature 阶段指南（单 feature 多端）

> **阶段**：B02-P
> **上游**：[`01-roles.md`](./01-roles.md) · [`02-auth-flow.md`](./02-auth-flow.md) · [`03-authz-mechanism.md`](./03-authz-mechanism.md) · [`04-data-model.md`](./04-data-model.md) · [`B01-08 §5`](../B01-architecture/08-surfaces.md) · [`B01-09`](../B01-architecture/09-auth-infra.md)
> **下游**：`auth` feature 的全部 C / D 阶段产物（按 `auth/<surface>/` 多端形态拆分）
> **冻结状态**：已冻结 · 2026-04-28（双 feature 合并为单 feature 多端 · 2026-05-17）

---

## 0. 摘要

- 给"未来执行 `auth` C/D 循环"的同学（包括 AI）的**唯一**前置阅读。
- `auth` 是 **单一 feature 多端** 形态（A00-04 §四.5）；目录形如 `C0X/auth/{baseline 或 _shared, app/, admin/}`。
- 列出 `app` / `admin` 两端各自必须覆盖的页面 / 接口 / 字段 / 错误码 / i18n key；超出本表的功能必须开变更单。
- 与 `prompt/A-framework/A00-04-文档目录规划.md` 的 "多端 feature" 约定 1:1 对齐。

---

## 1. 两端范围对比

| 范围 | `app` 端 | `admin` 端 |
|------|----------|------------|
| 注册页 | ✅ 邮箱 + Google 一键 | ❌ 无注册入口（邀请制 + 运维 seed）|
| 登录页 | ✅ 邮箱密码 + Google 按钮 | ✅ 仅邮箱密码（不展示 Google）|
| 邮箱验证 | ✅ `verify-email-sent` + `auth/callback` | ❌（超管 seed 时已 `email_confirmed_at`）|
| 找回密码 | ✅ forgot + reset 两页 | ✅ 相同（管理员忘密走相同流程）|
| 个人中心 / 账户信息 | ✅ 头像 / 显示名 / 邮箱 / 偏好语言 / 修改密码 / 退出 | ✅ 简化版：仅修改密码 + 退出（无头像 / 显示名）|
| 删除账号 | ❌（本期不支持 self-delete）| ❌（超管严禁删自己）|
| 修改邮箱 | ❌（变更走客服）| ❌（变更走运维）|
| 2FA / TOTP | ❌ | ❌ |
| Onboarding（学习语言、HSK 起点）| ✅（首次登录跳 `/onboarding`，表单字段属 `user-account` feature 而非 `auth`）| ❌ |

> **以上未列出的功能（如手机号绑定、第三方账号合并、设备管理页…）本期均不实现。**

---

## 2. 必须建的页面（C03 N 阶段产物）

### 2.1 `auth/app/` （9 页，page-id `P-app-auth-NNN`）

| page-id | 路径 | 4 态 | 备注 |
|---------|------|------|------|
| `P-app-auth-001` | `/auth/login` | idle / submitting / error / kicked-back | redirect 参数支持 |
| `P-app-auth-002` | `/auth/register` | idle / submitting / error | 密码强度提示 |
| `P-app-auth-003` | `/auth/verify-email-sent` | sent / resend-throttled | "重新发送" 60s 倒计时 |
| `P-app-auth-004` | `/auth/callback` | exchanging / success / failed | OAuth + magic link 通用 |
| `P-app-auth-005` | `/auth/forgot` | idle / submitting / sent / throttled | — |
| `P-app-auth-006` | `/auth/reset-password` | idle / submitting / success / token-invalid | 重置成功后其他设备登出 |
| `P-app-auth-007` | `/me` | profile-view / loading / error | 个人中心首页，承载子页入口 |
| `P-app-auth-008` | `/me/security` | view / changing-password / done | 修改密码 + 退出 |
| `P-app-auth-009` | `/me/profile` | view / editing / saving | 头像 / 显示名 / 偏好语言 |

### 2.2 `auth/admin/` （4 页，page-id `P-admin-auth-NNN`）

| page-id | 路径 | 4 态 | 备注 |
|---------|------|------|------|
| `P-admin-auth-001` | `/admin/auth/login` | idle / submitting / error / not-admin / kicked-back | 仅邮箱密码 |
| `P-admin-auth-002` | `/admin/auth/forgot` | idle / submitting / sent / throttled | — |
| `P-admin-auth-003` | `/admin/auth/reset-password` | idle / submitting / success / token-invalid | 同 app |
| `P-admin-auth-004` | `/admin/me` | view / changing-password / done | 简化账号设置：仅修改密码 + 退出 |

> 命名遵循 `A00-03 §四`：多端项目 P-ID 格式 `P-<surface>-<feature>-<seq3>`，feature 统一为 `auth`。

---

## 3. 接口清单（D02 L 阶段产物）

> 多端项目接口路由前缀强制 `/api/<surface>/*`（A00-03 §四），故 app 端走 `/api/app/v1/...`、admin 端走 `/api/admin/v1/...`；为兼容 `/system` 现状，保留 `/api/v1/auth/*` 作为对外稳定别名。

### 3.1 公开（无需 `authRequired`）

| Method | 路径 | 说明 | scope |
|--------|------|------|:----:|
| `POST` | `/api/v1/auth/login-attempt-record` | 登录前置：禁用账号 + 节流检查 | both |
| `POST` | `/api/v1/auth/register-throttle` | 注册前置：IP / email 节流（GoTrue Hook 二次拦截） | app |
| `POST` | `/api/v1/auth/forgot-password-throttle` | 忘密前置：60s / 1h 节流 | both |
| `POST` | `/api/v1/auth/cookie/{get,set,clear}` | supabase-js 适配器 cookie 操作 | both |
| `POST` | `/internal/auth-hook` | GoTrue `before_user_created` 回调（HMAC 验签） | both |

> admin 端走相同 service 逻辑；handler 仅做 surface 标签透传，便于 `user_sessions.surface` 与审计区分。

### 3.2 需登录

| Method | 路径 | 说明 | scope |
|--------|------|------|:----:|
| `POST` | `/api/v1/auth/session-register` | 登录成功挂会话 + 3 设备检查 | both |
| `POST` | `/api/v1/auth/session-revoke` | 退出 | both |
| `GET`  | `/api/v1/auth/session-status` | 启动时拉一次：被踢判定 | both |
| `GET`  | `/api/app/v1/me` | 当前用户 profile（含 avatar/display_name/locale） | app |
| `PATCH`| `/api/app/v1/me` | 改 display_name / avatar_url / locale | app |
| `POST` | `/api/app/v1/me/password` | 修改密码（先 verify 旧密） | app |
| `GET`  | `/api/admin/v1/me` | 管理员自己 profile（含 audit 摘要） | admin |
| `POST` | `/api/admin/v1/me/password` | 管理员改密 | admin |

---

## 4. 必须遵守

1. **JWT 字段**：仅信任 `app_metadata.role` 和 `sub`；前端传来的 role hint 一律忽略。
2. **错误码**：完全使用 [03 §4](./03-authz-mechanism.md) 清单；不允许自定义新 `AUTH_*` 码（如必需，先开 B02 变更单加入清单）。
3. **i18n key 命名**：`auth.login.title` / `auth.register.field.password.weak` / `auth.error.AUTH_INVALID_CREDENTIALS` 等；5 语全量；admin 端复用 80%，差异 key 命名 `auth.admin.*`。
4. **页面跳转**：未登录守卫拦截 → `/auth/login?redirect=<full-url>`（admin 端：`/admin/auth/login?redirect=...`）；登录后必须读 `redirect` 跳回。
5. **登录/注册互链**：app 端登录页与注册页底部互链文字按钮（`text-button` + 红色文字）；admin 端无注册页，故无对应链接。
6. **OAuth 回调**：仅 app 端启用；成功后强制读 `app_metadata.role`；非预期角色（如返回 admin 角色）→ 立即 `signOut` + Toast。admin 端如收到任何 OAuth 回调请求一律拒绝。
7. **个人中心展示**：永远展示 `email`（脱敏前 3 字符 + `***@domain`），不展示完整 token / refresh token / 任何敏感字段。
8. **修改密码**：客户端 zod 校验 ≥ 8 + 字母 + 数字；服务端调 GoTrue 二次校验；成功后**保留当前会话**，但 revoke 其他设备 refresh。
9. **退出登录**："本设备退出" 与 "全部设备退出" 两个按钮；后者调 `supabase.auth.admin.signOut(userId, { scope: 'global' })`。
10. **审计**：所有 admin 写动作必须 `INSERT audit_logs`；app 端仅记 `auth.signin_success` / `auth.signout`；严禁明文密码 / token 入 payload。
11. **admin 角色守卫**：`/admin/*` 全路径在 TanStack Router `_admin` 根 loader + 后端 `requireRole('super_admin')` 双重校验；非超管 → `/admin/auth/login?error=not_admin` + `AUTH_USE_USER_ENTRY`。
12. **3 设备硬上限按端隔离**：`user_sessions.surface` 上独立计数，app 与 admin 互不影响。

---

## 5. 必须避开的反模式

- ❌ 在前端任何地方持有明文 access / refresh token；
- ❌ 让 admin 端能创建 / 列出其他 admin（v1 不上 `admin-users` feature）；
- ❌ "我的设备" 页 / 心跳接口；
- ❌ 第三方验证码（Turnstile / hCaptcha）；
- ❌ TOTP / WebAuthn / Passkey（v1 不上）；
- ❌ 在 `audit_logs` payload 中存明文密码 / token；
- ❌ Google OAuth 出现在管理端登录页；
- ❌ 注册流程跳过邮箱验证（除 Google）；
- ❌ 将 `app-auth` / `admin-auth` 作为两个独立 feature 处理（已废弃 · 详见 2026-05-17 changelog）。

---

## 6. C / D 阶段产出位置速查

| 阶段 | 路径 | 形态 |
|------|------|------|
| C01 R | `docs/C01-requirements/auth/baseline.md` + `flows/` + `app/notes.md` + `admin/notes.md` | 基线单份 + 流程 + 端补充 |
| C02 I | `docs/C02-ia/auth/{_shared/{state-machines.md,flows-shared.md}, app/{00..07,99}.md, admin/{00..07,99}.md}` | _shared + per-surface |
| C03 N | `docs/C03-pages/auth/{app/P-app-auth-NNN.md, admin/P-admin-auth-NNN.md}` | per-surface |
| C04 H | `docs/C04-prototype/auth/{app,admin}/{index.html, pages/, states/, ...}` | per-surface |
| C05 E | `docs/C05-prd/auth/{_shared/{glossary.md,business-rules.md}, app/, admin/}` | _shared + per-surface |
| D01 D | （未生成）`docs/D01-data/auth/01-tables.md` | 数据模型单份 |
| D02 L | （未生成）`docs/D02-api/auth/{app,admin}/01-routes-delta.md` | per-surface |
| D03 V | （未生成）`docs/D03-validation/auth/V01-V03.md` | 单份 |

---

## 99. 待确认问题
- `AUTH_USE_USER_ENTRY` 在 G3 / B02-01 文案中的归口确认（同 `B02 §99` Q-2026-05-16-01）。

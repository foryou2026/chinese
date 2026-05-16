<!-- TARGET-PATH: docs/C01-requirements/auth/baseline.md -->

# `auth` · 需求基线（跨端单一真相）

> **阶段**：C01-R · **feature**：`auth` · **surface**：`app` + `admin`（多端单 feature）
> **上游**：
> - 输入草案：[`_input/app-draft.md`](./_input/app-draft.md)、[`_input/admin-draft.md`](./_input/admin-draft.md)
> - B02 规范：[`05-auth-feature-guideline.md`](../../B02-permissions/05-auth-feature-guideline.md)、[`02-auth-flow.md`](../../B02-permissions/02-auth-flow.md)、[`03-authz-mechanism.md`](../../B02-permissions/03-authz-mechanism.md)、[`04-data-model.md`](../../B02-permissions/04-data-model.md)
> - B03 语气：[`04-voice-tone.md`](../../B03-ux/04-voice-tone.md)
> **下游**：本 feature 全部 C02 / C03 / C04 / C05 产物；未来 D 阶段路由必须覆盖全部 R-ID。
> **冻结状态**：已冻结 · 2026-05-16（合并 app-auth+admin-auth 双 feature 重构 · 2026-05-17）

---

## 0. 摘要

- 本文件是 `auth` feature 在 **app 端 + admin 端** 共同的「需求基线」单一真相；按 `R-auth-NNN` 切分原子需求。
- 多端范围由 **scope** 列声明：`app` / `admin` / `both`；surface 特有差异（例：admin 强制角色守卫、admin 无注册）通过：
  - [`app/notes.md`](./app/notes.md)：app 端补充说明
  - [`admin/notes.md`](./admin/notes.md)：admin 端补充说明
- 共 25 条 R-ID（app 范围 17 条 / admin 范围 10 条 / 两端共有 8 条）。
- C02 流程：
  - 共享/跨端：[`_shared/state-machines.md`](../../C02-ia/auth/_shared/state-machines.md)、[`_shared/flows-shared.md`](../../C02-ia/auth/_shared/flows-shared.md)
  - per-surface：[`app/02-flows.md`](../../C02-ia/auth/app/02-flows.md)、[`admin/02-flows.md`](../../C02-ia/auth/admin/02-flows.md)

---

## 1. R-ID 列表

| R-ID | scope | 一句话 | 关联页面 | 关联接口 / 适配器 |
|------|:----:|--------|----------|--------------------|
| **R-auth-001** | app | 邮箱 + 密码注册账号，必须邮箱验证后才能首次登入 | `P-app-auth-002` / `003` / `004` | `register-throttle` / Supabase `signUp` / Hook |
| **R-auth-002** | app | Google 一键注册即登录，无需邮箱验证 | `P-app-auth-002` / `004` | Supabase `signInWithOAuth` / Hook |
| **R-auth-003** | both | 邮箱 + 密码登录；登录前置节流 + 禁用检查（admin 端额外要求 `super_admin` 角色，非超管立即 signOut 并报 `AUTH_USE_USER_ENTRY`） | app: `P-app-auth-001`<br>admin: `P-admin-auth-001` | `login-attempt-record` / `signInWithPassword` |
| **R-auth-004** | both | 登录态 HttpOnly Cookie（`zhiyu-at`/`zhiyu-rt`）；30 天 refresh；CSRF Double-Submit（写请求必须带 `X-CSRF-Token`） | 跨页（不可见） | `cookie/get` / `set` / `clear` |
| **R-auth-005** | both | 多设备活跃会话 ≤ 3，第 4 台踢最早；`user_sessions.surface` 按端独立计数 | app: 跨页 + `P-app-auth-001` "kicked"<br>admin: 跨页 + `P-admin-auth-001` "kicked" | `session-register` / `session-status` |
| **R-auth-006** | both | 5/15min 错密 → 自动锁定 15min；`profiles.is_disabled=true` → 全设备登出 + 拒登 | app: `P-app-auth-001` "error"<br>admin: `P-admin-auth-001` "error" | `login-attempt-record` |
| **R-auth-007** | both | 忘记密码 → 邮件链接 → 设新密码 → 自动登入并踢其它设备；链接 15min 一次性 | app: `P-app-auth-005` / `006`<br>admin: `P-admin-auth-002` / `003` | `forgot-password-throttle` / `resetPasswordForEmail` / `updateUser` |
| **R-auth-008** | both | 已登录用户可修改密码（先验旧密）+ 选「全部设备退出」 | app: `P-app-auth-008`<br>admin: `P-admin-auth-004` | `POST /api/<surface>/me/password` |
| **R-auth-009** | both | 用户可随时「本设备退出」或「全部设备退出」 | app: `P-app-auth-008` + 顶栏头像<br>admin: `P-admin-auth-004` | `cookie/clear` / `session-revoke` / `admin.signOut('global')` |
| **R-auth-010** | both | 路由守卫：未登录访问受保护页 → 跳 `/auth/login?redirect=<full-url>`（admin 端跳 `/admin/auth/login?redirect=...`，且额外做 `super_admin` 校验，非超管跳 `?error=not_admin`） | 跨页（守卫层） | — |
| **R-auth-011** | app | 已登录用户可查看 / 修改 profile：头像 / 显示名 / 偏好语言 | `P-app-auth-007` / `009` | `GET/PATCH /api/app/me` |
| **R-auth-012** | app | OAuth 回调失败 / 用户取消 → 静默回登录页；OAuth 角色异常 → Toast + 登出 | `P-app-auth-004` | — |
| **R-auth-013** | app | 邮箱验证 / 重置链接过期 → 「链接已过期」页 + 重新发起入口 | `P-app-auth-003` / `006` "token-invalid" 态 | — |
| **R-auth-014** | app | 邮箱已注册时注册提示「已注册，请去登录或找回密码」；找回密码不暴露邮箱是否存在 | `P-app-auth-002` / `005` | — |
| **R-auth-015** | app | 「重新发送验证邮件」按钮带 60s 倒计时 + 60s/1h 双层节流 | `P-app-auth-003` | `register-throttle`（复用）|
| **R-auth-016** | admin | （已并入 R-auth-003 admin 分支）保留 ID 为占位，避免历史链接断裂 | — | — |
| **R-auth-017** | admin | （已并入 R-auth-010 admin 分支）保留 ID 为占位 | — | — |
| **R-auth-018** | admin | （已并入 R-auth-004）保留 ID 为占位 | — | — |
| **R-auth-019** | admin | （已并入 R-auth-005）保留 ID 为占位 | — | — |
| **R-auth-020** | admin | （已并入 R-auth-006）保留 ID 为占位 | — | — |
| **R-auth-021** | admin | （已并入 R-auth-007）保留 ID 为占位 | — | — |
| **R-auth-022** | admin | （已并入 R-auth-008）保留 ID 为占位 | — | — |
| **R-auth-023** | admin | （已并入 R-auth-009）保留 ID 为占位 | — | — |
| **R-auth-024** | admin | （已并入 R-auth-010）保留 ID 为占位 | — | — |
| **R-auth-025** | admin | 管理员账号 seed 创建（**无产品功能**）：通过运维脚本 `scripts/db/seed-super-admin.sh` 创建，密码运维侧明文交付；本条仅为契约存档 | — | — |

> **占位说明**（R-auth-016 ~ R-auth-024）：原 admin-auth feature 的 R-001..009 在合并后语义上已被 R-auth-003/004/005/006/007/008/009/010 的 admin 分支收编；为防止历史 C02/C05 文件中 9 处占位链接出现 404，先以"占位 + 指向"形式保留，待 C02 覆盖矩阵 Round 8 一次性清理后再回收 ID 段。
>
> 后续 C02/C03 任何 page-id 或接口必须能被至少一个 R-ID 覆盖，反之每条 **有效** R-ID 必须能被至少一个 page-id 或接口覆盖（详见 [`C02 §06 覆盖矩阵`](../../C02-ia/auth/app/06-coverage-matrix.md) / [`admin/06-coverage-matrix.md`](../../C02-ia/auth/admin/06-coverage-matrix.md)）。

---

## 2. 非功能需求（NFR）

| NFR | 目标 | scope |
|-----|------|:---:|
| 登录页 TTFB | < 200ms（CDN 缓存静态壳） | both |
| `signInWithPassword` 请求时延 | p95 < 800ms（含锁定查表 + Supabase Auth） | both |
| 注册到验证邮件到达 | dev/mock：即时落盘 `system/.dev/mailbox/`；prod：< 30s（v2 接 SMTP） | app |
| 重置邮件到达 | dev mock → `system/.dev/mailbox/` · prod → SMTP | both |
| 任意 auth 接口可用性 | ≥ 99.5% | both |
| 密码 bcrypt cost | 10（GoTrue 默认） | both |
| 错误码国际化覆盖 | 5 语全量（zh/en/vi/th/id） | both |
| 无障碍 | WCAG AA；表单可纯键盘完成；focus ring 可见 | both |
| 审计 | 所有 admin 端的登录 / 改密 / 退出 100% 入 `audit_logs` | admin |
| 浏览器存储 | 严禁缓存任何 admin token 于 `localStorage` / `sessionStorage`；严禁明文密码入日志 / 审计 payload | admin |

---

## 3. 范围外（明确不做）

| 项 | scope | 理由 / 推迟到 |
|----|:----:|---------------|
| 手机号登录 | both | 东南亚短信成本高，v2 评估 |
| 微信 / Apple / Facebook OAuth | both | v2 评估 |
| 2FA（TOTP / WebAuthn） | both | v1 不上 |
| 第三方验证码（Turnstile / hCaptcha） | both | 仅靠节流；v2 若被刷再加 |
| Magic Link 登录 | both | 与「邮箱密码」互斥；本期只走密码 |
| 设备管理 / 「我的设备」页 | both | 仅后台用 `user_sessions` 做硬上限，不暴露给用户 |
| Self-delete 账号 | both | 走客服工单 / 运维变更；管理员严禁删自己 |
| 改邮箱 | both | 走客服工单 / 运维变更 |
| 改密期间保留其他设备 | both | 安全要求一律踢；不开放选项 |
| 头像上传图床 | app | v1 仅接受 URL 输入（OAuth 自动填）；v2 上传 |
| 注册页 | admin | 邀请制，无自助注册 |
| Google OAuth | admin | 管理端 100% 邮密 |
| 邮箱验证页 | admin | seed 时已 `email_confirmed_at` |
| 头像 / 显示名编辑 | admin | 管理端不展示头像 |
| 自助邀请 UI | admin | v2+（需先升级 B02-01）|
| 管理员列表 / 改他人密码 | admin | v2+（归 `admin-users` feature）|

---

## 4. 验收准则（与未来 D03 V03 对齐）

- app 端 9 个页面（`P-app-auth-001`..`009`）全部具有 idle / loading / error / 4 态以上；
- admin 端 4 个页面（`P-admin-auth-001`..`004`）同样满足态覆盖；
- 所有错误码在 [`03-authz-mechanism §4`](../../B02-permissions/03-authz-mechanism.md) 清单内；
- 所有路由可被未来 `D02-api/auth/{app,admin}/01-routes-delta.md` 覆盖；
- 非 `super_admin` 用 user 账号尝试登录 `/admin/auth/login` → 立即 signOut + Toast「请使用用户入口登录」；
- 任意管理员密码改成功 → 立即在另一个浏览器收到 401 → 跳回 `/admin/auth/login`；
- 管理员尝试登录第 4 设备 → 第 1 设备 10 秒内被踢（轮询 `session-status`）；
- D 阶段未新增本 feature 独占表（沿用 [B02-04](../../B02-permissions/04-data-model.md) 5 张表）。

---

## 5. R-ID 与 B 阶段映射

| R-ID 范围 | B 阶段依据 |
|---|---|
| R-auth-001 / 002 | `B02-02` §2 注册流程 · OAuth provider 接入位 |
| R-auth-003 / 004 / 009 | `B02-02` 主流程 · `B02-03` 中间件 · `B01-09 §3` |
| R-auth-005 | `B01-09 §0`「3 设备硬上限」 |
| R-auth-006 | `B02-02 §6` 节流 · `B02-04` `auth_login_attempts` |
| R-auth-007 / 013 / 015 | `B02-02 §5` 重置 / 验证流程 |
| R-auth-008 | `B02-05 §3` `/me/password` |
| R-auth-010 | `B02-05 §4.4` redirect 约定 |
| R-auth-011 | `B02-05 §3` `/me` GET/PATCH |
| R-auth-014 | `B02-02 §2.3` 注册响应不暴露存在性 |
| R-auth-025 | `B01-09 §1`「邀请制注册」备注 · `seed.sql` |

---

## 6. 待确认问题

详见 [`99-open-questions.md`](./99-open-questions.md) 与 [`B02 §99`](../../B02-permissions/99-open-questions.md)（`AUTH_USE_USER_ENTRY` 文案归口）。

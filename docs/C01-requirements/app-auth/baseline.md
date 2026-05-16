<!-- TARGET-PATH: docs/C01-requirements/app-auth/baseline.md -->

# `app-auth` · 需求基线

> **阶段**：C01-R · **feature**：`app-auth` · **surface**：`app`  
> **上游**：[`_input/draft.md`](./_input/draft.md)、[`docs/B02-permissions/05-auth-feature-guideline.md`](../../B02-permissions/05-auth-feature-guideline.md)、[`02-auth-flow.md`](../../B02-permissions/02-auth-flow.md)、[`B03-ux/04-voice-tone.md`](../../B03-ux/04-voice-tone.md)  
> **下游**：本 feature C02 / C03 / C05 全部产物；D 阶段路由必须覆盖本基线全部 R-ID  
> **冻结状态**：已冻结 · 2026-05-16

---

## 0. 摘要

- 应用端「账号生命周期」一组完整需求：注册 / 邮箱验证 / 登录 / OAuth / 找回密码 / 修改密码 / 个人资料编辑 / 退出登录 / 被踢提示。
- 9 个一级页面，列于 [B02-05 §2.1](../../B02-permissions/05-auth-feature-guideline.md)；本文件按 **R-ID** 切分原子需求，供后续阶段引用。
- 不包含：onboarding、删账号、改邮箱、2FA、设备管理、手机号、第三方账号合并。

---

## 1. R-ID 列表

| R-ID | 一句话 | 关联页面 | 关联接口 |
|------|--------|---------|---------|
| **R-app-auth-001** | 邮箱 + 密码注册账号，必须邮箱验证后才能首次登入 | `P-app-app-auth-002` / `003` / `004` | `register-throttle` / Supabase `signUp` / Hook |
| **R-app-auth-002** | Google 一键注册即登录，无需邮箱验证 | `P-app-app-auth-002` / `004` | Supabase `signInWithOAuth` / Hook |
| **R-app-auth-003** | 邮箱 + 密码登录；登录前置节流 + 禁用检查 | `P-app-app-auth-001` | `login-attempt-record` / `signInWithPassword` |
| **R-app-auth-004** | 登录态 HttpOnly Cookie 存放；30 天 refresh；CSRF Double-Submit | 跨页（不可见）| `cookie/get` / `set` / `clear` |
| **R-app-auth-005** | 多设备活跃会话 ≤ 3，第 4 台踢最早 | 跨页 + `P-001` "kicked" 态 | `session-register` / `session-status` |
| **R-app-auth-006** | 5/15min 错密 → 自动锁定 15min；账号禁用 → 全设备登出 + 拒登 | `P-001` "error" 态 | `login-attempt-record` |
| **R-app-auth-007** | 忘记密码 → 邮件链接 → 设新密码 → 自动登入并踢其它设备 | `P-005` / `P-006` | `forgot-password-throttle` / `resetPasswordForEmail` / `updateUser` |
| **R-app-auth-008** | 已登录用户可查看 / 修改 profile：头像 / 显示名 / 偏好语言 | `P-007` / `P-009` | `GET/PATCH /api/v1/me` |
| **R-app-auth-009** | 已登录用户可修改密码（先验旧密）+ 选「全部设备退出」 | `P-008` | `POST /api/v1/me/password` |
| **R-app-auth-010** | 用户可随时「本设备退出」或「全部设备退出」 | `P-008` + 顶栏头像 | `cookie/clear` / `session-revoke` / `admin.signOut('global')` |
| **R-app-auth-011** | OAuth 回调失败 / 用户取消 → 静默回登录页；OAuth 角色异常 → Toast + 登出 | `P-004` | — |
| **R-app-auth-012** | 邮箱验证 / 重置链接过期 → 「链接已过期」页 + 重新发起入口 | `P-003` / `P-006` "token-invalid" 态 | — |
| **R-app-auth-013** | 路由守卫：未登录访问受保护页 → 跳 `/auth/login?redirect=<full-url>` | 跨页（守卫层）| — |
| **R-app-auth-014** | 邮箱已注册时注册提示「已注册，请去登录或找回密码」；找回密码不暴露邮箱是否存在 | `P-002` / `P-005` | — |
| **R-app-auth-015** | 「重新发送验证邮件」按钮带 60s 倒计时 + 60s/1h 双层节流 | `P-003` | `register-throttle`（复用）|

> 后续 C02/C03 任何 page-id 或接口必须能被至少一个 R-ID 覆盖，反之每个 R-ID 必须能被至少一个 page-id 或接口覆盖（详见 [C02 §06 覆盖矩阵](../../C02-ia/app-auth/06-coverage-matrix.md)）。

---

## 2. 非功能需求

| NFR | 目标 |
|-----|------|
| 登录页 TTFB | < 200ms（CDN 缓存静态壳）|
| signInWithPassword 请求时延 | p95 < 800ms |
| 注册到验证邮件到达 | dev/mock：即时落盘 `system/.dev/mailbox/`；prod：< 30s（v2 接 SMTP）|
| 任意 auth 接口可用性 | ≥ 99.5% |
| 密码 bcrypt cost | 10（GoTrue 默认）|
| 错误码国际化覆盖 | 5 语全量（zh/en/vi/th/id）|
| 无障碍 | WCAG AA；表单可纯键盘完成；focus ring 可见 |

---

## 3. 范围外（明确不做）

| 项 | 理由 / 推迟到 |
|----|--------------|
| 手机号登录 | 东南亚短信成本高，v2 评估 |
| 微信 / Apple / Facebook OAuth | v2 评估 |
| 2FA（TOTP / WebAuthn）| v1 不上 |
| 第三方验证码（Turnstile / hCaptcha）| 仅靠节流；v2 若被刷再加 |
| Magic Link 登录 | 与"邮箱密码"互斥；本期只走密码 |
| 设备管理 / "我的设备"页 | 仅后台用 user_sessions 做硬上限，不暴露给用户 |
| Self-delete 账号 | 走客服工单；v2 评估 |
| 改邮箱 | 走客服工单；v2 评估 |
| 改密期间保留其他设备 | 安全要求一律踢；不开放选项 |
| 头像图床 | v1 仅接受 URL 输入（OAuth 自动填）；v2 上传 |

---

## 4. 验收准则（与 D03 V03 对齐）

- 9 个页面全部具有 idle / loading / error / 4 态以上（详 [B02-05 §2.1](../../B02-permissions/05-auth-feature-guideline.md)）；
- 所有错误码在 [03-authz-mechanism §4](../../B02-permissions/03-authz-mechanism.md) 清单内；
- 所有路由通过 [`D02-api/app-auth/01-routes-delta.md`](../../D02-api/app-auth/01-routes-delta.md) 注册到 `_global-routes.md`；
- D01 D 阶段未新增本 feature 独占表（沿用 B02-04 5 张表）；
- D03 V01/V02/V03 全绿。

---

## 5. 待确认问题
（无 · 全部已闭合在 B02-permissions/99）

<!-- TARGET-PATH: docs/C04-pages/auth/app/P-app-auth-001.md -->

# `P-app-auth-001` · 登录

> **阶段**：C04-N · **feature**：`auth` · **surface**：`app`
> **角色可见**：未登录（已登录访问自动跳 `/`）
> **R 覆盖**：R-003 / 004 / 005 / 006 / 011 / 013
> **冻结状态**：已冻结 · 2026-05-16

## 1. 布局

- 全局顶栏（GlassNav）：未登录态，右上「主题 / 语言 / 登录 / 注册」；
- 内容区居中卡片 `<GlassCard>`，桌面宽 480px / 移动 100% - 32px；卡片顶部 60px；
- 远景层 + 红色径向光晕（B03 §02-layout §3）。

## 2. DOM 骨架

```
GlassCard
  ├─ h1 「欢迎回来」 (text-h1)
  ├─ p  「登录账号继续学习」 (text-body text-secondary)
  ├─ button.secondary [Google 继续]   ← 移动端置顶；桌面在表单上方
  ├─ divider「或」
  ├─ form
  │    ├─ field email   (autoFocus, type=email, autocomplete=email)
  │    ├─ field password (type=password, autocomplete=current-password)
  │    │     右上角「忘记密码？」link → /auth/forgot
  │    └─ button.primary [登录] (loading + disabled in submitting)
  └─ p.footer 「还没有账号？」 link 「立即注册」 → /auth/register
```

## 3. 字段

| key | 类型 | 约束（展示用） | 错误提示 i18n |
|-----|------|----------------|--------------|
| email | string | 邮箱格式 | `auth.login.field.email.invalid` |
| password | string | 长度 ≥ 8 | `auth.login.field.password.tooShort` |

> 字段语义仅用于客户端表单交互提示；完整校验 schema（含服务端二次校验）在 **D01-data 开始定义**。

## 4. 4 + 1 态

| 态 | 触发 | UI 表现 |
|---|------|---------|
| `idle` | 默认 | 字段可填，按钮校验通过才高亮 |
| `submitting` | 提交后 | 按钮 spinner + disabled；字段 readonly |
| `error` | 4xx 返回 | 顶部 Toast (5xx) 或字段下内联 (字段类 4xx)；进入 idle 可重试 |
| `kicked-back` | `?reason=kicked` | 顶部 Toast「您的账号在其他设备登录，已被退出」+ 进入 idle |
| `locked` | `login-attempt-record` 返 429 | 按钮替换为「mm:ss 后可重试」灰色禁用；倒计时实时刷新；倒计时到 0 回 idle |

> `?reason=disabled` 在 `error` 态下展示“账号已停用” + 客服入口；`?reason=expired` Toast「登录已过期，请重新登录」；`?reason=signout` 不弹 Toast。

## 5. 关键交互

- **提交**：点击“登录” → 进入 `submitting` 态 → 发起邀请 `auth` 服务的登录（节流检查 + 凭证校验 + 会话登记，具体接口在 D02-api/auth/app/login 定义）→ 成功后跳 `redirect ?? '/'`。
- **Google**：点击 “Google 继续” → 发起 OAuth 跳转（跳回 对应页面，详见 P-app-auth-004）；本页不做预校验。
- **redirect**：query 中带 `redirect=<encoded url>`；登录成功优先跳此；缺省跳 `/`。
- **守卫**：已登录访问本页时，路由 root loader 自动 navigate 走（实现细节与auth 路由守卫一同在 D02 定义）。

## 6. 错误码映射

| code | 表现位置 | i18n key |
|------|---------|---------|
| `AUTH_LOGIN_RATE_LIMITED` | 整页 `locked` 态 + 倒计时 | `auth.error.rateLimited` |
| `AUTH_ACCOUNT_DISABLED` | 顶部 Toast + 客服入口 | `auth.error.accountDisabled` |
| `AUTH_INVALID_CREDENTIALS` | 密码字段下内联 | `auth.error.invalidCredentials` |
| `AUTH_EMAIL_NOT_VERIFIED` | 顶部 Toast + 「重发验证邮件」按钮 → 走 register-throttle | `auth.error.emailNotVerified` |
| `AUTH_OAUTH_FAILED` | 顶部 Toast | `auth.error.oauthFailed` |
| 5xx | 顶部 Toast「服务异常」+ 表单值保留 | `common.error.server` |

## 7. 移动端差异

- 主按钮 100% 宽；
- Google 按钮置顶；
- 副链接「忘记密码 / 注册」上下排列，每个 44px 高。

## 8. 无障碍

- email 字段 `autoFocus`；
- 全部字段 `<label for>` 关联；
- 错误提示 `aria-live="polite"`；
- 按钮 disabled 时仍可 focus（含 `aria-disabled="true"`）。

## 9. 性能 / 埋点

- 首屏不调任何
- 提交开始 `analytics.track('auth.signin_attempt')`；成功 / 失败追加各自事件（事件 schema 见 `analytics` feature，暂不支持）。

## 10. 场景验证

详见 [`P-app-auth-001.scenarios.md`](./P-app-auth-001.scenarios.md)。

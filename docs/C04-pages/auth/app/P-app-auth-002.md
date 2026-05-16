<!-- TARGET-PATH: docs/C04-pages/auth/app/P-app-auth-002.md -->

# `P-app-auth-002` · 注册

> **path**：`/auth/register` · **角色可见**：未登录  
> **R 覆盖**：R-001 / 002 / 014  
> **冻结状态**：已冻结 · 2026-05-16

## 1. 布局
同 P-001 的 `<GlassCard>` 模板（480 / 100%）。

## 2. DOM 骨架

```
GlassCard
  ├─ h1 「创建账号，开始学」
  ├─ p  「东南亚汉语学习平台」 (副标题)
  ├─ button.secondary [Google 一键注册]   ← 即「Google 登录」按钮，文案因角色态不同
  ├─ divider「或」
  ├─ form
  │    ├─ field email
  │    ├─ field password (含强度条 weak/medium/strong)
  │    │     hint「至少 8 位，含字母 + 数字」
  │    └─ button.primary [注册]
  ├─ p.tos 「点击注册即表示同意《用户协议》《隐私政策》」(超链接) ← 静态页，v2 评估
  └─ p.footer 「已有账号？」 link 「立即登录」 → /auth/login
```

## 3. 字段

| key | zod | 错误 |
|-----|-----|------|
| email | `z.string().email()` | `auth.register.field.email.invalid` |
| password | `z.string().min(8).regex(/[A-Za-z]/).regex(/\d/)` | `auth.register.field.password.weak` |

## 4. 态

| 态 | 触发 | UI |
|---|------|----|
| `idle` | 默认 | 字段可填；密码强度条实时反馈 |
| `submitting` | 提交 | 按钮 spinner |
| `error` | 4xx | 字段内联或 Toast |

## 5. 交互

`useAsyncAction(submitRegister)`：
1. `POST /v1/auth/register-throttle { email }` 命中 → 429 → Toast `AUTH_REGISTER_RATE_LIMITED`；
2. `supabase.auth.signUp({ email, password, options:{ data:{ locale: i18n.current }}})`；
3. 成功 → 跳 `P-003` `/auth/verify-email-sent?email=<email>`；
4. 失败映射：`email_exists` → 邮箱字段下内联「该邮箱已注册」+ 同行右侧「去登录 / 找回密码」两个 link button；`weak_password` → 密码字段下「密码强度不足」。

## 6. Google

同 P-001 §5 Google 流程；按钮文案「Google 一键注册」实际等价于 OAuth 登录。

## 7. 密码强度条

- 弱：长度 < 8 或仅字母 或仅数字 — 灰色 1/3 条 + 文字「弱」
- 中：≥ 8 + 字母 + 数字 + 长度 ≥ 8 < 12 — 红色 2/3 条 + 文字「可用」
- 强：≥ 12 + 字母 + 数字 + 含特殊字符 — 红色满条 + 文字「强」
- 仅显示用，不阻塞提交（zod 才是阻塞校验）。

## 8. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 新邮箱注册成功 | 跳 `/auth/verify-email-sent?email=...` |
| S2 | 邮箱已存在 | 字段下内联「已注册」+ 跳转链接 |
| S3 | 弱密码（仅字母）| 字段下内联「密码强度不足」 |
| S4 | 节流命中 | Toast「注册尝试过多」 |
| S5 | Google 一键 | 同 P-001 S8 |
| S6 | TOS 链接 | 新页签打开 |

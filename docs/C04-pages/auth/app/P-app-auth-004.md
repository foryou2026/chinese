<!-- TARGET-PATH: docs/C04-pages/auth/app/P-app-auth-004.md -->

# `P-app-auth-004` · OAuth / 邮箱验证回调

> **path**：`/auth/callback` · **角色可见**：任意  
> **R 覆盖**：R-002 / R-011 / R-012  
> **冻结状态**：已冻结 · 2026-05-16

## 1. 用途

- Google OAuth `redirectTo` 落地；
- 邮箱注册验证链接 / 重置密码链接的部分场景（reset 走 `/auth/reset-password` 单独承载，本页不处理 recovery）；
- 仅 `type=signup` / `type=invite` / 无 type（OAuth）经过本页。

## 2. 布局

全屏居中 `<GlassCard>`（中等宽度 480）；首屏只显 Spinner + 文案「正在登录…」。

## 3. 态

| 态 | UI |
|---|----|
| `exchanging` | Spinner + 「正在登录…」 |
| `success` | 即时跳走，不停留（≤200ms 内）|
| `failed` | 错误图标 + 「无法完成登录」+ 错误码文案 + 按钮「重试」/「用邮箱登录」|
| `token-invalid` | 警告图标 + 「链接已过期或已使用」+ 按钮「重新发送验证邮件」(若来源是 signup) / 「重新发起忘记密码」(若来源是 recovery 误入) |

## 4. 流程

```
1. mount → 提取 query (code / access_token / type / error)
2. 若 query.error → failed + 显示 error_description
3. supabase.auth.exchangeCodeForSession(code)
   - 成功 → cookieStorage.set 自动写 cookie → 调 POST /v1/auth/session-register
   - 失败 (otp_expired / token_used) → token-invalid
   - 其他失败 → failed
4. 成功后角色判定：
   - role === 'super_admin' → signOut + 跳 /auth/login?reason=use_admin_entry
   - role === 'user' → 跳 redirect 参数 ?? (first sign-in ? '/onboarding' : '/')
```

## 5. 子状态文案

| 子态 | i18n key | 按钮 |
|-----|----------|------|
| failed | `auth.callback.failed` | 「重试」(reload) /「用邮箱登录」(/auth/login) |
| token-invalid (signup) | `auth.callback.tokenInvalidSignup` | 「重新发送验证邮件」(/auth/verify-email-sent?email=...) |
| token-invalid (recovery) | `auth.callback.tokenInvalidRecovery` | 「重新发起忘记密码」(/auth/forgot) |

## 6. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | OAuth 成功新用户 | exchanging ≤500ms → success → 跳 /onboarding |
| S2 | OAuth 成功老用户 | 跳 / |
| S3 | OAuth provider_error | failed 子态 + 重试按钮 |
| S4 | signup 链接过期 | token-invalid signup 子态 |
| S5 | 直接打开本路径无 query | failed 子态 + 用邮箱登录 |
| S6 | OAuth 但拿到 super_admin role | signOut + 跳 /auth/login?reason=use_admin_entry |

<!-- TARGET-PATH: docs/C03-pages/auth/app/P-auth-005.md -->

# `P-auth-005` · 忘记密码

> **path**：`/auth/forgot` · **角色可见**：未登录  
> **R 覆盖**：R-007  
> **冻结状态**：已冻结 · 2026-05-16

## 1. DOM

```
GlassCard
  ├─ h1 「找回密码」
  ├─ p  「输入注册时使用的邮箱，我们会发送重置链接。」
  ├─ form
  │    ├─ field email (autoFocus)
  │    └─ button.primary [发送重置链接]
  └─ p.footer link 「想起来了？返回登录」 → /auth/login
```

## 2. 态

| 态 | UI |
|---|----|
| `idle` | 字段可填 |
| `submitting` | 按钮 spinner |
| `sent` | 替换内容：icon mail-check + 文案「如果该邮箱已注册，重置链接已发送至 <email>。请查收。」+ 按钮「重新发送 ({{cd}}s)」 + link 「返回登录」 |
| `throttled` | sent 态基础上按钮 cooldown 按后端返 retryAfter |

> **重要安全约定**：即使邮箱不存在，UI **不暴露**——一律切到 `sent` 态。

## 3. 流程

```
1. submit
2. POST /v1/auth/forgot-password-throttle { email }
   - 429 → 显字段下「请稍后再试，{{retryAfter}}s」
3. supabase.auth.resetPasswordForEmail(email, { redirectTo: '<origin>/auth/reset-password' })
4. 不论返回真实是否存在，统一切 `sent` 态
5. cooldown 按 60s（与后端节流一致）
```

## 4. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 有效邮箱 | 切 sent；mailbox 落盘一封 |
| S2 | 不存在的邮箱 | 同 S1（不暴露）；mailbox 不落 |
| S3 | 同 email 60s 内重发 | 字段下「请稍后再试，剩余 NN s」 |
| S4 | 同 IP 1h 内 ≥ 5 次 | 字段下「尝试过多，1h 内最多 5 次」 |
| S5 | sent 态下点重发 | 按钮 cooldown 60s 后 ok |

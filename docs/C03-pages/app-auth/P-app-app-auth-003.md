<!-- TARGET-PATH: docs/C03-pages/app-auth/P-app-app-auth-003.md -->

# `P-app-app-auth-003` · 验证邮件已发送

> **path**：`/auth/verify-email-sent` · **角色可见**：未登录  
> **R 覆盖**：R-001 / R-015  
> **冻结状态**：已冻结 · 2026-05-16

## 1. 布局

`<GlassCard>` 单卡片，居中。

## 2. DOM

```
GlassCard
  ├─ icon mail-check 56px (--brand)
  ├─ h1 「检查你的邮箱」
  ├─ p  「我们刚刚向 <strong>{email}</strong> 发送了验证链接。点击链接完成注册。」
  ├─ p.muted 「没收到？检查垃圾邮件文件夹，或……」
  ├─ button.secondary [重新发送 ({{cd}}s)]   ← SM-app-auth-02 cooldown
  └─ p.footer 「邮箱填错了？」 link 「重新注册」 → /auth/register
```

## 3. 入参

- query `email`：必传；若缺失 → 跳 `/auth/register`；
- 初次进入按钮处 `cooldown` 60s（与注册成功瞬间一致）。

## 4. 态

| 态 | 表现 |
|---|------|
| `sent` | 默认；按钮处于 `cooldown` 60s |
| `resend-throttled` | 倒计时归零后点击若再 429 → Toast「请稍后再试」+ 按钮重新进入 cooldown，时长 = 后端返 retryAfter |

## 5. 交互

- 重发：`POST /v1/auth/register-throttle { email }` → `POST /v1/auth/resend-verify { email }`（内部调 supabase.auth.admin `inviteUserByEmail` 或 `resend` API）；
- 控制台 dev 下额外打印验证链接（mock 邮件）。

## 6. 邮件 mock（dev）

- 写入 `system/.dev/mailbox/{email}-{ts}.eml`；
- 控制台同步 `console.info('[mail] verify link:', url)`；
- 用户可在登录页 ~50% 概率手动复制链接粘贴到浏览器（开发自测）。

## 7. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 注册后进入 | 显「检查你的邮箱」+ 按钮 60s 倒计时 |
| S2 | 倒计时 0 后点重发 | 按钮再次 60s 倒计时 + Toast「已重新发送」 |
| S3 | 60s 内强行点 | 按钮 disabled 无响应 |
| S4 | 缺少 query email | 自动跳 `/auth/register` |
| S5 | 服务端额外节流命中 | Toast「请稍后再试」+ 按钮倒计时按 retryAfter |

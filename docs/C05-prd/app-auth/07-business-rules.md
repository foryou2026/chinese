<!-- TARGET-PATH: docs/C05-prd/app-auth/07-business-rules.md -->

# 07 · 业务规则

> 全部规则均可在 [`B02-permissions/02-auth-flow.md`](../../B02-permissions/02-auth-flow.md) 与 [`05-auth-feature-guideline.md`](../../B02-permissions/05-auth-feature-guideline.md) 中找到落地源；本节按业务语言重排。

## BR-1 · 密码规则

- 最少 8 位；必须含字母 + 数字；
- 与旧密码相同 → 改密不允许；
- 强度条仅 UI 提示，不阻塞提交（zod 才阻塞）；
- bcrypt cost = 10（GoTrue 默认）。

## BR-2 · 邮箱规则

- 注册必须先验证才能首次登入；
- Google OAuth 注册视为已验证；
- 邮箱**不可修改**（v1）；
- 邮箱不暴露存在性（忘密 / 错密一律不区分）。

## BR-3 · 会话规则

- Access Token 1h；Refresh Token 30d 滚动更新；
- 多设备硬上限 3，新登录踢最早；
- 当前会话不被改密 / 找回密码动作踢；
- 主动「全部设备退出」自身也退出。

## BR-4 · 节流 + 锁定

| 接口 | 维度 | 限制 |
|------|------|------|
| `register-throttle` | email | 1h 内 3 次 |
| `register-throttle` | IP | 1h 内 10 次 |
| `login-attempt-record` | email + IP | 15min 内 ≥ 5 次错密 → 锁 15min |
| `forgot-password-throttle` | email | 60s 内 1 次 |
| `forgot-password-throttle` | IP | 1h 内 5 次 |
| `me/password` | session | 5min 内 3 次 |
| 「重发验证邮件」按钮 | 前端 | 60s 倒计时 |

## BR-5 · 禁用规则

- 禁用立即 `admin.signOut global` + 删 `user_sessions`；
- API 层 30s LRU cache 失效兜底；
- 禁用账号登录尝试直接 401，**不进 supabase**；
- 客服解禁后用户需重新登录。

## BR-6 · OAuth 规则

- 只有 Google 一家（v1）；
- 应用端登录页才展示 Google；管理端登录页**不展示**；
- 应用端 OAuth 拿到 `super_admin` role → 视为误用，自动登出 + Toast；
- OAuth 失败 / 用户取消 → 静默返回登录页。

## BR-7 · 重置密码规则

- 链接有效期 1h（GoTrue 默认）；
- 重置成功 → 自动登入本设备 + 踢其他设备；
- 重置流程内的"recovery session"不能调业务接口（只能调 `updateUser`）。

## BR-8 · 资料编辑规则

- `display_name` 1-32 字符；
- `avatar_url` URL 或空；
- `locale` 必须在 `[zh, en, vi, th, id]` 内；
- 修改 `locale` 立即生效 + reload；
- editing 草稿 localStorage 30s 自动存，保存成功立即清。

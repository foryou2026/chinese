<!-- TARGET-PATH: docs/C05-prd/auth/app/05-user-journeys.md -->

# 05 · 用户旅程

> 与 [`C01-requirements/auth/flows/main-flow.md`](../../C01-requirements/auth/flows/main-flow.md) 同源；本节用"故事"语言重述，给非技术干系人看。

## 旅程 1：首次注册

> Linh，越南河内大学生，听同学说"知语"。

1. 打开 `https://zhiyu.app/vi`，落地页底部"开始学"按钮；
2. 跳转 `/auth/register`，看到表单与"Google 一键"按钮；
3. 选用学校 gmail "Google 一键" → 跳 Google 同意页 → 回 `/auth/callback`；
4. ≤500ms 后跳 `/onboarding`（不在本 feature 范围）；
5. **整段不需要打开邮箱**。

## 旅程 2：邮箱注册 → 验证

> Niran，泰国曼谷上班族，习惯用 outlook。

1. `/auth/register` 输 email + password；
2. 提交 → 跳 `/auth/verify-email-sent?email=…`；
3. 打开 outlook → 找到 "知语 - 验证你的邮箱" 邮件 → 点链接；
4. 浏览器打开 `/auth/callback?type=signup&code=…` → ≤1s 跳 `/onboarding`。

## 旅程 3：跨设备使用 + 被踢

> Andi，印尼雅加达自由职业，习惯 4 个设备：手机/平板/家里电脑/咖啡馆电脑。

1. 在 4 台设备依次登入；
2. 第 4 台登入时后端发现 user_sessions > 3，作废最早设备（手机）；
3. 手机当前 access 仍有效 ≤ 1h；
4. 1h 内手机下次刷新或下次 API 调用时 refresh 被拒；
5. 手机自动登出，跳 `/auth/login?reason=kicked` 显 Toast「您的账号在其他设备登录…」。

## 旅程 4：忘记密码

> Linh，3 个月没回来，忘了密码。

1. `/auth/login` → 点"忘记密码？"→ 跳 `/auth/forgot`；
2. 输 email → 提交 → 切到"如果该邮箱已注册，重置链接已发送至…"；
3. 打开邮箱 → 点链接 → `/auth/reset-password?code=…`；
4. 设新密码 → 「保存」→ 切 success → 2s 后自动跳 `/me`；
5. 后台同时把她其他设备（如果之前有登）全部踢掉。

## 旅程 5：账号被禁

> Cesar，被违规社区行为触发管理员禁用。

1. 管理员在 admin-users 点禁用 → 后端全设备登出 + cache 失效；
2. Cesar 的下一次 API 调用立即 401 → 应用全局登出 → 跳 `/auth/login?reason=disabled`；
3. 登录页 Toast「账号已被停用：违反社区规范。如有疑问，请联系客服。」+ 客服链接 `/help/contact`。

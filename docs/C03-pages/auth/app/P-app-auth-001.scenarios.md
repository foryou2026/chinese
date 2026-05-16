<!-- TARGET-PATH: docs/C03-pages/auth/app/P-app-auth-001.scenarios.md -->

# `P-app-auth-001` · 场景验证脚本

| # | 场景 | 输入 | 期望结果 |
|---|------|------|---------|
| S1 | 正常邮密登录 | 有效 email + 正确 password | 跳 `/`；顶栏头像出现 |
| S2 | 邮密登录带 redirect | `?redirect=/me/profile` | 登录后跳 `/me/profile` |
| S3 | 错密 1~4 次 | 错 password | 字段下「邮箱或密码不正确」；按钮恢复 idle |
| S4 | 错密第 5 次 → 锁定 | 错 password | 整页 locked + 15:00 倒计时；按钮 disabled |
| S5 | 锁定期间再提交 | 任意 | 前置 `login-attempt-record` 直接返 429，重置倒计时显示 |
| S6 | 已禁用账号登录 | 禁用账号 | Toast「账号已被停用，原因：…」+ 客服入口；不提交 supabase |
| S7 | 未验证邮箱登录 | 未点验证链接的账号 | Toast「邮箱未验证」+「重发验证邮件」按钮 |
| S8 | Google 一键 | 点 Google | 跳 Google → `/auth/callback` → 跳 `/` |
| S9 | Google 取消 | Google 同意页点取消 | 静默回 `/auth/login`，不弹 Toast |
| S10 | `?reason=kicked` 直接访问 | URL `?reason=kicked` | 顶部 Toast「您的账号在其他设备登录…」+ idle |
| S11 | 已登录访问本页 | 有效 cookie | 自动跳 `/` |
| S12 | 5xx 模拟 | mock signIn 返 500 | Toast「服务异常」+ 字段值保留 |
| S13 | 键盘提交 | Tab 到密码 + Enter | 触发提交（form `onSubmit`） |
| S14 | 主题切换不丢值 | 切换 dark/light | 字段值保留 |
| S15 | 第 4 设备登录 | D4 同账号登录 | 200 + 跳 `/`；早设备下次 refresh 后跳 `/auth/login?reason=kicked` |

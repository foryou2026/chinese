<!-- TARGET-PATH: docs/C03-pages/auth/admin/_input/P-auth-001-desc.md -->

# N01 · 页面描述 · admin 登录页

- 路径 `/admin/auth/login`
- 居中卡片 (max-w 420),深色 admin 主题 (B04 暗色 token)
- 字段:邮箱 / 密码 (无 Google 按钮 / 无 "注册" 链接)
- 底部小字:`忘记密码?` (text-button)
- 错误:内联 + 红字 (`AUTH_INVALID_CREDENTIALS` / `AUTH_LOGIN_RATE_LIMITED` / `AUTH_ACCOUNT_DISABLED` / `AUTH_USE_USER_ENTRY` 全部内联)
- "登录" 主按钮,带 loading 状态
- 不提供"切换为 user 入口"链接 (admin 入口与 app 完全独立)
- 其它 3 页结构类似,本文件仅为登录页样例;其它页结构在对应 P-md 内简述

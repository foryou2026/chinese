<!-- TARGET-PATH: docs/C03-pages/app-auth/_input/P-app-app-auth-001-desc.md -->

# 登录页（P-app-app-auth-001）· N01 用户输入

> 反推回写 · 2026-05-16

- 路径 `/auth/login`，未登录可见，已登录访问自动跳 `/`。
- 表单 3 个字段：邮箱、密码、（可选）"30 天保持登录"开关——**本期不上**（refresh 固定 30d）。
- 主按钮"登录"；副按钮"Google 继续"；底部小字"还没有账号？立即注册"。
- 顶部展示"忘记密码？"链接。
- 节流锁定时按钮显倒计时。
- query `?reason=kicked|disabled|expired|signout` 在进入时映射对应 Toast。
- 5 语 i18n key 前缀 `auth.login.*`。

<!-- TARGET-PATH: docs/C06-prd/auth/app/04-feature-catalog.md -->

# 04 · 功能模块 · auth / **app**

> 单 surface 退化形态。

## Must-Have

- M-auth-app-session(注册/登录/会话/全局登出)
- M-auth-app-cookie(Edge 之间 cookie 交换)
- M-auth-app-throttle(防刷:注册/找回/登录失败)
- M-auth-app-me(资料 / 密码)

## Should-Have

- 邮箱重发验证冷却 UI
- 第三方登录(Google / Apple)— 占位

## Won't-Have

- 短信验证码(成本敏感)
- 2FA(当前仅 admin 端有)

<!-- TARGET-PATH: docs/C05-prd/app-auth/app/04-feature-catalog.md -->

# 04 · 功能模块(MoSCoW)· app-auth / **app**

> 单 surface 退化形态。

## Must-Have

- M-app-auth-session(注册/登录/会话/全局登出)
- M-app-auth-cookie(Edge 之间 cookie 交换)
- M-app-auth-throttle(防刷:注册/找回/登录失败)
- M-app-auth-me(资料 / 密码)

## Should-Have

- 邮箱重发验证冷却 UI
- 第三方登录(Google / Apple)— 占位

## Won't-Have

- 短信验证码(成本敏感)
- 2FA(本期仅 admin 端有)

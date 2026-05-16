<!-- TARGET-PATH: docs/C05-prd/admin-auth/admin/04-feature-catalog.md -->

# 04 · 功能模块(MoSCoW)· admin-auth / **admin**

> 单 surface 退化形态。与 app-auth 完全隔离的 Auth 项目。

## Must-Have

- M-admin-auth-session(登录 / session-status / 全局登出)
- M-admin-auth-password(自助改密 + super 重置)
- M-admin-auth-me

## Should-Have

- 2FA(TOTP) — 由 super 强制开启
- 管理员邀请白名单

## Won't-Have

- 公开注册(永不开)
- 找回密码自助(必须 super 重置)

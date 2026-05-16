<!-- TARGET-PATH: docs/D02-api/app-auth/04-error-codes.md -->

# `app-auth` · 错误码

> 与 [`B02-permissions/03-authz-mechanism §4`](../../B02-permissions/03-authz-mechanism.md) 全局错误码一致。

| code | HTTP | i18n key | 用途 |
|------|------|---------|------|
| `AUTH_NOT_AUTHED` | 401 | `auth.error.notAuthed` | 缺 cookie / token 过期 |
| `AUTH_FORBIDDEN` | 403 | `auth.error.forbidden` | role / 资源不匹配 |
| `AUTH_INVALID_CREDENTIALS` | 401 | `auth.error.invalidCredentials` | 错密 / 错邮箱（统一文案）|
| `AUTH_INVALID_OLD_PASSWORD` | 401 | `auth.error.invalidOldPassword` | 改密时旧密错 |
| `AUTH_EMAIL_TAKEN` | 409 | `auth.error.emailTaken` | 注册邮箱已存在 |
| `AUTH_EMAIL_NOT_VERIFIED` | 401 | `auth.error.emailNotVerified` | 登录前未验邮箱 |
| `AUTH_ACCOUNT_DISABLED` | 401 | `auth.error.accountDisabled` | 账号被禁 |
| `AUTH_USE_ADMIN_ENTRY` | 403 | `auth.error.useAdminEntry` | super_admin 误进应用端 |
| `AUTH_NOT_ADMIN` | 403 | `auth.error.notAdmin` | 普通用户进管理端 |
| `AUTH_LOGIN_RATE_LIMITED` | 429 | `auth.error.loginRateLimited` | 5/15min 锁定 |
| `AUTH_REGISTER_RATE_LIMITED` | 429 | `auth.error.registerRateLimited` | 注册 / 重发邮件节流 |
| `AUTH_FORGOT_RATE_LIMITED` | 429 | `auth.error.forgotRateLimited` | 忘密节流 |
| `AUTH_PASSWORD_CHANGE_RATE_LIMITED` | 429 | `auth.error.passwordChangeRateLimited` | 改密节流 |
| `AUTH_WEAK_PASSWORD` | 400 | `auth.error.weakPassword` | 强度不足 |
| `AUTH_SAME_AS_OLD_PASSWORD` | 400 | `auth.error.sameAsOld` | 新旧一致 |
| `AUTH_OAUTH_FAILED` | 400 | `auth.error.oauthFailed` | OAuth provider 错 |
| `AUTH_TOKEN_INVALID` | 400 | `auth.error.tokenInvalid` | 邮件 / 重置链接过期 |
| `VALIDATION_FAILED` | 400 | `common.error.validation` | zod 字段类 |
| `INVALID_SIGNATURE` | 401 | — (internal) | Hook 签名错 |
| `INVALID_KEY` / `INVALID_TOKEN` | 400 | — | cookie/set Adapter 内部 |

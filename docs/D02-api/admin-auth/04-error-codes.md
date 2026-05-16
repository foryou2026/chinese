<!-- TARGET-PATH: docs/D02-api/admin-auth/04-error-codes.md -->

# D02 · 错误码 · `admin-auth`

> 完全沿用 [`app-auth/04-error-codes.md`](../app-auth/04-error-codes.md);本文仅列 admin 新增 + admin 重映射差异。

## 1. 新增

| 错误码 | HTTP | 触发 | 中文文案 |
|--------|------|------|---------|
| `AUTH_USE_USER_ENTRY` | 403 | admin 登录时检测到 `app_metadata.role !== 'super_admin'` | 请使用用户入口登录 |

## 2. 复用 (前 20 个)

`AUTH_INVALID_CREDENTIALS` / `AUTH_LOGIN_RATE_LIMITED` / `AUTH_ACCOUNT_DISABLED` / `AUTH_TOKEN_INVALID` / `AUTH_INVALID_OLD_PASSWORD` / `AUTH_SAME_AS_OLD_PASSWORD` / `AUTH_WEAK_PASSWORD` / `AUTH_PASSWORD_CHANGE_RATE_LIMITED` / `AUTH_FORGOT_RATE_LIMITED` / `AUTH_NOT_AUTHED` / `AUTH_FORBIDDEN` / `AUTH_SESSION_KICKED` / `VALIDATION_FAILED` / `INVALID_SIGNATURE` / `INVALID_KEY` / `INVALID_TOKEN` 等。

## 3. admin 不会出现

- `AUTH_EMAIL_TAKEN` (无注册)
- `AUTH_EMAIL_NOT_VERIFIED` (seed 必带 confirm)
- `AUTH_REGISTER_RATE_LIMITED` (无注册)
- `AUTH_OAUTH_FAILED` (无 OAuth)

# 接口规范 · account-entry · 共用总览

> **适用系统**：app, admin
> **关联 R-ID**：app(R-auth-005~008,010), admin(R-auth-003~006,009)
> **不做**：表结构(D01)、页面/原型(C02/C03)
> **接口详情**：见 01-password-recovery.md ~ 02-session.md

## 1. 共用接口清单

| API-ID | 方法 | 路径 | 职责(≤10字) | 适用系统 | R-ID | SM 转移 | 详情 |
|--------|------|------|------------|---------|------|--------|------|
| API-common-auth-forgot-password | POST | /api/v1/{sys}/auth/forgot-password | 发送重置验证码 | app, admin | app:R-auth-005, admin:R-auth-003 | 无 | 01 |
| API-common-auth-verify-reset-otp | POST | /api/v1/{sys}/auth/forgot-password/verify | 验证重置OTP | app, admin | app:R-auth-005, admin:R-auth-003 | 无 | 01 |
| API-common-auth-reset-password | POST | /api/v1/{sys}/auth/reset-password | 重置密码 | app, admin | app:R-auth-006,010, admin:R-auth-004,009 | 无 | 01 |
| API-common-auth-logout | POST | /api/v1/{sys}/auth/logout | 退出登录 | app, admin | app:R-auth-008, admin:R-auth-006 | app:TR-010, admin:TR-007 | 02 |

> API-ID：`API-common-auth-<verb>-<noun>`
> 路径使用 `{sys}` 占位符，实际挂载到 `/api/v1/app/` 和 `/api/v1/admin/` 下。

## 2. 共用错误码

| code | HTTP | 含义 | 文案 | 触发接口 |
|------|------|------|------|---------|
| 40001 | 400 | 参数校验失败 | 请检查输入内容 | forgot-password, reset-password |
| 40101 | 401 | Token无效 | 认证失败 | reset-password, logout |
| 40102 | 401 | 验证码过期 | 验证码已过期，请重新发送 | verify-reset-otp |
| 40103 | 401 | 验证码错误 | 验证码错误 | verify-reset-otp |
| 42901 | 429 | 请求过于频繁 | 请求过于频繁 | forgot-password |

## 3. 并发与幂等

无

## 99. 待确认问题

无

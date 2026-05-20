<!-- TARGET-PATH: docs/C02-ia-interaction/auth/account-entry/04-pages.md -->

# 页面清单 · account-entry

> **阶段**：C02-IN · **模块**：`auth` · **功能**：`account-entry`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端页面（4 页）

| page-id | 名称 | 类型 | 角色 | M-ID | 关联 R-ID | 主要 4 态 |
|---------|------|------|------|------|-----------|----------|
| P-app-auth-001 | 登录 | 表单页 | 未登录 | M-auth-app-01 | R-auth-003/004/005/006/013 | idle · submitting · error · kicked-back |
| P-app-auth-002 | 注册 | 表单页 | 未登录 | M-auth-app-01 | R-auth-001/002/014 | idle · submitting · error |
| P-app-auth-003 | 验证邮件已发送 | 信息页 | 未登录 | M-auth-app-01 | R-auth-001/015 | sent · resend-throttled |
| P-app-auth-004 | OAuth / 邮箱验证回调 | 过场页 | 任意 | M-auth-app-01 | R-auth-002/012 | exchanging · success · failed · token-invalid |

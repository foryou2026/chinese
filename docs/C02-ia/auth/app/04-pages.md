<!-- TARGET-PATH: docs/C02-ia/auth/app/04-pages.md -->

# `auth` · 页面清单

> **冻结状态**：已冻结 · 2026-05-16  
> 路径见 [`D02-api/auth/app/01-routes-delta.md`](../../D02-api/auth/app/01-routes-delta.md)（本文件按框架约定**不**含 URL，只列 page-id 与归属 module）。

| page-id | 名称 | 类型 | 角色 | 模块 M | 关联 R-ID | 主要 4 态 |
|---------|------|------|------|--------|-----------|----------|
| `P-auth-001` | 登录 | 表单页 | 未登录 | M-01 | R-003 / 004 / 005 / 006 / 011 / 013 | idle · submitting · error · kicked-back |
| `P-auth-002` | 注册 | 表单页 | 未登录 | M-01 | R-001 / 002 / 014 | idle · submitting · error |
| `P-auth-003` | 验证邮件已发送 | 信息页 | 未登录 | M-01 | R-001 / 015 | sent · resend-throttled |
| `P-auth-004` | OAuth / 邮箱验证回调 | 过场页 | 任意 | M-01 | R-002 / 011 / 012 | exchanging · success · failed · token-invalid |
| `P-auth-005` | 忘记密码 | 表单页 | 未登录 | M-02 | R-007 | idle · submitting · sent · throttled |
| `P-auth-006` | 重置密码 | 表单页 | 未登录（recovery session）| M-02 | R-007 / 012 | idle · submitting · success · token-invalid |
| `P-auth-007` | 个人中心首页 | 列表入口页 | 用户 | M-03 | R-008 | profile-view · loading · error |
| `P-auth-008` | 账号与安全 | 表单页 | 用户 | M-03 | R-009 / 010 | view · changing-password · done |
| `P-auth-009` | 编辑资料 | 表单页 | 用户 | M-03 | R-008 | view · editing · saving |

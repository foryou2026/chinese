<!-- TARGET-PATH: docs/C02-ia-interaction/auth/account-profile/04-pages.md -->

# 页面清单 · account-profile

> **阶段**：C02-IN · **模块**：`auth` · **功能**：`account-profile`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端页面（3 页）

| page-id | 名称 | 类型 | 角色 | M-ID | 关联 R-ID | 主要 4 态 |
|---------|------|------|------|------|-----------|----------|
| P-app-auth-007 | 个人中心首页 | 列表入口页 | 用户 | M-auth-app-03 | R-auth-011 | profile-view · loading · error |
| P-app-auth-008 | 账号与安全 | 表单页 | 用户 | M-auth-app-03 | R-auth-008/009 | view · changing-password · done |
| P-app-auth-009 | 编辑资料 | 表单页 | 用户 | M-auth-app-03 | R-auth-011 | view · editing · saving |

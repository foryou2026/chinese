<!-- TARGET-PATH: docs/C02-ia-interaction/auth/04-pages.md -->

# 页面清单

> **阶段**：C02-IN · **功能**：`auth`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端（9 页）

| page-id | 名称 | 类型 | 角色 | 模块 M | 关联 R-ID | 主要 4 态 |
|---------|------|------|------|--------|-----------|----------|
| P-app-auth-001 | 登录 | 表单页 | 未登录 | M-auth-app-01 | R-auth-003/004/005/006/011/013 | idle · submitting · error · kicked-back |
| P-app-auth-002 | 注册 | 表单页 | 未登录 | M-auth-app-01 | R-auth-001/002/014 | idle · submitting · error |
| P-app-auth-003 | 验证邮件已发送 | 信息页 | 未登录 | M-auth-app-01 | R-auth-001/015 | sent · resend-throttled |
| P-app-auth-004 | OAuth / 邮箱验证回调 | 过场页 | 任意 | M-auth-app-01 | R-auth-002/011/012 | exchanging · success · failed · token-invalid |
| P-app-auth-005 | 忘记密码 | 表单页 | 未登录 | M-auth-app-02 | R-auth-007 | idle · submitting · sent · throttled |
| P-app-auth-006 | 重置密码 | 表单页 | 未登录（recovery session）| M-auth-app-02 | R-auth-007/012 | idle · submitting · success · token-invalid |
| P-app-auth-007 | 个人中心首页 | 列表入口页 | 用户 | M-auth-app-03 | R-auth-008 | profile-view · loading · error |
| P-app-auth-008 | 账号与安全 | 表单页 | 用户 | M-auth-app-03 | R-auth-009/010 | view · changing-password · done |
| P-app-auth-009 | 编辑资料 | 表单页 | 用户 | M-auth-app-03 | R-auth-008 | view · editing · saving |

---

## admin 端（4 页）

| page-id | 名称 | 主要状态 | 守卫 | 覆盖 R-ID |
|---------|------|---------|------|-----------|
| P-admin-auth-001 | 登录 | idle / submitting / error / not-admin / locked / kicked-back | 公开 | R-auth-001/002/004/005/009 |
| P-admin-auth-002 | 忘密 | idle / submitting / sent / throttled | 公开 | R-auth-006 |
| P-admin-auth-003 | 重置密码 | exchanging / idle / submitting / success / token-invalid | 公开 | R-auth-006 |
| P-admin-auth-004 | 账号与安全 | view / changing-password / done | admin | R-auth-003/007/008 |

> app 端 9 页 + admin 端 4 页 = 共 13 页。
> admin 端登录 / 忘密 / 重置密码（P-001~003）使用居中 GlassCard 布局；P-admin-auth-004 嵌在 admin 主框架内（左侧导航 + 右上头像）。

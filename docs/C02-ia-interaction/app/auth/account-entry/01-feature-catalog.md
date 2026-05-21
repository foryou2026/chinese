# 功能模块清单

| M-ID | 模块名 | 功能 | 职责 | 主要角色 | 关联 R-ID |
|------|--------|------|------|---------|----------|
| M-auth-001 | 账号入口 | 邮箱注册 | 收集邮箱密码创建账号 | ROLE-USER | R-auth-001, R-auth-010, R-auth-011 |
| M-auth-001 | 账号入口 | 邮箱登录 | 邮箱密码认证 | ROLE-USER | R-auth-002, R-auth-004, R-auth-011 |
| M-auth-001 | 账号入口 | Google 快捷登录 | OAuth 一键登录/自动注册 | ROLE-USER | R-auth-003, R-auth-012 |
| M-auth-001 | 账号入口 | 密码找回 | 邮件重置密码 | ROLE-USER | R-auth-005, R-auth-006, R-auth-010 |
| M-auth-001 | 账号入口 | 密码修改 | 已登录修改/设置密码 | ROLE-USER | R-auth-007, R-auth-010, R-auth-014 |
| M-auth-001 | 账号入口 | 会话管理 | 退出登录、Token 过期 | ROLE-USER | R-auth-008, R-auth-009 |

## 模块×角色矩阵

| 模块 | ROLE-USER |
|------|-----------|
| M-auth-001 账号入口 | 全部功能 |

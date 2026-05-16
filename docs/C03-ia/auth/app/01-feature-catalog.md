<!-- TARGET-PATH: docs/C03-ia/auth/app/01-feature-catalog.md -->

# `auth` · 功能模块清单

> **冻结状态**：已冻结 · 2026-05-16

| M-ID | 名称 | 一句话职责 | 主要角色 | 关联 R-ID |
|------|------|-----------|---------|----------|
| M-auth-app-01 | `account-entry`（账号入口）| 登录 / 注册 / OAuth 入口与回调 | 未登录访客 / 用户 | R-001 / R-002 / R-003 / R-004 / R-005 / R-006 / R-011 / R-013 / R-014 / R-015 |
| M-auth-app-02 | `account-recovery`（账号找回）| 忘记密码 / 重置密码 / 链接失效兜底 | 未登录访客 / 用户 | R-007 / R-012 |
| M-auth-app-03 | `account-profile`（个人中心）| 查看 / 修改 profile / 修改密码 / 退出 | 用户 | R-008 / R-009 / R-010 |

每个 M 模块对应的 page-id 详见 [04-pages.md](./04-pages.md)。

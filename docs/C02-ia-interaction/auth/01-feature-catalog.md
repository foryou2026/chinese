<!-- TARGET-PATH: docs/C02-ia-interaction/auth/01-feature-catalog.md -->

# 功能模块清单

> **阶段**：C02-IN · **功能**：`auth`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端（M-auth-app-NN）

| M-ID | 名称 | 一句话职责 | 主要角色 | 关联 R-ID |
|------|------|-----------|---------|----------|
| M-auth-app-01 | `account-entry`（账号入口）| 登录 / 注册 / OAuth 入口与回调 | 未登录访客 / 用户 | R-auth-001~006、011、013~015 |
| M-auth-app-02 | `account-recovery`（账号找回）| 忘记密码 / 重置密码 / 链接失效兜底 | 未登录访客 / 用户 | R-auth-007、012 |
| M-auth-app-03 | `account-profile`（个人中心）| 查看 / 修改 profile / 修改密码 / 退出 | 用户 | R-auth-008~010 |

每个 M 模块对应的 page-id 详见 [04-pages.md](./04-pages.md)。

---

## admin 端（M-auth-admin-NN）

| M-ID | slug | 说明 | 覆盖 R-ID |
|------|------|------|-----------|
| M-auth-admin-01 | `admin-entry` | 登录 / 忘密 / 重置三件套 | R-auth-001/002/004/005/006/009 |
| M-auth-admin-02 | `admin-account` | `/admin/me` 改密 / 退出 / 多设备 | R-auth-003/007/008 |

> R-auth-010（seed 账号创建）不属任何 M，走运维脚本流程。

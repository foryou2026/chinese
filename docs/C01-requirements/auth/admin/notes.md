<!-- TARGET-PATH: docs/C01-requirements/auth/admin/notes.md -->

# `auth` · admin 端补充说明

> **阶段**：C01-R · **feature**：`auth` · **surface**：`admin`
> **作用**：仅承载 admin 端独有补充；统一基线见 [`../baseline.md`](../baseline.md)。

---

## 1. admin 端专属 R-ID

| R-ID | 重点 |
|------|------|
| `R-auth-025` | 管理员账号 seed 创建（无 UI；运维脚本）|

## 2. admin 端对共有 R-ID 的强化

| R-ID | admin 行为 |
|------|------------|
| `R-auth-003` | **强制** `super_admin` 角色守卫：非超管立即 `signOut()` 并回 `AUTH_USE_USER_ENTRY` 错误码 |
| `R-auth-005` | `user_sessions.surface='admin'` 维度独立计数（与 app 互不影响）|
| `R-auth-006` | 同 app；运维可手工 `is_active=false` disable 异常管理员 |
| `R-auth-007` | 路径走 `/admin/auth/forgot` → `/admin/auth/reset-password` |
| `R-auth-008` | 复用 `POST /api/admin/me/password`（与 app 同密码规则：8+ 字母 + 数字）|
| `R-auth-010` | 守卫跳 `/admin/auth/login?redirect=...`；非超管 → `/admin/auth/login?error=not_admin` |

## 3. admin 不做（在基线已声明，再次提示运维注意）

- 无注册页 / 无 Google OAuth / 无邮箱验证页 / 无头像 / 无 self-delete / 无改邮箱 UI
- 自助邀请 UI、管理员列表、改他人密码：均属未来 `admin-users` feature

## 4. 流程文件

- 主流程：[`../flows/admin-main-flow.md`](../flows/admin-main-flow.md)
- 异常流：[`../flows/admin-exception-flow.md`](../flows/admin-exception-flow.md)
- C02 admin：[`../../C02-ia/auth/admin/`](../../C02-ia/auth/admin/)

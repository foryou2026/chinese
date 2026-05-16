<!-- TARGET-PATH: docs/C01-requirements/auth/app/notes.md -->

# `auth` · app 端补充说明

> **阶段**：C01-R · **feature**：`auth` · **surface**：`app`
> **作用**：仅承载 app 端独有补充；统一基线见 [`../baseline.md`](../baseline.md)。

---

## 1. app 端专属 R-ID

| R-ID | 重点 |
|------|------|
| `R-auth-001` | 邮箱 + 密码注册 → 邮箱验证 → 首次登入 |
| `R-auth-002` | Google OAuth 一键注册即登录 |
| `R-auth-011` | profile 编辑（头像/显示名/偏好语言）|
| `R-auth-012` | OAuth 回调失败/取消 → 静默回登录页 |
| `R-auth-013` | 验证 / 重置链接过期 → 「链接已过期」页 |
| `R-auth-014` | 注册撞已存在邮箱 → 友好提示；找回密码不暴露邮箱存在性 |
| `R-auth-015` | 「重新发送验证邮件」60s 倒计时 + 60s/1h 双层节流 |

## 2. app 端共有 R-ID 的差异

| R-ID | app 行为 |
|------|----------|
| `R-auth-003` | 不做角色守卫（任何 `profiles.role` 均可登录）|
| `R-auth-005` | `user_sessions.surface='app'` 维度独立计数 |
| `R-auth-010` | 守卫跳 `/auth/login?redirect=...`；无角色校验 |
| `R-auth-008` / `009` | 走 `POST /api/app/me/password` 与 `POST /api/app/me/sign-out` |

## 3. 流程文件

- 主流程：[`../flows/app-main-flow.md`](../flows/app-main-flow.md)
- 异常流：[`../flows/app-exception-flow.md`](../flows/app-exception-flow.md)
- C02 app：[`../../C02-ia/auth/app/`](../../C02-ia/auth/app/)

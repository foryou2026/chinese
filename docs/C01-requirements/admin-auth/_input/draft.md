<!-- TARGET-PATH: docs/C01-requirements/admin-auth/_input/draft.md -->

# R01 用户输入 · `admin-auth` 需求初稿

> 由 PM 反向整理 · 2026-05-16
> 来源:`B02-permissions/05-auth-feature-guideline.md` / `B01-architecture/08-surfaces.md`

---

## 1. 一句话

后台管理员的"登录 / 找回密码 / 改密 / 退出"——**没有注册入口、没有 Google、没有自助邀请 UI**;新管理员账号通过运维侧 SQL seed (`scripts/db/seed-super-admin.sh`) 创建。

## 2. 边界

| 项 | 范围 |
|----|------|
| ✅ in | 登录 / 忘记密码 / 重置密码 / 改密 / 退出 / 守卫拦截 / 多设备 3 上限 |
| ❌ out | 注册页 / Google OAuth / 邮箱验证 (seed 时已 `email_confirmed_at`) / 头像 / 显示名编辑 / 自助删除 / 自助邀请 / 管理员列表页 / 2FA |
| 🔜 v2+ | admin 自助邀请 UI · TOTP · IP 白名单 · SSO (Workspace) |

## 3. 与 app-auth 的关系

- **后端 service 100% 复用**:所有 `/v1/auth/*` handler 同时在 `/admin/v1/auth/*` 同构暴露,只多套一道 `requireRole('super_admin')`;
- **前端独立**:`web-admin` 自带 4 页登录态界面,设计语言/i18n 与 app 端区分 (深色为主、信息密度更高);
- **数据 0 新增**:`auth.users` / `profiles` (`role='super_admin'`) / `user_sessions` (`surface='admin'`) / `auth_login_attempts` / `audit_logs` 全部复用。

## 4. 新管理员创建流程 (v1 运维流程,非产品流程)

```
运维拿到 SUPER_ADMIN_EMAIL + SUPER_ADMIN_PWD →
  docker compose run --rm db-migrate /scripts/db/seed-super-admin.sh \
    SUPER_ADMIN_EMAIL=x@y.com SUPER_ADMIN_PWD=...
→ seed.sql 调 auth.users INSERT + email_confirmed_at = now() + profiles.role='super_admin'
→ 该管理员可立即在 /admin/auth/login 登录
```

> **强制约束**:本期管理后台**永不**暴露"邀请新管理员"按钮/API;若 v2 实现,必须先升级 `01-roles.md` 加入 `admin_inviter` 子角色并经审批。

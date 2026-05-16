<!-- TARGET-PATH: docs/D01-data/admin-auth/01-entities-delta.md -->

# D01 · 实体差异 · `admin-auth`

> 全部表复用 [`D01-data/app-auth/02-entities/`](../app-auth/02-entities/)。本文仅列 admin 视角的字段值/约束差异。

## 1. `auth.users`

| 字段 | admin 取值 | 说明 |
|------|-----------|------|
| `email_confirmed_at` | seed 时强制 `now()` | admin 不走邮箱验证 |
| `raw_app_metadata.role` | `'super_admin'` | 由 seed 注入;运行时严禁产品代码修改 |
| `raw_app_metadata.provider` | `'email'` | admin 端无 Google |

## 2. `public.profiles`

| 字段 | admin 取值 |
|------|-----------|
| `role` | `'super_admin'` |
| `is_disabled` | 仅运维 SQL 可设 |
| `display_name` | seed 默认 "Super Admin";v1 不允许 admin UI 修改 |
| `avatar_url` | NULL (admin 不展示头像) |
| `locale` | 由超管在浏览器切换;不写库 (v1 admin 不持久化语言) |

## 3. `public.user_sessions`

| 字段 | admin 取值 |
|------|-----------|
| `surface` | `'admin'` |
| 上限 | 3 (与 app 独立计数) |

## 4. `public.auth_login_attempts`

无差异;共表;`surface` 字段值 `'admin'` 区分。

## 5. `public.audit_logs`

| 字段 | admin 取值 |
|------|-----------|
| `actor_role` | `'super_admin'` |
| `event` | 见 [`D02-api/admin-auth/06-events.md`](../../D02-api/admin-auth/06-events.md) |

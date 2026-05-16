<!-- TARGET-PATH: docs/D01-data/app-auth/02-entities/profiles.md -->

# Entity · `public.profiles`

- 完整 DDL 见 [`B02-permissions/04-data-model §2.1`](../../../B02-permissions/04-data-model.md)。
- 本 feature 用到的字段：

| 字段 | 类型 | 默认 | 本 feature 写 / 读 |
|------|------|------|-------------------|
| `id` | uuid PK & FK→auth.users.id | — | 仅读 |
| `display_name` | text NOT NULL | (注册时 = email 前段) | 用户改资料 写 |
| `avatar_url` | text | NULL | 用户改资料 / OAuth 自动填 写 |
| `locale` | text NOT NULL | 'zh' | 用户改资料 写 |
| `role` | text NOT NULL | 'user' | 仅 Hook 注册时写；客户端永不可写 |
| `is_disabled` | bool NOT NULL | false | 仅 admin 写；本 feature 仅读（兜底校验）|
| `disabled_reason` | text | NULL | 仅 admin 写；本 feature 读（Toast 文案） |
| `created_at` / `updated_at` | timestamptz | now() | trigger 维护 |

- 写入入口：
  - **before_user_created Hook** (`/internal/auth-hook`) → INSERT
  - **DB Trigger `handle_new_user`** → INSERT（兜底，Hook 失败时）
  - **PATCH /v1/me** → UPDATE display_name / avatar_url / locale 白名单

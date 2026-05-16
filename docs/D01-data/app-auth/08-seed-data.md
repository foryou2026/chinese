<!-- TARGET-PATH: docs/D01-data/app-auth/08-seed-data.md -->

# `app-auth` · 种子数据

> 真正的 SQL 见 [`system/supabase/seed.sql`](../../../system/supabase/seed.sql)。

## 1. super_admin 账号

- 来源：[`grules/G3-权限与认证规范/05-注册流程.md §3`](../../../grules/G3-权限与认证规范/05-注册流程.md)；
- 通过 `supabase.auth.admin.createUser({email, password, email_confirm:true})` + `INSERT INTO profiles (id, role) VALUES (?, 'super_admin')`；
- 详细 seed 步骤 + 默认账号详 [`B02-permissions/05-auth-feature-guideline §6`](../../B02-permissions/05-auth-feature-guideline.md)。

## 2. 测试用 user 账号（dev only）

| email | password | role | 用途 |
|-------|----------|------|------|
| `dev.user1@example.com` | `Devuser1!` | user | 普通 dev 自测 |
| `dev.user2@example.com` | `Devuser2!` | user | 多设备测试 |
| `dev.disabled@example.com` | `Devdis1!` | user (is_disabled=true) | 禁用兜底测试 |

> 仅在 `NODE_ENV !== 'production'` 时通过 `scripts/db/seed-dev.ts` 写入。

## 3. dev mailbox 占位

- `system/.dev/mailbox/.gitkeep` 必须存在，确保目录被打包到 docker；
- dev 注册产生的 `.eml` 仅本地，**不**进版本控制（`.gitignore` 已忽略）。

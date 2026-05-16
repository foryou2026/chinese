<!-- TARGET-PATH: docs/D01-data/app-auth/02-entities/auth-users.md -->

# Entity · `auth.users`（Supabase 内置）

- 完整定义见 [`B02-permissions/04-data-model §1.1`](../../../B02-permissions/04-data-model.md)。
- 本 feature 仅 **只读** 该表 + 通过 `supabase.auth.admin.*` 间接写：
  - `signUp` / `signInWithPassword` / `signInWithOAuth` / `signOut` / `admin.updateUserById` / `admin.deleteUser`（v2）/ `resetPasswordForEmail`。
- **禁止**直接 `UPDATE auth.users`（绕过 GoTrue 会破坏 password hash 一致性）。
- 关键字段：`id`、`email`、`encrypted_password`、`email_confirmed_at`、`last_sign_in_at`。

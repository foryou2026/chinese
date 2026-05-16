<!-- TARGET-PATH: docs/D01-data/app-auth/_input/data-rules.md -->

# `app-auth` · D01 数据规则输入

> 反推回写 · 2026-05-16

- 本 feature **不新增**任何表 —— 全部沿用 [`B02-permissions/04-data-model.md`](../../B02-permissions/04-data-model.md) 5 张表：
  `auth.users`（Supabase）、`public.profiles`、`public.user_sessions`、`public.auth_login_attempts`、`public.audit_logs`。
- 写入路径必须保证 `before_user_created` Hook 与 `handle_new_user` 触发器**只有一处真正插入** profiles（Hook 优先，触发器兜底）。
- 改资料只允许更新 `display_name / avatar_url / locale`；`role` 等敏感字段在 API 层 zod whitelist。
- 节流计数在 Redis（kv 后端），不入 PG。

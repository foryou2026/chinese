<!-- TARGET-PATH: docs/D01-data/admin-auth/_input/data-rules.md -->

# D01 用户输入 · 数据规则 · `admin-auth`

- **0 新增表**:`auth.users` / `profiles` / `user_sessions` / `auth_login_attempts` / `audit_logs` 全部复用
- `profiles.role` 取值 `'super_admin'` (由 seed 设置;运行时不允许产品代码修改 role)
- `user_sessions.surface = 'admin'` (本 feature 独立的会话桶)
- `audit_logs.actor_role = 'super_admin'` (由 jwt 派生写入)
- 不引入 admin 专属表

<!-- TARGET-PATH: docs/D01-data/admin-auth/03-seed.md -->

# D01 · seed 流程 · `admin-auth`

## 1. 命令

```bash
# 容器内
docker compose run --rm db-migrate /scripts/db/seed-super-admin.sh \
  SUPER_ADMIN_EMAIL=ops@zhiyu.app \
  SUPER_ADMIN_PWD='<random-strong>'
```

## 2. 脚本路径

- `system/scripts/db/seed-super-admin.sh` (容器内入口)
- `system/supabase/seed.sql` (SQL 主体)

## 3. SQL 关键步骤 (引自 seed.sql)

1. `auth.users` INSERT (或 UPDATE);
2. 强制 `email_confirmed_at = now()`;
3. 强制 `raw_app_meta_data = {"role":"super_admin","display_name":"Super Admin","locale":"zh"}`;
4. `profiles` UPDATE `role='super_admin', is_active=true, updated_at=now()`;
5. 输出 NOTICE。

## 4. Runbook 约束

- seed 后**必须**让超管登录立即改密 (避免运维侧明文密码长期可用)
- 同一邮箱重复 seed 不报错 (UPSERT 语义),但密码不会被自动覆盖 (脚本会跳过)
- seed 不写 audit_logs (系统初始化,无 actor)

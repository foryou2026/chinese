# user_profiles

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-auth-001, R-auth-003, R-auth-012, R-auth-014 |
| 业务定义 | 用户扩展资料 |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | 无 | 是 | 主键=auth.users.id | 引用 auth.users(id) |
| display_name | text | 否 | null | 否 | 显示名称 | 长度≤50 |
| avatar_url | text | 否 | null | 否 | 头像地址 | 合法URL或null |
| auth_provider | text | 是 | 'email' | 否 | 注册来源 | 枚举:auth_provider_enum |
| has_password | boolean | 是 | true | 否 | 是否有密码 | Google用户为false |
| deleted_at | timestamptz | 否 | null | 否 | 注销时间 | 注销后保留7天 |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - id 不使用 gen_random_uuid()，取 auth.users.id 的值。
> - 软删除策略：用户注销时设 deleted_at=now()，7天后由 cron 硬删除（同步删除 auth.users）。
> - 默认查询追加 `WHERE deleted_at IS NULL`。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| auth.users | 1:1 | id | CASCADE |

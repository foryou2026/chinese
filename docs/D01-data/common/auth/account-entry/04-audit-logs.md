# audit_logs

| 项 | 值 |
|----|-----|
| 关联 R-ID | C01 §6 审计要求 |
| 业务定义 | 认证操作审计日志 |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| user_id | uuid | 否 | null | 否 | 操作用户 | 失败登录可为null |
| email | text | 否 | null | 否 | 操作邮箱 | 无 |
| system_id | text | 是 | 无 | 否 | 所属系统 | 枚举:system_enum |
| action | text | 是 | 无 | 否 | 操作类型 | 枚举:audit_action_enum |
| ip_address | text | 否 | null | 否 | 客户端IP | 无 |
| user_agent | text | 否 | null | 否 | 客户端UA | 无 |
| metadata | jsonb | 否 | null | 否 | 附加信息 | 无 |

> - 不做软删除（B01 规定审计表不做软删除）。
> - 仅携带 id + created_at，不携带 updated_at/created_by/updated_by。
> - 保留 90 天（C01 §6），由 cron 硬删除 `created_at < now() - interval '90 days'`。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| auth.users | N:1 | user_id | SET NULL |

> user_id 使用 SET NULL 而非 CASCADE，确保用户删除后审计记录留存。

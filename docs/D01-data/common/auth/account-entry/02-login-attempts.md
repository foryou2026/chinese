# login_attempts

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-auth-004(app), R-auth-002(admin) |
| 业务定义 | 登录失败计数与锁定 |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| email | text | 是 | 无 | 否 | 尝试登录邮箱 | 邮箱格式 |
| system_id | text | 是 | 无 | 否 | 所属系统 | 枚举:system_enum |
| consecutive_failures | integer | 是 | 0 | 否 | 连续失败次数 | ≥0 |
| last_failure_at | timestamptz | 否 | null | 否 | 末次失败时间 | 无 |
| locked_until | timestamptz | 否 | null | 否 | 锁定截止时间 | 无 |

> - UNIQUE(email, system_id)。
> - 不使用软删除。成功登录后重置 consecutive_failures=0 并清空 locked_until。
> - 以 email 为键而非 user_id，因为登录失败时账号可能不存在。

## 关系

无外键关联。

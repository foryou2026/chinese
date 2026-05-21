# user_sessions

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-auth-016(app), R-auth-011(admin) |
| 业务定义 | 活跃会话追踪 |
| 状态机 | SM-auth-001 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| user_id | uuid | 是 | 无 | 否 | 所属用户 | 引用 auth.users(id) |
| system_id | text | 是 | 无 | 否 | 所属系统 | 枚举:system_enum |
| session_token_hash | text | 是 | 无 | 是 | 会话标识哈希 | 非空 |
| device_info | text | 否 | null | 否 | 设备信息 | 长度≤500 |
| ip_address | text | 否 | null | 否 | 登录IP | 无 |
| logged_in_at | timestamptz | 是 | now() | 否 | 登录时间 | 无 |
| last_active_at | timestamptz | 是 | now() | 否 | 末次活跃时间 | 无 |
| is_active | boolean | 是 | true | 否 | 是否活跃 | 无 |

> - 不使用软删除。会话失效时设 is_active=false。
> - session_token_hash 使用 SHA-256 哈希 Supabase refresh_token。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| auth.users | N:1 | user_id | CASCADE |

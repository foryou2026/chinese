# 枚举定义

> 与 C02 SM 对齐。

## auth_provider_enum

| 值 | 中文名 | 默认 |
|-----|--------|------|
| email | 邮箱注册 | ✅ |
| google | Google登录 | |

## system_enum

| 值 | 中文名 | 默认 |
|-----|--------|------|
| app | 用户系统 | |
| admin | 管理系统 | |

## audit_action_enum

| 值 | 中文名 | 默认 |
|-----|--------|------|
| register | 注册 | |
| login | 登录成功 | |
| login_failed | 登录失败 | |
| login_locked | 账号锁定 | |
| google_login | Google登录 | |
| logout | 退出登录 | |
| password_change | 修改密码 | |
| password_reset | 重置密码 | |
| password_set | 设置密码 | |
| session_revoked | 会话踢下线 | |

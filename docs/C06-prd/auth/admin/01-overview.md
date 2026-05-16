<!-- TARGET-PATH: docs/C06-prd/auth/admin/01-overview.md -->

# C06 · 01 总览 · `auth`

## 1. 一句话

后台超管的"登录 / 找回密码 / 改密 / 退出"账号生命周期最小集;**邀请制 = 运维 SQL seed,无产品 UI**。

## 2. 范围

- in:邮密登录 + 角色守卫 + Cookie 会话 + CSRF + 多设备 3 上限 + 锁定/禁用 + 忘密/重置 + 改密 + 退出 (本设备 / 全部)
- out:注册 / Google / 邮箱验证页 / 头像 / 显示名 / 自助删除 / 自助邀请 / 管理员列表 / 改他人密 / 2FA
- v2+:自助邀请 UI / TOTP / IP 白名单 / SSO / "我的设备" 页

## 3. 关键指标 (v1 不强制埋点)

| 指标 | 期望 |
|------|------|
| 超管登录失败率 | < 5% (失败多 = 密码遗忘或盗号尝试) |
| 锁定触发次数 / 周 | 监控 + 周报;> 3 → 调查 |
| 重置邮件触发次数 / 月 | 监控 |
| 第 4 设备踢出次数 / 月 | 监控;> 0 即调查 (超管账号被多人共用?) |

## 4. 与其它 feature 的关系

| 关系 | feature |
|------|---------|
| 复用 backend service | `auth` (handler 100% 同源) |
| 共享数据表 | B02-04 全部 5 表 |
| 不依赖 | `user-account`(无 onboarding) · `discover-china` / `course` (内容) |
| 守卫消费者 | `admin-users` / `admin-discover` / `admin-courses` / `admin-novels` (全部 admin 业务 feature) |

<!-- TARGET-PATH: docs/D01-data/app-auth/05-calculations.md -->

# `app-auth` · 计算字段

| 字段 | 输入 | 公式 | 用途 |
|------|------|------|------|
| `email_masked` | profiles.email | `email[0..2] + '***@' + domain` | `/me` 展示，避免泄漏完整邮箱 |
| `password_strength` | new_password | 见下方分级 | UI 强度条 |
| `lockout_remaining_seconds` | `auth_login_attempts.created_at` 最旧的失败时间 | `15*60 - (now - oldest_failed_at)` | 登录页倒计时显示 |
| `display_name_initial` | display_name | `display_name.trim()[0].toUpperCase()` | 头像兜底（无 avatar_url 时显示首字符）|

## password_strength 分级

| 等级 | 条件 |
|------|------|
| weak | length < 8 OR 仅字母 OR 仅数字 |
| medium | length ≥ 8 AND 含字母 AND 含数字 AND length < 12 |
| strong | length ≥ 12 AND 含字母 AND 含数字 AND 含特殊字符 |

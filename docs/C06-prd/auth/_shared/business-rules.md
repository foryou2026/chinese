<!-- TARGET-PATH: docs/C06-prd/auth/_shared/business-rules.md -->

# auth · `_shared/business-rules.md` · 跨端业务规则

> **作用**：auth feature 中**两端必须同时遵守**的业务规则；端独有规则在 `app/07-business-rules.md` / `admin/07-business-rules.md`。
> **冻结**：2026-05-17

---

## BR-auth-shared-01 · 密码复杂度

- 长度 ≥ 8、≤ 128
- 必须含字母 + 数字（特殊字符可选）
- 拒绝常见弱密表（top-10000，前端 + 后端双校验）
- 历史密码不强制不复用（仅 admin 端运维侧建议）

## BR-auth-shared-02 · 锁定与禁用

| 触发 | 行为 | 解除 |
|------|------|------|
| 同 (user_id, ip) 15min 内错密 ≥ 5 | 该账号锁定 15min（两端通锁） | 15min 自动 |
| `zhiyu.profiles.is_active = false` | 全设备全端立即撤销 + 拒登 | super_admin 改回 true |

## BR-auth-shared-03 · session 颁发与续签

- `access_token` 30min；`refresh_token` 7d，rotation（旧 refresh 立即失效）
- session 空闲 ≥ 7d → `expired`，需重新登入
- `revoked_at` 一旦写入，**不可** 回滚

## BR-auth-shared-04 · 设备名册（按端独立）

- (user_id, surface) 维度上最多 3 条未撤销 session
- 第 4 条登入 → 找 `last_seen_at` 最早一条 revoke，写 `kicked_reason = 'device-limit'`
- app 与 admin 各自计数，互不影响

## BR-auth-shared-05 · CSRF / cookie / 跨域

- 所有写接口必须双提交 CSRF
- cookie 全部 `HttpOnly; Secure; SameSite=Lax`；OAuth 回调允许 `SameSite=None; Secure`
- 两端 cookie name 不同：`sb-access` / `sb-admin-access`；**不**共域 (`app.<host>` / `admin.<host>`)

## BR-auth-shared-06 · 节流

| 接口 | 节流 |
|------|------|
| `/auth/login` | 5 次错密锁 15min（见 BR-02） |
| `/auth/register`（app 独有，但规则共享） | 60s 倒计时 + 1h 3 次 |
| `/auth/forgot-password` | 同上 |
| `/auth/resend-verification` | 同上 |

## BR-auth-shared-07 · 不暴露账户存在性

- 注册：邮箱已存在 → 同样返回 `{ok: true}`，提示「若该邮箱未注册，验证邮件已发出」
- 忘记密码：同样固定返回 `{ok: true}`
- 登入失败：不区分「邮箱不存在」与「密码错」，统一 `INVALID_CREDENTIALS`
- 例外：admin 端「非 super_admin 登入」**主动** 返回 `AUTH_USE_USER_ENTRY` —— 该提示属合规白名单，不视为暴露

## BR-auth-shared-08 · 数据清单（共享列）

- `profiles`：`id`(=auth.user_id) / `role` / `is_active` / `display_name` / `avatar_url` / `locale` / `email_verified_at`
- `user_sessions`：`id` / `user_id` / `device_id` / `device_name` / `user_agent` / `ip` / `refresh_jti` / `created_at` / `last_seen_at`
- `auth_login_attempts`：`email` / `ip` / `user_agent` / `success` / `reason` / `created_at`（cron 清7天外）

---

## 99. 上游引用

- [C02-permissions/04-data-model.md](../../../C02-permissions/04-data-model.md)
- [C02-permissions/05-auth-feature-guideline.md](../../../C02-permissions/05-auth-feature-guideline.md)
- [C03-ia/auth/_shared/state-machines.md](../../../C03-ia/auth/_shared/state-machines.md)
- [C03-ia/auth/_shared/flows-shared.md](../../../C03-ia/auth/_shared/flows-shared.md)
- [glossary.md](./glossary.md)

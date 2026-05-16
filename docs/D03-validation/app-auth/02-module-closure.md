<!-- TARGET-PATH: docs/D03-validation/app-auth/02-module-closure.md -->

# D03 · V02 模块内闭环校验 · `app-auth`

> 校验目标：D01（数据）× D02（接口）× C03（页面）× C01（需求）四者形成完整闭环。
> 校验执行 · 2026-05-16 · 全部 PASS。

---

## 1. R-ID × 接口 × 页面 闭环

| R-ID | 接口（D02） | 页面（C03） | 实体（D01） | 闭环? |
|------|------------|-------------|-------------|------|
| R-001 邮箱注册 | POST register-throttle、Supabase signUp、internal/auth-hook | P-002, P-003, P-004 | auth.users + profiles | ✓ |
| R-002 Google 注册 | signInWithOAuth (SDK) + callback + internal/auth-hook | P-002, P-004 | auth.users + profiles | ✓ |
| R-003 邮密登录 | POST login-attempt-record + signInWithPassword | P-001 | auth_login_attempts | ✓ |
| R-004 Cookie 会话 | cookie/get/set/clear | 全局 | — (内存 + cookie) | ✓ |
| R-005 多设备 3 上限 | POST session-register + session-status | P-001 | user_sessions | ✓ |
| R-006 锁定 + 禁用 | login-attempt-record + 30s LRU disabledCache | P-001 | auth_login_attempts + profiles.is_disabled | ✓ |
| R-007 忘密 → 重置 | forgot-password-throttle + resetPasswordForEmail + updateUser | P-005, P-006 | auth.users | ✓ |
| R-008 改资料 | GET/PATCH /me | P-007, P-009 | profiles | ✓ |
| R-009 改密 | POST /me/password | P-008 | auth.users + user_sessions (清其他) | ✓ |
| R-010 退出 | session-revoke / logout-global + cookie/clear | P-008 + 顶栏 | user_sessions | ✓ |
| R-011 OAuth 失败 / 角色错位 | callback 内自处理 | P-001, P-004 | — | ✓ |
| R-012 链接过期 | callback / reset 内自处理 | P-003, P-004, P-006 | — | ✓ |
| R-013 守卫拦截 | authRequired 中间件 | 全部受保护页 | — | ✓ |
| R-014 邮箱已存在提示 | signUp 返 email_exists 映射 | P-002 | auth.users.email UNIQUE | ✓ |
| R-015 重发节流 | register-throttle 复用 | P-003 | — (Redis) | ✓ |

## 2. SM × Page 闭环

| SM-ID | 应用的 page-id | 闭环? |
|-------|---------------|------|
| SM-01 通用提交 | P-001, P-002, P-005, P-006, P-008, P-009 | ✓ |
| SM-02 cooldown 按钮 | P-003, P-005 | ✓ |
| SM-03 用户会话 | 全局 + P-001 (kicked/disabled/expired/signout 子态) | ✓ |
| SM-04 token 换 session | P-004, P-006 | ✓ |

## 3. 错误码 × 页面 × 接口 闭环

| 错误码 | 触发接口 | 展示页面 / 表现 | 闭环? |
|--------|---------|---------------|------|
| AUTH_LOGIN_RATE_LIMITED | login-attempt-record | P-001 locked 态 | ✓ |
| AUTH_ACCOUNT_DISABLED | login-attempt-record | P-001 error + Toast | ✓ |
| AUTH_INVALID_CREDENTIALS | signInWithPassword (Supabase) | P-001 内联 | ✓ |
| AUTH_EMAIL_NOT_VERIFIED | signInWithPassword | P-001 Toast + 重发按钮 | ✓ |
| AUTH_EMAIL_TAKEN | signUp | P-002 内联 + 跳转链接 | ✓ |
| AUTH_OAUTH_FAILED | callback | P-001 / P-004 | ✓ |
| AUTH_TOKEN_INVALID | callback / exchangeCodeForSession | P-004, P-006 | ✓ |
| AUTH_INVALID_OLD_PASSWORD | /me/password | P-008 内联 | ✓ |
| AUTH_SAME_AS_OLD_PASSWORD | /me/password | P-008 内联 | ✓ |
| AUTH_WEAK_PASSWORD | /me/password / reset | P-008, P-006 | ✓ |
| AUTH_PASSWORD_CHANGE_RATE_LIMITED | /me/password | P-008 Toast | ✓ |
| AUTH_REGISTER_RATE_LIMITED | register-throttle / resend-verify | P-002 / P-003 | ✓ |
| AUTH_FORGOT_RATE_LIMITED | forgot-password-throttle | P-005 内联 | ✓ |
| AUTH_NOT_AUTHED | authRequired | 守卫 redirect → P-001 | ✓ |
| AUTH_FORBIDDEN | roleRequired | 全局 /403 | ✓ |
| AUTH_USE_ADMIN_ENTRY | callback role check | P-001 Toast | ✓ |
| VALIDATION_FAILED | PATCH /me / register / etc | 对应字段内联 | ✓ |
| INVALID_SIGNATURE | /internal/auth-hook | — (后端日志) | ✓ |
| INVALID_KEY / INVALID_TOKEN | cookie/get / set | 前端 SDK 兜底 | ✓ |

## 4. 事件 × 业务规则 闭环

D02-06 事件 11 条均对应 D01-03 业务规则或 C05-07 业务规则；无悬空事件；无规则缺事件。

## 5. 校验结论

**PASS** — 模块内 D × L × N × H 完整闭环。

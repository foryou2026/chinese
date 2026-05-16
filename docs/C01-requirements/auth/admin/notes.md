<!-- TARGET-PATH: docs/C01-requirements/admin-auth/baseline.md -->

# C01 · 需求基线 · `admin-auth`

> 冻结状态:已冻结 · 2026-05-16
> 上游:[`_input/draft.md`](./_input/draft.md) · [`B02-05 §1`](../../B02-permissions/05-auth-feature-guideline.md)
> 下游:C02 IA · C03 页面 · C05 PRD · D 阶段全部

---

## 1. 需求条目 (R-ID)

| R-ID | 标题 | 说明 | 关联角色 |
|------|------|------|---------|
| R-admin-auth-001 | 邮密登录 | 管理员通过 `/admin/auth/login` 输入邮箱 + 密码登录;仅 `super_admin` 角色放行,其它角色 (含 `user`) 立即 signOut 并报 `AUTH_USE_USER_ENTRY` | super_admin |
| R-admin-auth-002 | 角色守卫 | `/admin/*` 全路径在 TanStack Router `_admin` 根 loader + 后端 `requireRole('super_admin')` 双重校验;非超管 → 跳 `/admin/auth/login?error=not_admin` | super_admin |
| R-admin-auth-003 | Cookie 会话 + CSRF | 同 app:`zhiyu-at`/`zhiyu-rt` HttpOnly + `zhiyu-csrf` Double-Submit;写请求必须带 `X-CSRF-Token` | super_admin |
| R-admin-auth-004 | 3 设备上限 | `user_sessions` 带 `surface='admin'` 维度独立计数;第 4 次登录踢最早 | super_admin |
| R-admin-auth-005 | 锁定 + 禁用拦截 | 同 app:5/15min 锁定;`profiles.is_disabled=true` 立即拒登 (运维可手工 disable 异常管理员) | super_admin |
| R-admin-auth-006 | 忘记密码 → 重置 | `/admin/auth/forgot` → 邮件 → `/admin/auth/reset-password`;链接 15min 一次性;成功后 revoke 其他设备 refresh | super_admin |
| R-admin-auth-007 | 修改密码 | `/admin/me` 内联表单:旧密 + 新密 + 重复新密;复用 `POST /me/password` 同款规则 (8+ 字母 + 数字) | super_admin |
| R-admin-auth-008 | 退出 | "本设备退出" + "全部设备退出";后者 revoke 全部 refresh + 清当前 Cookie | super_admin |
| R-admin-auth-009 | 守卫 redirect | 未登录访问 `/admin/foo` → 跳 `/admin/auth/login?redirect=/admin/foo`;成功登录后跳回 | super_admin |
| R-admin-auth-010 | 账号 seed 创建 | **无产品功能**;新管理员通过运维脚本 `scripts/db/seed-super-admin.sh` 创建,密码由运维侧明文交付;本条仅为契约存档 | 运维 |

---

## 2. 非功能性

| 类别 | 指标 |
|------|------|
| 登录响应 p95 | < 800ms (含锁定查表 + Supabase Auth) |
| 重置邮件 | dev mock → `system/.dev/mailbox/` · prod → SMTP |
| 审计 | 所有登录 / 改密 / 退出 100% 入 `audit_logs` (event 详见 D02-06) |
| i18n | 5 语全量;key 命名 `auth.admin.*` (复用 `auth.*` 的 80%,仅页面标题等差异) |
| 安全 | 严禁缓存任何 admin token 于浏览器存储;严禁明文密码入日志/审计 payload |

---

## 3. 不做清单 (v1)

| 项 | 原因 |
|----|------|
| 注册页 | 邀请制,无自助注册 |
| Google OAuth | 管理端 100% 邮密 |
| 邮箱验证页 | seed 时已确认 |
| 头像 / 显示名编辑 | 管理端不展示头像 |
| 自助删除账号 | 严禁超管删自己 |
| 修改邮箱 | 走运维变更 |
| TOTP / WebAuthn | v2+ |
| 自助邀请 UI | v2+ (需先升级 B02-01) |
| 管理员列表 / 改他人密码 | v2+ (归 `admin-users` feature) |

---

## 4. R-ID 与 B 阶段映射

| R-ID | B 阶段依据 |
|------|----------|
| R-001/002/003/008 | B02-02 主流程 · B02-03 中间件 · B01-09 §3 |
| R-004 | B01-09 §0 "3 设备硬上限" |
| R-005 | B02-02 §6 节流 · B02-04 `auth_login_attempts` |
| R-006 | B02-02 §5 重置流程 |
| R-007 | B02-05 §3 `/me/password` |
| R-009 | B02-05 §4.4 redirect 约定 |
| R-010 | B01-09 §1 "邀请制注册" 备注 · seed.sql |

---

## 5. 验收 (Acceptance)

- 4 个页面均能在 mock 模式下完整跑通 (mock SMTP / mock 邮件落 mailbox);
- 非 super_admin 用 user 账号尝试登录 → 立即 signOut + Toast "请使用用户入口登录";
- 任意管理员密码改成功 → 立即在另一个浏览器收到 401 → 跳回登录页;
- 管理员尝试登录第 4 设备 → 第 1 设备 10 秒内被踢 (轮询 `session-status`)。

<!-- TARGET-PATH: docs/B02-permissions/00-index.md -->

# B02 · 权限与认证规范（索引）

> **阶段**：B02-P 权限基线  
> **角色**：架构师 + PM  
> **feature**：全局  
> **上游依赖**：`B01-architecture/09-auth-infra.md`、`_input/roles-input.md`、`A00-meta/questions/A-questions-round1-resolved.md`  
> **冻结状态**：已冻结 · 2026-04-28  
> **下游影响**：所有 D02 L 必须使用本目录定义的中间件与错误码；`app-auth` / `admin-auth` 两个 feature 的 C/D 阶段全部产物

---

## 0. 摘要

- **角色**：仅 2 个 — `super_admin`、`user`。**不引入第三种角色 / 不做 RBAC 矩阵**。
- **登录方式**：应用端 = 邮箱 + Google；管理端 = 仅邮箱。
- **Token**：Supabase JWT（HS256），**HttpOnly Cookie** 存储 + CSRF Double-Submit。
- **多设备**：硬上限 3，第 4 次踢最早；不提供"我的设备"页。
- **不上 2FA**；防爆破靠后端节流。
- **超管 seed**：`.env` 注入 + 部署脚本写入；UI 无创建入口；丢密码走手工 SQL 逆生（[04 §3.4](./04-data-model.md)）。

---

## 1. 文件清单

| 序号 | 文件 | 职责 | 何时引用 |
|------|------|------|---------|
| _input | [`_input/roles-input.md`](./_input/roles-input.md) | PM 模拟输入回写 | 仅评审本期角色基线时 |
| 00 | 00-index.md（本文件）| 索引 + 原则 + 跨文件约定 | 进入 B02 必读 |
| 01 | [01-roles.md](./01-roles.md) | 角色枚举、可见菜单、与 PRD 模块对应、超管自保规则 | 任何涉及角色判断的开发 |
| 02 | [02-auth-flow.md](./02-auth-flow.md) | 登录 / 登出 / Token / 会话 / 密码 / 忘密 / 邮件 | 实现 `<surface>-auth` 任何流程 |
| 03 | [03-authz-mechanism.md](./03-authz-mechanism.md) | 前端路由守卫 / 菜单过滤 / 按钮可见；后端 Hono 中间件（`authRequired` / `adminRequired` / `csrfRequired` / `optionalAuth`） | 任何路由 / 接口落地前 |
| 04 | [04-data-model.md](./04-data-model.md) | `auth.users` 字段约定、`profiles` / `user_sessions` / `auth_login_attempts` / `audit_logs` 表结构、RLS 策略 | D01 D 阶段引用本表；不重复定义 |
| 05 | [05-auth-feature-guideline.md](./05-auth-feature-guideline.md) | 给 `app-auth` / `admin-auth` 两 feature 的 C/D 阶段使用指南：哪些页面要建、命名、必须遵守的接口/字段/错误码 | 启动 `<surface>-auth` C 阶段时 |
| 99 | [99-open-questions.md](./99-open-questions.md) | 待 PM 拍板项 | 评审 |

---

## 2. 核心原则（不可违反 · 与 grules/G3 §一 完全一致）

1. **认证后端 = 自托管 Supabase Auth（GoTrue）**。Hono API 不自建 JWT 签发器。
2. **角色仅 2 种**：`super_admin` + `user`。
3. **登录方式**：应用端 = 邮箱密码 + Google OAuth；管理端 = 仅邮箱密码。
4. **Token = HS256 JWT**；access 1h / refresh 30d 滚动。
5. **多设备**：硬上限 3，第 4 次登录踢最早。
6. **不自动登出**：refresh 未过期就保持登录。
7. **超级管理员**：seed 写入；不能删/禁用自己；忘密走 SQL 逆生。
8. **被禁用账号**：返回 `AUTH_ACCOUNT_DISABLED` + 撚销全部 refresh + 删 user_sessions。
9. **凭证存储 = HttpOnly Cookie**（PM 决策：安全优先）+ CSRF Double-Submit。
10. **角色来源**：JWT `app_metadata.role`，不再查库。
11. **防爆破**：不依赖第三方验证码；仅后端节流。
12. **i18n 全 5 语**：所有 `AUTH_*` 错误提示 + 邮件模板 zh/en/vi/th/id。

---

## 3. B02 与未来 `<surface>-auth` feature 的边界

B02 **只**定义"基础设施 + 规则 + 数据结构"；具体的页面交互、表单字段、跳转链路、文案、错误展示位置、按钮顺序等，留给 feature 的 C 阶段：

| 留给 B02 | 留给 `app-auth` / `admin-auth` |
|---------|------------------------------|
| 角色枚举、Token 规格、Cookie 策略 | 登录页 / 注册页 / 找回密码 / 邮箱验证 / 个人中心 / 安全设置 等具体页面与交互 |
| 中间件分层、错误码清单 | 表单字段 / 验证规则 / 文案 / 跳转链 |
| `profiles` / `user_sessions` / `auth_login_attempts` / `audit_logs` 表结构 | feature 自有的偏好 / 通知 / 实名 等附加表 |
| GoTrue Hook + DB Trigger（注册侧风控与默认 role 注入）| Onboarding 流程 / 头像上传 / 修改邮箱 / 修改密码具体接口 |

---

## 4. 跨文件约定

- 角色枚举唯一定义 → [01-roles.md §1](./01-roles.md)
- 错误码统一前缀 `AUTH_*`，权威清单 → [03-authz-mechanism.md §4](./03-authz-mechanism.md)
- SQL / 表结构权威 → [04-data-model.md](./04-data-model.md)
- 中间件签名 / 错误响应格式 → 与 `B01-architecture/04-api-conventions.md` 完全一致
- 任何 PRD 模块的"按钮可见 / 列表过滤"逻辑都不在 B02 写死，按"角色 + 资源所有权"两条判定，详见 [01 §四](./01-roles.md)

---

## 99. 待确认问题
（无）

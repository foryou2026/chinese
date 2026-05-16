<!-- TARGET-PATH: docs/C02-permissions/00-index.md -->

# C02 · 角色与权限（全局索引）

> **阶段**：C02-P 角色与权限（per feature 增量，全局合并）
> **角色**：安全/权限工程师
> **feature**：全局合并（不开 feature 子目录）
> **上游依赖**：`B01-architecture/09-auth-infra.md`、`B01-architecture/08-surfaces.md`、各 feature `C01-requirements/<feature>/baseline.md`、`_input/<feature>/roles-input.md`
> **冻结状态**：滚动冻结（每次新增 feature 经过 C02-P 都会增量并入）
> **下游影响**：所有 feature 的 C03 I / C04 N / C05 H / C06 E 必须读取本目录确定角色可见性与可达性；D02 L 中间件必须使用本目录定义的错误码与权限模型

---

## 0. 摘要

- **角色**：当前仅 2 个 — `admin`、`user`。新增角色须经 C02-P 走澄清流程。
- **登录方式**：应用端 = 邮箱 + Google；管理端 = 仅邮箱。
- **Token**：Supabase JWT（HS256），**HttpOnly Cookie** 存储 + CSRF Double-Submit。
- **多设备**：硬上限 3，第 4 次踢最早；不提供「我的设备」页。
- **不上 2FA**；防爆破靠后端节流。
- **超管 seed**：`.env` 注入 + 部署脚本写入；UI 无创建入口；丢密码走手工 SQL 逆生（[03 §3.4](./03-data-model.md)）。

---

## 1. 文件清单

| 序号 | 文件 | 职责 | 何时引用 |
|------|------|------|---------|
| _input | [`_input/`](./_input/) | 每个 feature 的角色描述输入（per feature 落 `<feature-id>/roles-input.md`）| C02-P 澄清评审 |
| 00 | 00-index.md（本文件）| 索引 + 原则 + 跨文件约定 | 进入 C02 必读 |
| 01 | [01-roles.md](./01-roles.md) | 全局角色枚举、可见菜单、与 PRD 模块对应、超管自保规则 | 任何涉及角色判断的开发 |
| 02 | [02-authz-mechanism.md](./02-authz-mechanism.md) | 前端路由守卫 / 菜单过滤 / 按钮可见；后端 Hono 中间件（`authRequired` / `adminRequired` / `csrfRequired` / `optionalAuth`） | 任何路由 / 接口落地前 |
| 03 | [03-data-model.md](./03-data-model.md) | 用户账号 字段约定、用户档案 / 会话记录 / 登录尝试记录 / 审计记录 表结构、RLS 策略 | D01 D 阶段引用本表；不重复定义 |
| 99 | [99-open-questions.md](./99-open-questions.md) | 待 PM 拍板项 | 评审 |

---

## 2. 核心原则（不可违反）

1. **认证后端 = Supabase Auth（Supabase Auth）**。Hono API 不自建 JWT 签发器。
2. **角色枚举单点**：所有角色定义集中于 [01-roles.md](./01-roles.md)，新增角色经 C02-P 走澄清。
3. **登录方式**：应用端 = 邮箱密码 + Google OAuth；管理端 = 仅邮箱密码。
4. **Token = HS256 JWT**；access 1h / refresh 30d 滚动。
5. **多设备**：硬上限 3，第 4 次登录踢最早。
6. **不自动登出**：refresh 未过期就保持登录。
7. **超级管理员**：seed 写入；不能删/禁用自己；忘密走 SQL 逆生。
8. **被禁用账号**：返回 `AUTH_ACCOUNT_DISABLED` + 撤销全部 refresh + 删 会话记录。
9. **凭证存储 = HttpOnly Cookie**（PM 决策：安全优先）+ CSRF Double-Submit。
10. **角色来源**：JWT `账号元数据.role`，不再查库。
11. **防爆破**：不依赖第三方验证码；仅后端节流。
12. **i18n 全 5 语**：所有 `AUTH_*` 错误提示 + 邮件模板 zh/en/vi/th/id。

---

## 3. C02 与 `auth` feature 的边界

C02 **只**定义「全局角色 + 权限机制 + 数据结构」；具体的页面交互、表单字段、跳转链路、文案、错误展示位置、按钮顺序等，属于 `auth` feature 的 C04 N（页面交互）/ C05 H（HTML 原型）/ C06 E（PRD）阶段产物。

| 留给 C02 全局 | 留给 `auth` feature 的 C04 / C05 / C06 |
|---------|------------------------------|
| 角色枚举、Token 规格、Cookie 策略 | 登录页 / 注册页 / 找回密码 / 邮箱验证 / 个人中心 / 安全设置 等具体页面与交互 |
| 中间件分层、错误码清单 | 表单字段 / 验证规则 / 文案 / 跳转链 |
| 用户档案 / 会话记录 / 登录尝试记录 / 审计记录 表结构 | feature 自有的偏好 / 通知 / 实名 等附加表 |
| Supabase Auth Hook + DB Trigger（注册侧风控与默认 role 注入）| Onboarding 流程 / 头像上传 / 修改邮箱 / 修改密码具体接口 |

> 其他业务 feature（如 `course`、`discover-china`）的 C02-P 仅向本目录**增量并入**自己的「新增角色 / 权限粒度 / 数据可见范围」，**不**再各自维护一份权限文档。

---

## 4. 跨文件约定

- 角色枚举唯一定义 → [01-roles.md §1](./01-roles.md)
- 错误码统一前缀 `AUTH_*`，权威清单 → [02-authz-mechanism.md §4](./02-authz-mechanism.md)
- SQL / 表结构权威 → [03-data-model.md](./03-data-model.md)
- 中间件签名 / 错误响应格式 → 与 `B01-architecture/04-api-conventions.md` 完全一致
- 任何 PRD 模块的「按钮可见 / 列表过滤」逻辑都不在 C02 写死，按「角色 + 资源所有权」两条判定，详见 [01 §四](./01-roles.md)

---

## 99. 待确认问题
（无）

<!-- TARGET-PATH: docs/C02-permissions/01-roles.md -->

# 01 · 角色定义

> **阶段**：B02-P  
> **上游**：`_input/roles-input.md`、`B01-architecture/08-surfaces.md`  
> **下游**：`B03-design/design-system/03-navigation.md`、所有 D02 L、`auth` / `auth` feature  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 全系统**仅 2 个角色**：`super_admin`（管理端）+ `user`（应用端）。
- 角色字段位置：JWT `app_metadata.role`；DB `auth.users.raw_app_meta_data->>'role'`，trigger 同步到 `zhiyu.profiles.role` 仅作冗余索引。
- **超管自保**：不能删 / 禁用自己；不出现在任何"用户管理"列表中；UI 无创建入口。

---

## 1. 角色枚举（权威清单）

| 角色（DB / JWT 字面量）| 显示名 | 入口 surface | 备注 |
|--------------------|-------|-------------|------|
| `super_admin` | 超级管理员 | `admin`（`/admin/*`）| 默认 1 个（`.env` seed）；技术上允许多个；UI 无创建入口；不能删/禁用自己；不出现在任何"用户管理"列表 |
| `user` | 用户 | `app`（`/`）| 所有邮箱 / Google 注册的新账号默认 `role='user'` |

> 本期**严禁**引入第三种角色。运营 / 审核 / 客服 / 内容编辑 / AI 训练师 等诉求一律视为 super_admin 兼任。

---

## 2. 菜单暴露矩阵（与 `B03-design/design-system/03-navigation.md` 完全对齐）

### 2.1 应用端（surface=`app`，角色 `user` 可见，未登录也能看见菜单结构）

| 菜单 | 路由 | feature | 未登录可见 |
|------|------|---------|-----------|
| 发现中国 | `/discover` | `discover-china` | ✅（仅前 3 主题可浏览）|
| 系统课程 | `/courses` | `course` | ✅（点击跳登录）|
| 游戏专区 | `/games` | `games`（未来）| ✅（点击跳登录）|
| 小说专区 | `/novels` | `novels`（未来）| ✅（点击跳登录）|
| 个人中心 | `/me` | `auth` + `user-account`（未来）| 替换为「登录 / 注册」入口 |

### 2.2 管理端（surface=`admin`，角色 `super_admin` 可见）

| 菜单 | 路由 | feature | 备注 |
|------|------|---------|------|
| 用户管理 | `/admin/users` | `user-management`（未来）| 只列 `role='user'`，**绝不**列任何 super_admin |
| 发现中国 | `/admin/discover` | `discover-china` | 内容审核 / 上下架 |
| 系统课程 | `/admin/courses` | `course` | 课程管理 / 上下架 |
| 小说专区 | `/admin/novels` | `novels`（未来）| 章节管理 / 审核 |

**管理端本期不暴露**：游戏配置、经济、邀请、客服、安全、内容工厂、i18n 校对、支付配置。

---

## 3. 用户管理菜单的 P0 硬性规则

管理端 `/admin/users` 与对应接口 `GET /admin/v1/users`：

1. **只能列出 `role='user'`** 的账号；
2. **绝不**列出任何 `role='super_admin'`（包括管理员自己）；
3. 列表中"封禁 / 解禁 / 重置密码"操作**只对 `role='user'` 生效**；
4. 后端 SQL **必须**强约束 `WHERE role = 'user'`；
5. 前端按钮可见性仅作兜底，**不能反过来靠前端过滤**。

**反例（禁止）**：返回全表给前端，让前端 `.filter(role !== 'super_admin')`。一旦前端漏过滤就是越权展示。

---

## 4. 权限判定只问两件事

1. **是否登录**：`req.user` 是否存在 → 中间件 `authRequired`。
2. **是否 super_admin**：`req.user.role === 'super_admin'` → 中间件 `adminRequired`。

对"自己资源"的所有权判定（如自己的订单 / 自己的学习进度），按 `row.user_id === req.user.id` 直接判断，**不进入角色系统**。本期代码不读取任何"数字权限级别"，统一字符串比较。

---

## 5. 与 feature 的对应关系

| feature ID | 应用端（`user`）| 管理端（`super_admin`）|
|-----------|--------------|---------------------|
| `discover-china` | ✅ 浏览（未登录限前 3 主题）| ✅ 内容审核 / 上下架 |
| `course` | ✅ 学习 | ✅ 课程管理 |
| `auth`（未来）| ✅ 自有登录 / 注册 / 找回密码 / 个人中心 | ❌ |
| `auth`（未来）| ❌ | ✅ 仅邮箱密码登录 |
| `user-management`（未来）| ❌ | ✅ 列 / 禁用 / 启用 `role='user'` |
| `games`（未来）| ✅ | ❌ |
| `novels`（未来）| ✅ | ✅ 审核 / 章节管理 |
| `economy`（未来）| ✅ 钱包 | ❌ |
| `payment`（未来）| ✅ 下单（Paddle）| ❌（去 Paddle 后台直管）|
| `referral`（未来）| ✅ | ❌ |
| `customer-service`（未来）| ✅ 工单 | ❌（本期无 UI，邮件兜底）|
| `i18n`（未来）| 隐式 | 隐式 |

---

## 6. 变更约束

- 新增 / 修改角色 → 必须写迁移 `supabase/migrations/xxxx_xxx.sql`，**不允许只改 TS 常量**；
- 修改菜单暴露 → 必须先改 [`B03-design/design-system/03-navigation.md`](../B03-design/design-system/03-navigation.md) + 本文件 §2 → 再改代码；
- 任何"管理员可以管理管理员"的新需求，本期一律拒绝，走 SQL 直改 + 变更评审单。

---

## 99. 待确认问题
（无）

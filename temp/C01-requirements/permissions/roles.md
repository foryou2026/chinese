<!-- TARGET-PATH: docs/C01-requirements/permissions/roles.md -->

# 权限注册表 — 角色枚举与全局策略

> **维护方式**：增量更新，每轮新功能若引入新角色或修改策略，在本文件对应节追加/修改并标注增量标记。
> **引用方**：C02（信息架构）、C03（HTML 原型）、D01（数据规范）、D02（接口规范）
> **上游依赖**：B01-architecture/08-surfaces.md、B01-architecture/09-auth-infra.md
> **最后更新**：2026-05-17（初始建立，合并自 auth / course / discover-china baseline.md）

---

## P1. 角色枚举

全系统**仅 2 个角色**：`ROLE-USER`（应用端）+ `ROLE-ADMIN`（管理端）。当前严禁引入第三种角色；运营 / 审核 / 客服等诉求一律视为 admin 兼任。

| 角色 ID | DB / JWT 字面量 | 显示名 | 职责（一句话） | 不能做 | 首次引入功能 |
|--------|---------------|-------|-------------|--------|------------|
| ROLE-USER | `user` | 普通用户 / 学员 | 在 app 端注册登录、学习课程、浏览文化内容、维护个人资料 | 进入 admin 受守卫页面 | auth |
| ROLE-ADMIN | `admin` | 超级管理员 | 登录 admin 端、管理课程内容与文化内容、处理举报、访问全部 admin 受守卫页面 | 在管理端自助注册；从管理端编辑普通用户密码；删除 12 个固定类目 | auth |

---

## P2. 多角色策略

- 一个用户拥有**唯一**角色（`user` 或 `admin`），不支持多角色叠加。
- 角色字段位置：JWT 元数据 `.role`；DB `users.role`；触发器同步到用户档案（冗余索引）。
- 是否需要角色组 / 部门概念：**否**（当前阶段不需要）。
- 同一用户跨 surface：**不适用**（角色绑定 surface，ROLE-USER 只进 app，ROLE-ADMIN 只进 admin）。

---

## P3. 角色 × surface 矩阵

| 角色 ID | `app` | `admin` |
|---------|-------|---------|
| ROLE-USER | ✅ 主 surface | ❌ 被守卫阻断 |
| ROLE-ADMIN | ❌ 不适用 | ✅ 主 surface |

---

## P4. 系统级硬约束

- ROLE-ADMIN 不能删除 / 禁用自己（`AUTH_SUPER_ADMIN_SELF_DELETE`）。
- ROLE-ADMIN 账号不出现在任何"用户管理"列表中；后端 SQL 必须强约束 `WHERE role = 'user'`。
- UI 无创建管理员账号的入口；管理员仅可由运维 seed 流程创建。
- 被禁用账号统一返回 403，全设备登出。
- 接口 / 列表 / 封禁 / 重置密码操作**只对 `role='user'` 生效**；不允许靠前端过滤代替后端约束。

---

## P5. 变更历史

| 轮次 | 日期 | 变更摘要 | 来源功能 |
|------|------|---------|---------|
| 初始 | 2026-05-17 | 建立文件，合并 auth / course / discover-china 的角色定义 | auth, course, discover-china |

<!-- TARGET-PATH: docs/C01-requirements/permissions/admin-matrix.md -->

# 权限注册表 — admin 端权限矩阵

> **维护方式**：增量更新，每轮新功能若为 admin 端新增或变更权限行，在本文件追加并标注增量标记。
> **角色定义**：见 `permissions/roles.md`
> **授权基础设施**：见 `B01-architecture/09-auth-infra.md`
> **最后更新**：2026-05-17（初始建立，合并自 auth / course / discover-china baseline.md）

---

## P2.1 功能点级权限矩阵（admin 端）

> admin 端所有页面均需 `adminRequired` 中间件（`authRequired` + `role === 'admin'`）；ROLE-USER 统一被阻断。

| 资源 / 操作 | ROLE-ADMIN | 数据范围 | 所属功能 |
|------------|:----------:|---------|---------|
| **— 认证 —** | | | |
| admin 登录页 | ✅ | — | auth |
| admin 忘记密码流程 | ✅ | — | auth |
| admin 修改密码 | ✅ | owner-only | auth |
| admin 退出登录 | ✅ | — | auth |
| **— 课程管理 —** | | | |
| 课程目录总览 | ✅ | global（含草稿）| course |
| 主题 / 阶段 / 章 / 节四级列表 + 拖拽排序 | ✅ | global | course |
| 节编辑（基本信息 / 知识点绑定 / 发布下架）| ✅ | global | course |
| 知识点列表 + 编辑面板（含媒资 / 题目）| ✅ | global | course |
| 题目列表 + 双开布局预览 + 解析编辑 | ✅ | global | course |
| 批量导入（知识点 / 题目）| ✅ | global | course |
| 学员举报处理 | ✅ | global | course |
| 媒资库（列表 / 上传 / 软删）| ✅ | global | course |
| 考试中心配置 | ✅ | global | course |
| 全局搜索（知识点 / 题目 / 节）| ✅ | global | course |
| **— 发现中国管理 —** | | | |
| 类目统计总览 | ✅ | global | discover-china |
| 文章 CRUD（含草稿）| ✅ | global | discover-china |
| 句子编辑 / 重排 / 插入 | ✅ | global | discover-china |
| 文章发布 / 下架 | ✅ | global | discover-china |
| 三级搜索（类目 / 文章 / 句子）| ✅ | global | discover-china |
| 类目固定不可删 | ❌（硬约束）| — | discover-china |

---

## P2.2 数据可见范围原则（admin 端）

| 角色 ID | 默认可见范围 | 说明 |
|---------|-----------|------|
| ROLE-ADMIN | global（排除其他管理员账号）| 课程全部内容含草稿；文化文章含未发布；不可见其他管理员账号 |

---

## P2.3 授权校验机制（admin 端）

> 认证基础设施引用 `B01-architecture/09-auth-infra.md`，本节只定义授权层。

**后端中间件**：
- `adminRequired`：在 `authRequired` 基础上校验 `role === 'admin'`，挂在 admin 全部路由。
- `csrfRequired`：验证 CSRF 令牌，挂在所有写操作。
- 后端 SQL 凡涉及"用户管理"必须强约束 `WHERE role = 'user'`，不允许靠前端过滤代替。

**前端路由守卫（TanStack Router）**：
- `/_admin/`：未登录 → 跳 `/admin/auth/login`；已登录但非 admin → 跳 `/admin/auth/login?reason=not_admin`。
- 无权操作直接不渲染（不灰显）；后端必须二次校验，前端不可信。

---

## P3. 变更历史

| 轮次 | 日期 | 变更摘要 | 来源功能 |
|------|------|---------|---------|
| 初始 | 2026-05-17 | 建立文件，合并 auth / course / discover-china 的 admin 端权限 | auth, course, discover-china |

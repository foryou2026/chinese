<!-- TARGET-PATH: docs/C01-requirements/permissions/app-matrix.md -->

# 权限注册表 — app 端权限矩阵

> **维护方式**：增量更新，每轮新功能若为 app 端新增或变更权限行，在本文件追加并标注增量标记。
> **角色定义**：见 `permissions/roles.md`
> **授权基础设施**：见 `B01-architecture/09-auth-infra.md`
> **最后更新**：2026-05-17（初始建立，合并自 auth / course / discover-china baseline.md）

---

## P2.1 功能点级权限矩阵（app 端）

| 资源 / 操作 | ROLE-USER（未登录） | ROLE-USER（已登录） | 数据范围 | 所属功能 |
|------------|:------------------:|:-----------------:|---------|---------|
| **— 认证 —** | | | | |
| 登录页 / 注册页 | ✅ | ✅（已登录时跳首页） | — | auth |
| 邮箱注册 | ✅ | ❌ | — | auth |
| Google 一键注册登录 | ✅ | ❌ | — | auth |
| 忘记密码流程 | ✅ | ✅ | — | auth |
| 修改密码 | ❌ | ✅ | owner-only | auth |
| 退出登录 | ❌ | ✅ | — | auth |
| 个人资料查看 / 修改 | ❌ | ✅ | owner-only | auth |
| **— 课程 —** | | | | |
| app 公开落地页 | ✅ | ✅ | global | course |
| app 受守卫课程页（含首页 / 学习地图 / 节内 / 复习 / 考试 / 统计）| ❌ | ✅ | owner-only | course |
| 学习 / 复习 / 节内答题 | ❌ | ✅ | owner-only | course |
| 个人统计 | ❌ | ✅ | owner-only | course |
| 提举报 | ❌ | ✅ | — | course |
| **— 发现中国 —** | | | | |
| 01-03 类目浏览 | ✅ | ✅ | published-only | discover-china |
| 04-12 类目浏览 | ❌（登录引导） | ✅ | published-only | discover-china |
| 文章阅读 + TTS 播放 | ✅（01-03）| ✅ | published-only | discover-china |
| 阅读进度同步（跨设备）| ❌（本地兜底）| ✅ | owner-only | discover-china |
| app 端全文搜索（发现中国）| ✅ | ✅ | published-only | discover-china |

---

## P2.2 数据可见范围原则（app 端）

| 角色 ID | 状态 | 默认可见范围 | 说明 |
|---------|------|-----------|------|
| ROLE-USER | 未登录 | published-only，01-03 类目 | 无需 JWT |
| ROLE-USER | 已登录 | published-only，全部功能 | 自己的进度 / 资料 / 统计；课程内容仅已发布 |

---

## P2.3 授权校验机制（app 端）

> 认证基础设施引用 `B01-architecture/09-auth-infra.md`，本节只定义授权层。

**后端中间件**：
- `authRequired`：验证 JWT 有效并注入 `req.user`，挂在 app 全部受保护路由。
- `optionalAuth`：尝试解析 JWT，失败不报错，挂在公开但需识别身份的路由（如阅读进度）。
- `csrfRequired`：验证 CSRF 令牌，挂在所有写操作。

**前端路由守卫（TanStack Router）**：
- `/_authed/`：未登录 → 跳 `/auth/login?redirect=...`；登入后自动回原页。
- 按钮 / 操作级：无权操作直接不渲染（不灰显）；后端必须二次校验，前端不可信。

**行级所有权**：SRS / 考试 attempt / 阅读进度读写按 `row.user_id === req.user.id` 判定，不进入角色系统。

---

## P3. 变更历史

| 轮次 | 日期 | 变更摘要 | 来源功能 |
|------|------|---------|---------|
| 初始 | 2026-05-17 | 建立文件，合并 auth / course / discover-china 的 app 端权限 | auth, course, discover-china |

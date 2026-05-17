<!-- TARGET-PATH: docs/C02-ia-interaction/auth/account-entry/00-index.md -->

# IA 与交互规范 · account-entry

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`auth`
> **功能**：`account-entry`
> **上游依赖**：`C01-requirements/auth/account-entry/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

app 端未登录用户的**账号入口**：邮箱注册 / Google 注册即登录 / 邮箱密码登录 / 邮箱验证回调，以及关联的节流、自锁、会话管理逻辑。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-auth-app-01` |
| 页面 P-ID | P-app-auth-001, P-app-auth-002, P-app-auth-003, P-app-auth-004 |
| 流程 FL-ID | FL-auth-app-01（邮箱注册主流程）、FL-auth-app-02（登录主流程）、FL-auth-app-05（锁定）、FL-auth-app-06（第 4 设备踢）、FL-auth-app-07（禁用）、FL-auth-app-08（OAuth 失败）、FL-auth-app-09（链接过期）、FL-auth-app-10（网络断）、FL-auth-app-11（守卫拦截） |
| 共享流程 | FL-auth-shared-01（登入成功）、FL-auth-shared-02（登出）、SM-auth-shared-01~04 |
| 覆盖 R-ID | R-auth-001, R-auth-002, R-auth-003, R-auth-004, R-auth-005, R-auth-006, R-auth-010, R-auth-012, R-auth-013, R-auth-014, R-auth-015 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-app-auth-001~004）|

> 共享状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。

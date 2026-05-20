<!-- TARGET-PATH: docs/C02-ia-interaction/auth/admin-entry/00-index.md -->

# IA 与交互规范 · admin-entry

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`auth`
> **功能**：`admin-entry`
> **上游依赖**：`C01-requirements/auth/admin-entry/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

admin 端管理员的**登录入口**：邮箱密码登录（含非管理员阻断）、忘记密码流程、重置密码、会话管理 / 节流 / 自锁 / 路由守卫。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-auth-admin-01` |
| 页面 P-ID | P-admin-auth-001, P-admin-auth-002, P-admin-auth-003 |
| 流程 FL-ID | FL-auth-admin-01（登录）、FL-auth-admin-02（忘密→重置）、FL-auth-admin-05（非 admin 拦截）、FL-auth-admin-06（锁定）、FL-auth-admin-07（禁用）、FL-auth-admin-08（第 4 设备踢）、FL-auth-admin-09（重置链接过期）、FL-auth-admin-10（守卫拦截）、FL-auth-admin-11（5xx 兜底）|
| 共享流程 | FL-auth-shared-01（登入成功）、FL-auth-shared-04（忘记密码）、SM-auth-shared-01~04 |
| 覆盖 R-ID | R-auth-003, R-auth-004, R-auth-005, R-auth-006, R-auth-010, R-auth-016 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-admin-auth-001~003）|

> 共享状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。

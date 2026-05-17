<!-- TARGET-PATH: docs/C02-ia-interaction/auth/admin-account/00-index.md -->

# IA 与交互规范 · admin-account

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`auth`
> **功能**：`admin-account`
> **上游依赖**：`C01-requirements/auth/admin-account/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

admin 端已登录管理员的**账号管理**：修改密码（先验旧密）、本设备退出 / 全部设备退出。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-auth-admin-02` |
| 页面 P-ID | P-admin-auth-004 |
| 流程 FL-ID | FL-auth-admin-03（改密）、FL-auth-admin-04（退出）、FL-auth-shared-02（登出）、FL-auth-shared-03（改密）|
| 覆盖 R-ID | R-auth-007, R-auth-008, R-auth-009 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-admin-auth-004）|

> 共享状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。

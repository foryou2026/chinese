<!-- TARGET-PATH: docs/C02-ia-interaction/auth/account-recovery/00-index.md -->

# IA 与交互规范 · account-recovery

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`auth`
> **功能**：`account-recovery`
> **上游依赖**：`C01-requirements/auth/account-recovery/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

app 端未登录用户的**账号找回**：忘记密码 → 邮件一次性链接 → 设新密码 → 自动登入，以及链接过期兜底。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-auth-app-02` |
| 页面 P-ID | P-app-auth-005, P-app-auth-006 |
| 流程 FL-ID | FL-auth-app-09（链接过期）+ FL-auth-shared-04（忘记密码完整流程） |
| 覆盖 R-ID | R-auth-007, R-auth-013, R-auth-014 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-app-auth-005~006）|

> 共享状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。

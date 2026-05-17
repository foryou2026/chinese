<!-- TARGET-PATH: docs/C02-ia-interaction/auth/account-profile/00-index.md -->

# IA 与交互规范 · account-profile

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`auth`
> **功能**：`account-profile`
> **上游依赖**：`C01-requirements/auth/account-profile/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

app 端已登录用户的**个人中心**：查看 / 修改 profile（头像、显示名、偏好语言）、修改密码（先验旧密）、本设备退出 / 全部设备退出。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-auth-app-03` |
| 页面 P-ID | P-app-auth-007, P-app-auth-008, P-app-auth-009 |
| 流程 FL-ID | FL-auth-app-03（修改资料）、FL-auth-app-04（修改密码 + 退出）、FL-auth-shared-02（登出）、FL-auth-shared-03（改密）|
| 覆盖 R-ID | R-auth-008, R-auth-009, R-auth-011 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-app-auth-007~009）|

> 共享状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。

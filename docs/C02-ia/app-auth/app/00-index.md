<!-- TARGET-PATH: docs/C02-ia/app-auth/app/00-index.md -->

# C02 · `app-auth` 信息架构

> **阶段**：C02-I · **feature**：`app-auth`  
> **上游**：[`C01-requirements/app-auth/baseline.md`](../../C01-requirements/app-auth/baseline.md)、[`_input/page-direction.md`](./_input/page-direction.md)、[`B02-permissions/05-auth-feature-guideline.md`](../../B02-permissions/05-auth-feature-guideline.md)  
> **下游**：本 feature C03 / C04 / C05 / D02 全部产物  
> **冻结状态**：已冻结 · 2026-05-16

---

## 0. 摘要

- 1 个 feature 拆 3 个 module：`account-entry`（登录 / 注册 / OAuth 入口）、`account-recovery`（找回 / 重置密码）、`account-profile`（个人中心 3 页）。
- 9 个 page-id 全部已在 [B02-05 §2.1](../../B02-permissions/05-auth-feature-guideline.md) 列出；本目录将其细化为完整的 4 态 + 状态机定义。
- 主流程 5 条：注册 / 登录 / OAuth / 找回密码 / 改资料；异常分支 7 类。

---

## 1. 文件清单

| 序号 | 文件 | 职责 |
|------|------|------|
| _input | [`_input/page-direction.md`](./_input/page-direction.md) | PM 模拟信息架构方向 |
| 00 | 00-index.md（本文）| 索引 + 边界 |
| 01 | [01-feature-catalog.md](./01-feature-catalog.md) | M-ID 功能模块清单 |
| 02 | [02-flows.md](./02-flows.md) | 主流程 + 异常流程图集中 |
| 03 | [03-state-machines.md](./03-state-machines.md) | SM-ID 状态机（页面 / 会话 / 重发邮件按钮）|
| 04 | [04-pages.md](./04-pages.md) | 9 个 page-id 详表 |
| 05 | [05-navigation.md](./05-navigation.md) | 顶栏 + 头像下拉对本 feature 的入口规则 |
| 06 | [06-coverage-matrix.md](./06-coverage-matrix.md) | R-ID × M / 流程 / 状态机 / 页面覆盖矩阵 |
| 07 | [07-error-pages.md](./07-error-pages.md) | 401 / 403 / 链接过期 子状态承载 |
| 99 | [99-open-questions.md](./99-open-questions.md) | 无 |

---

## 2. 边界

- 不涉及 admin 端；admin 端的对应 feature 是独立的 `admin-auth`，将在批次 4 落地。
- 不涉及 onboarding 表单（学习语言 / HSK 起点）—— 那是 `user-account` feature 的职责，本 feature 只负责"注册成功后 redirect 到 `/onboarding` 路径"这件事本身。
- 顶栏与全局菜单结构沿用 [B04 §03](../../B04-design/design-system/03-navigation.md)，本 feature 仅约定"未登录态在哪展示登录入口"。

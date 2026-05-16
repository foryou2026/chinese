<!-- TARGET-PATH: docs/C03-ia/auth/00-index.md -->

# C03 · IA 索引 · auth

> **阶段**：C03-I · **feature**：`auth` · **冻结状态**：已冻结 · 2026-05-16
> **上游**：[`C01-requirements/auth/baseline.md`](../../C01-requirements/auth/baseline.md)、[`C02-permissions/`](../../C02-permissions/)
> **下游**：C04 页面交互 / C05 原型 / C06 PRD

---

## 子目录与文件

`auth` feature 同时覆盖 **应用端（app）** 与 **管理端（admin）** 两个 surface，IA 按 surface 拆分；跨 surface 的状态机、流程归在 `_shared/`：

| 路径 | 内容 |
|------|------|
| [`app/00-index.md`](./app/00-index.md) | 应用端 9 页 IA 索引（M / Flow / SM / Page / Navigation / Coverage / Error） |
| [`admin/00-index.md`](./admin/00-index.md) | 管理端 4 页 IA 索引（同上） |
| [`_shared/state-machines.md`](./_shared/state-machines.md) | 跨 surface 共享状态机（Session / Token / Form-Dirty 等） |
| [`_shared/flows-shared.md`](./_shared/flows-shared.md) | 跨 surface 共享流程（登出 / 401 续签 / 多端踢人 等） |
| [`_input/app-page-direction.md`](./_input/app-page-direction.md) | 应用端页面方向用户输入草案 |
| [`_input/admin-page-direction.md`](./_input/admin-page-direction.md) | 管理端页面方向用户输入草案 |
| [`99-open-questions.md`](./99-open-questions.md) | feature 级 IA 待确认 |

## 命名约定

- page-id：`P-<surface>-auth-<seq3>`（app 9 + admin 4 = 13）
- M-ID：`M-auth-<功能区>`（如 `M-auth-login`、`M-auth-session`）
- Flow-ID：`FL-auth-<seq2>` / 异常 `FX-auth-<seq2>`
- SM-ID：`SM-auth-<域>`（共享 SM 在 `_shared/state-machines.md` 定义，surface 内引用）
- 错误码：详见 [`C02-permissions/02-authz-mechanism.md §4`](../../C02-permissions/02-authz-mechanism.md)

## 边界

- C03 只产出"页面清单 / 流程 / 状态机 / 导航 / 覆盖矩阵 / 错误页"，**不写**字段、不写接口、不写代码。
- 字段定义、错误码、权限策略一律回引 [`C02-permissions/`](../../C02-permissions/) 与 [`C01-requirements/auth/baseline.md`](../../C01-requirements/auth/baseline.md)。
- 视觉与交互组件回引 [`B03-design/design-system/`](../../B03-design/design-system/)。

## 与下游契约

- C04（页面交互规范）按 page-id 一一展开 4 态 + 交互细则；
- C05（HTML 原型）按 page-id 提供 4 态独立 HTML（共 13 × 4 = 52 文件，详见 surface 子目录）；
- C06（PRD）按 page-id 写 06-page-specs。

任何 IA 变更须同步 [`A00-meta/changelog.md`](../../A00-meta/changelog.md)。

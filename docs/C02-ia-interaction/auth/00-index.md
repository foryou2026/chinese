<!-- TARGET-PATH: docs/C02-ia-interaction/auth/00-index.md -->

# IA 与交互规范索引

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **功能**：`auth`
> **上游依赖**：`C01-requirements/auth/baseline.md`、`B01-architecture/09-auth-infra.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 子文件一览

`auth` 功能同时覆盖 **app** 与 **admin** 两个 surface，本目录以扁平结构合并两端内容，共享状态机与流程内联于各文件中。

| 文件 | 内容 |
|------|------|
| [01-feature-catalog.md](./01-feature-catalog.md) | 功能模块清单（app M-auth-app-NN + admin M-auth-admin-NN） |
| [02-flows.md](./02-flows.md) | 业务流程（app FL-auth-app-NN + admin FL-auth-admin-NN + 跨端共享流程 FL-auth-shared-NN） |
| [03-state-machines.md](./03-state-machines.md) | 状态机（app / admin 端独有 + 跨端共享 SM-auth-shared-NN） |
| [04-pages.md](./04-pages.md) | 页面清单（app 9 页 P-app-auth-NNN + admin 4 页 P-admin-auth-NNN） |
| [05-navigation.md](./05-navigation.md) | 导航结构（app 顶栏 / 下拉 / 二级菜单 + admin 顶栏 / 路由树） |
| [06-coverage-matrix.md](./06-coverage-matrix.md) | 覆盖矩阵（R × M × Flow × SM × Page，按端分区） |
| [07-error-pages.md](./07-error-pages.md) | 错误与兜底处理（app + admin） |
| [99-open-questions.md](./99-open-questions.md) | 待确认问题 |

## 命名约定

| 类别 | 格式 | 说明 |
|------|------|------|
| page-id（app） | `P-app-auth-NNN` | app 端，共 9 页（001-009） |
| page-id（admin） | `P-admin-auth-NNN` | admin 端，共 4 页（001-004） |
| 模块（app） | `M-auth-app-NN` | — |
| 模块（admin） | `M-auth-admin-NN` | — |
| 流程（app） | `FL-auth-app-NN` / `FX-auth-app-NN` | — |
| 流程（admin） | `FL-auth-admin-NN` | — |
| 流程（共享） | `FL-auth-shared-NN` | 跨两端必须遵守的不变式 |
| 状态机（app） | `SM-auth-app-NN` | — |
| 状态机（admin） | `SM-auth-admin-NN` | — |
| 状态机（共享） | `SM-auth-shared-NN` | 跨两端共享 |

## 边界

- 本层只产出"页面清单 / 流程 / 状态机 / 导航 / 覆盖矩阵 / 错误页"，**不写**字段、不写接口、不写代码。
- 字段定义、错误码、权限策略一律回引 `C01-requirements/auth/baseline.md`。
- 视觉与交互组件回引 `B02-experience-design/design-system/`。

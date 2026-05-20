<!-- TARGET-PATH: docs/C02-ia-interaction/course/00-index.md -->

# IA 与交互规范索引

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **功能**：`course`
> **上游依赖**：`C01-requirements/course/baseline.md`、`B01-architecture/08-surfaces.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 子文件一览

`course` 功能覆盖 **app**（学员侧）与 **admin**（运营侧）两个 surface，本目录以扁平结构合并两端，共享状态机与流程内联于各文件中。

| 文件 | 内容 |
|------|------|
| [01-feature-catalog.md](./01-feature-catalog.md) | 功能模块清单（app 7 个模块 + admin 6 个模块） |
| [02-flows.md](./02-flows.md) | 业务流程（app 端 + admin 端 + 跨端共享流程） |
| [03-state-machines.md](./03-state-machines.md) | 状态机（课程进度 / 内容发布 / 答题 / SRS / 考试 / 弱网队列 / 编辑 Dirty） |
| [04-pages.md](./04-pages.md) | 页面清单（app 8 页 + admin 9 页） |
| [05-navigation.md](./05-navigation.md) | 导航结构（app 底部 Tab + admin 左侧栏） |
| [06-coverage-matrix.md](./06-coverage-matrix.md) | 模块 × 页面覆盖矩阵（按端分区） |
| [07-error-pages.md](./07-error-pages.md) | 错误 / 边界态 / 弹窗对照 |
| [99-open-questions.md](./99-open-questions.md) | 待确认问题 |

## 命名约定

| 类别 | 格式 |
|------|------|
| page-id（app） | `P-app-course-NNN`（001-008）|
| page-id（admin） | `P-admin-course-NNN`（001-009）|
| 流程（共享） | `FL-course-NN` / `FX-course-NN` |
| 流程（app 独有） | `F-app-course-N` |
| 流程（admin 独有） | `F-admin-course-N` |
| 状态机 | `SM-course-<域>` |

## 边界

- 本层只产出"页面清单 / 流程 / 状态机 / 导航 / 覆盖矩阵 / 错误页"，不写字段、不写接口、不写代码。
- 字段定义回引 `C01-requirements/course/baseline.md`；视觉组件回引 `B02-experience-design/design-system/`。

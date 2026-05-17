<!-- TARGET-PATH: docs/C02-ia-interaction/course/report/00-index.md -->

# IA 与交互规范 · report

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`course`
> **功能**：`report`
> **上游依赖**：`C01-requirements/course/report/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

横跨 app 与 admin：**app** 端学习者在答题页提交题目举报（浮层）；**admin** 端管理员审核举报列表并处置（忽略 / 修改题目）。两端通过 `course_reports` 表协作。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-course-report-app`（app 端）、`M-course-report`（admin 端）|
| 页面 P-ID | P-app-course-003（举报浮层寄宿页）、P-admin-course-006 |
| 覆盖 R-ID | R-course-018, R-course-024 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-admin-course-006）|

> 流程图、状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。

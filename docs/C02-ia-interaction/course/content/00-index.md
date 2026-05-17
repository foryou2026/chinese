<!-- TARGET-PATH: docs/C02-ia-interaction/course/content/00-index.md -->

# IA 与交互规范 · content

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`course`
> **功能**：`content`
> **上游依赖**：`C01-requirements/course/content/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

admin 端**内容骨架与编辑**：轨道 / 阶段 / 章节 / 节（lesson）/ 知识点（KP）/ 题目的 CRUD，含拖拽排序、5 语 i18n 校验、行级 RLS 审计。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-course-content`、`M-course-i18n-perm-admin` |
| 页面 P-ID | P-admin-course-001, P-admin-course-002, P-admin-course-003, P-admin-course-004, P-admin-course-005 |
| 覆盖 R-ID | R-course-013~017, R-course-022, R-course-023, R-course-024 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-admin-course-001~005）|

> 流程图、状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。

<!-- TARGET-PATH: docs/C02-ia/course/00-index.md -->

# C02 · IA 索引 · course

> **阶段**:C02-I · **feature**:`course` · **冻结状态**:已冻结 · 2026-05-16
> **上游**:[`C01-requirements/course/baseline.md`](../../C01-requirements/course/baseline.md)
> **下游**:C03 页面 / C04 原型 / C05 PRD

---

## 子文件导航

| 文件 | 内容 |
|------|------|
| [01-feature-catalog.md](./01-feature-catalog.md) | 10 个 M 模块 |
| [02-flows.md](./02-flows.md) | 13 个 Flow-ID(6 主 + 7 异) |
| [03-state-machines.md](./03-state-machines.md) | 7 个 SM(节进度 / 内容发布 / 答题 / SRS 盒 / 考试 attempt / 表单脏 / 离线队列) |
| [04-pages.md](./04-pages.md) | 17 个 page-id(8 应用端 + 9 管理端) |
| [05-navigation.md](./05-navigation.md) | 应用端 5 Tab + 管理端 9 大模块菜单 |
| [06-coverage-matrix.md](./06-coverage-matrix.md) | R×M×Page / Flow×Page / SM×Page |
| [07-error-pages.md](./07-error-pages.md) | 空 / 403 订阅 / 404 / 410 下架 / 5xx / 离线 + D 弹窗对照表 |
| [99-open-questions.md](./99-open-questions.md) | 待确认 |

## 命名约定

- page-id:`P-<surface>-course-<seq3>`(app 8 + admin 9 = 17,与 [`function/02-course/ai/F3-AI-页面交互规范/00-index.md`](../../../../function/02-course/ai/F3-AI-页面交互规范/00-index.md) `P-C-*` / `P-A-*` 一一映射,见 [04-pages.md](./04-pages.md))
- M-ID:`M-course-<功能区>`
- Flow-ID:`FL-course-<seq2>` / 异常 `FX-course-<seq2>`
- SM-ID:`SM-course-<域>`
- D-ID(弹窗):沿用遗留 `D-1..D-18`,见 [07-error-pages.md §D 表](./07-error-pages.md)

<!-- TARGET-PATH: docs/C03-ia/course/00-index.md -->

# C03 · IA 索引 · course

> **阶段**:C03-I · **feature**:`course` · **冻结状态**:已冻结 · 2026-05-16
> **上游**:[`C01-requirements/course/baseline.md`](../../C01-requirements/course/baseline.md)
> **下游**:C03 页面 / C04 原型 / C05 PRD

---

## 子文件导航

| 文件 | 内容 |
|------|------|
| [`app/01-feature-catalog.md`](./app/01-feature-catalog.md) / [`admin/01-feature-catalog.md`](./admin/01-feature-catalog.md) | 各 surface 的 M 模块（应用端 + 管理端，合计 10 M） |
| [`app/02-flows.md`](./app/02-flows.md) / [`admin/02-flows.md`](./admin/02-flows.md) | 13 个 Flow-ID(6 主 + 7 异)按 surface 拆分 |
| [`_shared/state-machines.md`](./_shared/state-machines.md) | 7 个 SM(节进度 / 内容发布 / 答题 / SRS 盒 / 考试 attempt / 表单脏 / 离线队列) |
| [`app/04-pages.md`](./app/04-pages.md) / [`admin/04-pages.md`](./admin/04-pages.md) | 17 个 page-id(8 应用端 + 9 管理端) |
| [`app/05-navigation.md`](./app/05-navigation.md) / [`admin/05-navigation.md`](./admin/05-navigation.md) | 应用端 5 Tab + 管理端 9 大模块菜单 |
| [`app/06-coverage-matrix.md`](./app/06-coverage-matrix.md) / [`admin/06-coverage-matrix.md`](./admin/06-coverage-matrix.md) | R×M×Page / Flow×Page / SM×Page |
| [07-error-pages.md](./07-error-pages.md) | 空 / 403 订阅 / 404 / 410 下架 / 5xx / 离线 + D 弹窗对照表（跨 surface 共享） |
| [99-open-questions.md](./99-open-questions.md) | 待确认 |

## 命名约定

- page-id:`P-<surface>-course-<seq3>`(app 8 + admin 9 = 17,与 〔历史素材〕 `P-C-*` / `P-A-*` 一一映射,见 [`app/04-pages.md`](./app/04-pages.md) / [`admin/04-pages.md`](./admin/04-pages.md))
- M-ID:`M-course-<功能区>`
- Flow-ID:`FL-course-<seq2>` / 异常 `FX-course-<seq2>`
- SM-ID:`SM-course-<域>`
- D-ID(弹窗):沿用遗留 `D-1..D-18`,见 [07-error-pages.md §D 表](./07-error-pages.md)

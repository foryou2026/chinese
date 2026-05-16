<!-- TARGET-PATH: docs/C02-ia/discover-china/00-index.md -->

# C02 · IA 索引 · discover-china

> **阶段**:C02-I · **feature**:`discover-china` · **冻结状态**:已冻结 · 2026-05-16
> **上游**:[`C01-requirements/discover-china/baseline.md`](../../C01-requirements/discover-china/baseline.md)
> **下游**:C03 页面 / C04 原型 / C05 PRD

---

## 子文件导航

| 文件 | 内容 |
|------|------|
| [01-feature-catalog.md](./01-feature-catalog.md) | 5 个 M 模块 |
| [02-flows.md](./02-flows.md) | 13 个 Flow-ID(6 主 + 7 异) |
| [_shared/state-machines.md](./_shared/state-machines.md) | 4 个 SM(文章发布 / 音频生成 / 表单脏 / TTS 播放器) |
| [04-pages.md](./04-pages.md) | 7 个 page-id |
| [05-navigation.md](./05-navigation.md) | 应用端 Tab + 面包屑;管理端侧栏 + 面包屑 |
| [06-coverage-matrix.md](./06-coverage-matrix.md) | R × M × Page;Flow × Page;SM × Page |
| [07-error-pages.md](./07-error-pages.md) | 空 / 404 / 5xx / 登录引导 / 下架占位 |
| [99-open-questions.md](./99-open-questions.md) | 待确认 |

---

## 命名约定

- page-id:`P-<surface>-discover-china-<seq3>`(app 3 + admin 4 = 7)
- M-ID:`M-<surface>-discover-<功能区>`
- Flow-ID:`FL-discover-china-<seq2>`
- SM-ID:`SM-discover-china-<seq2>`
- D-ID(弹窗):沿用遗留 `D-1..D-8`,在 [`07-error-pages.md §6`](./07-error-pages.md) 列出对照表

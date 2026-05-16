<!-- TARGET-PATH: docs/C02-ia/discover-china/06-coverage-matrix.md -->

# 06 · 覆盖矩阵

> **ID 缩写约定**:本文件内 `R-NNN` = `R-discover-china-NNN`;`P-app-NNN` / `P-admin-NNN` = `P-app-discover-china-NNN` / `P-admin-discover-china-NNN`;`FL-NN` = `FL-discover-china-NN`;`SM-NN` = `SM-discover-china-NN`。完整 ID 见 [`C01/baseline.md`](../../C01-requirements/discover-china/baseline.md) 与本目录 [`02-flows.md`](./02-flows.md) / [`03-state-machines.md`](./03-state-machines.md) / [`04-pages.md`](./04-pages.md)。

## R × Page

| R-ID | P-app-001 | P-app-002 | P-app-003 | P-admin-001 | P-admin-002 | P-admin-003 | P-admin-004 |
|------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| R-001 | ● | | | | | | |
| R-002 | | ● | | | | | |
| R-003 | | | ● | | | | |
| R-004 | | | ● | | | | |
| R-005 | | | ● | | | | |
| R-006 | | | ● | | | | |
| R-007 | | ● | ● | | | | |
| R-008 | | | | ● | | | |
| R-009 | | | | | ● | | |
| R-010 | | | | | | ● | |
| R-011 | | | | | | ● | |
| R-012 | | | | | | ● | |
| R-013 | | | | | ● | ● | |
| R-014 | | | | | ● | ● | |
| R-015 | | | | | | ● | |
| R-016 | | | | ● | ● | ● | ● |
| R-017 | | | | | | ● | |
| R-018 | | | | ● | | | |
| R-019 | | | | | ● | ● | |
| R-020 | ● | | | | | | |

> 20 R-ID 全部至少落地一个 page-id ✅

## Flow × Page

| Flow-ID | 涉及 page-id |
|---------|-------------|
| FL-01 | P-app-001 → P-app-002 → P-app-003 |
| FL-02 | P-app-003 |
| FL-03 | P-app-003 |
| FL-04 | P-admin-002 → P-admin-003 |
| FL-05 | P-admin-003 |
| FL-06 | P-admin-001..003 → P-admin-004 |
| FL-07 | P-app-001 |
| FL-08 | P-app-003 |
| FL-09 | P-app-003 → P-app-002 |
| FL-10 | P-admin-003 |
| FL-11 | P-admin-003 |
| FL-12 | P-admin-001 |
| FL-13 | P-admin-003 |

## SM × Page

| SM-ID | 主消费 page |
|-------|-------------|
| SM-01 文章发布 | P-admin-002, P-admin-003 |
| SM-02 TTS 音频生成 | P-app-003 |
| SM-03 表单脏 | P-admin-003 |
| SM-04 应用端 TTS 播放器 | P-app-003 |

<!-- TARGET-PATH: docs/C02-ia-interaction/course/06-coverage-matrix.md -->

# 覆盖矩阵

> **阶段**：C02-IN · **功能**：`course`
> **冻结状态**：已冻结 · 2026-05-16
>
> ✓=主要 · ○=辅助 · —=不涉及

---

## app 端（M × P）

| M-ID \ P-ID | P-001 | P-002 | P-003 | P-004 | P-005 | P-006 | P-007 | P-008 |
|-------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| M-course-learning | ✓ | ✓ | ✓ | — | — | — | — | ○ |
| M-course-srs | ○ | — | ○ | ✓ | ✓ | — | — | — |
| M-course-exam | ○ | — | — | — | — | ✓ | ✓ | ✓ |
| M-course-onboarding | ✓ | — | — | — | — | — | — | — |
| M-course-report-app | — | ○ | ✓ | — | — | — | — | — |
| M-course-profile | ○ | — | — | — | — | — | — | ✓ |
| M-course-i18n-perm-app | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

核验：每 M-ID ≥1 ✓ · 每 P-ID ≥1 ✓ 全过。

---

## admin 端（M × P）

| M-ID \ P-ID | P-001 | P-002 | P-003 | P-004 | P-005 | P-006 | P-007 | P-008 | P-009 |
|-------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| M-course-content | ✓ | ✓ | ✓ | ✓ | ✓ | — | ○ | ○ | — |
| M-course-media | — | — | — | ○ | ○ | — | ✓ | ○ | — |
| M-course-report | — | — | — | — | ○ | ✓ | — | — | — |
| M-course-exam-admin | — | — | — | — | ○ | — | ○ | ✓ | — |
| M-course-search | — | — | — | — | — | — | — | — | ✓ |
| M-course-i18n-perm-admin | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

核验：每 M-ID ≥1 ✓ · 每 P-ID ≥1 ✓ 全过。

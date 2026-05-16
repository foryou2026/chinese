<!-- TARGET-PATH: docs/C02-ia/course/admin/06-coverage-matrix.md -->

> **本文件为 surface=`admin` 的视角拷贝(Round 1 物理拆分初版,Round 3+ 将按端过滤实质内容)。** 跨端通用部分见 [_shared/flows-shared.md](../_shared/flows-shared.md) 与 [_shared/state-machines.md](../_shared/state-machines.md)。


# 06 · 覆盖矩阵 · course

> ID 缩写:R=Requirement、M=Module、P=Page、Flow=Flow-ID、SM=StateMachine、D=Dialog

## R × M

| R-ID | M-ID |
|------|------|
| R-001 | M-course-learning, M-course-i18n-perm |
| R-002 | M-course-onboarding |
| R-003 | M-course-learning |
| R-004 | M-course-learning |
| R-005 | M-course-learning |
| R-006 | M-course-learning |
| R-007 | M-course-learning |
| R-008 | M-course-learning, M-course-srs |
| R-009 | M-course-srs |
| R-010 | M-course-srs |
| R-011 | M-course-exam |
| R-012 | M-course-profile |
| R-013..R-017 | M-course-content |
| R-018 | M-course-report |
| R-019 | M-course-media |
| R-020 | M-course-exam |
| R-021 | M-course-search |
| R-022 | M-course-content |
| R-023 | M-course-content |
| R-024 | M-course-report |
| R-025 | M-course-exam |
| R-026 | M-course-srs |
| R-027 | M-course-exam |
| R-028..R-030 | M-course-i18n-perm |

## R × Page

| R-ID | P-ID |
|------|------|
| R-001 | P-app-course-001, P-app-course-008 |
| R-002 | P-app-course-001 |
| R-003 | P-app-course-001 |
| R-004 | P-app-course-002 |
| R-005 | P-app-course-002, P-app-course-003 |
| R-006 | P-app-course-002 |
| R-007 | P-app-course-002, P-app-course-003, P-app-course-004, P-app-course-007 |
| R-008 | P-app-course-002 |
| R-009 | P-app-course-004 |
| R-010 | P-app-course-005 |
| R-011 | P-app-course-006, P-app-course-007 |
| R-012 | P-app-course-008 |
| R-013 | P-admin-course-001 |
| R-014 | P-admin-course-002 |
| R-015 | P-admin-course-003 |
| R-016 | P-admin-course-004 |
| R-017 | P-admin-course-005 |
| R-018 | P-admin-course-006 |
| R-019 | P-admin-course-007 |
| R-020 | P-admin-course-008 |
| R-021 | P-admin-course-009 |
| R-022 | P-admin-course-004, P-admin-course-005 |
| R-023 | P-admin-course-002, P-admin-course-003 |
| R-024 | P-admin-course-006, P-admin-course-005 |
| R-025 | P-admin-course-005, P-admin-course-008 |
| R-026 | 横切(系统副作用)|
| R-027 | 横切(系统副作用)|
| R-028..030 | 横切 |

## Flow × Page

| Flow | P-ID |
|------|------|
| FL-course-01 | P-admin-course-002, 003, 004, 005, 007, 008 |
| FL-course-02 | P-app-course-002, 003 |
| FL-course-03 | P-app-course-004 |
| FL-course-04 | P-app-course-006, 007 |
| FL-course-05 | P-admin-course-005, 006 · 答题反馈 D-14 |
| FL-course-06 | P-app-course-001 |
| FX-course-01 | P-app-course-002, 004, 007 |
| FX-course-02 | P-admin-course-008 |
| FX-course-03 | P-admin-course-005, P-app-course-007 |
| FX-course-04 | P-admin-course-007 |
| FX-course-05 | P-app-course-006 |
| FX-course-06 | P-app-course-002 |
| FX-course-07 | P-admin-course-004, 005 |

## SM × Page

| SM | P-ID |
|----|------|
| SM-course-lesson-progress | P-app-course-001, 002 |
| SM-course-content-publish | P-admin-course-002, 003, 004, 005 |
| SM-course-answer | P-app-course-002, 004, 007 |
| SM-course-srs | P-app-course-004 |
| SM-course-exam-attempt | P-app-course-006, 007 |
| SM-course-form-dirty | P-admin-course-003, 004, 005, 008 |
| SM-course-offline-queue | P-app-course-002, 004, 007 |

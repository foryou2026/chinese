<!-- TARGET-PATH: docs/C02-ia/course/app/04-pages.md -->

# 04 · 页面清单(P-ID) · course / **app**

> Round 5 按端过滤。详细规范在 [C03-pages/course/app/](../../../C03-pages/course/app/) 同名文件。

| P-ID | 标题 | 路由 | 关联 M-ID | 主要 OP |
|------|------|------|----------|---------|
| P-app-course-001 | 首页 / 轨道选择 | `/learn` | M-learning · M-onboarding · M-profile | OP-course-app-001..003 |
| P-app-course-002 | 节(lesson) | `/learn/lessons/:id` | M-learning | OP-course-app-004, 005 |
| P-app-course-003 | 答题(quiz) | `/learn/lessons/:id/quiz` | M-learning · M-report-app | OP-course-app-009, 010, 017 |
| P-app-course-004 | SRS 复习队列 | `/learn/srs` | M-srs | OP-course-app-011 |
| P-app-course-005 | 错题本 | `/learn/wrong` | M-srs | OP-course-app-012 |
| P-app-course-006 | 考试列表 | `/learn/exams` | M-exam | OP-course-app-013, 014 |
| P-app-course-007 | 考试进行 | `/learn/exams/:id/attempt/:aid` | M-exam | OP-course-app-015 |
| P-app-course-008 | 考试报告 / 个人统计 | `/learn/exams/:aid/report` · `/me/stats` | M-exam · M-profile | OP-course-app-016 |

共 **8 页**。覆盖矩阵见 [06-coverage-matrix.md](06-coverage-matrix.md)。

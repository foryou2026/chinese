<!-- TARGET-PATH: docs/C02-ia/course/app/01-feature-catalog.md -->

# 01 · 功能模块清单(M-ID) · course / **app**

> Round 5 按端过滤:仅列出 app 端涉及的模块。完整全端清单见根 [../00-index.md](../00-index.md);admin 端镜像见 [../admin/01-feature-catalog.md](../admin/01-feature-catalog.md);跨端共享流程见 [_shared/flows-shared.md](../_shared/flows-shared.md)。

## 1. app 端模块清单

| M-ID | 名称 | 涵盖 R-ID | 关联 P-ID(本端) |
|------|------|----------|----------------|
| **M-course-learning** | 节内学习与首页 | R-001, 003, 004, 005, 006, 007, 008 | P-app-course-001, 002, 003 |
| **M-course-srs** | SRS 复习与错题本 | R-008, 009, 010, 026 | P-app-course-004, 005 |
| **M-course-exam** | 考试中心(4 类) | R-011, 020, 025, 027 | P-app-course-006, 007, 008 |
| **M-course-onboarding** | 引导 / 定级 / 订阅 | R-002, 028 | P-app-course-001(首屏子流) |
| **M-course-report-app** | 学员举报入口(浮层) | R-018 | 答题反馈弹窗 D-14(P-app-course-002/003/006) |
| **M-course-profile** | 个人统计 / 设置 | R-001, 012 | P-app-course-008 |
| **M-course-i18n-perm-app** | 5 语 + 主题切换 + RLS 边界 | R-028, 029 | 横切 8 页 |

> **不在 app 端**(纯 admin):M-course-content / M-course-media / M-course-search / M-course-report(审核侧)。

## 2. 上下游

- 上游:[D01-data/data-model.md](../../../D01-data/data-model.md)(`course_lessons` / `course_kps` / `course_questions` / `course_srs_*` / `course_exam_*`)。
- 下游:[D02-api/course/app](../../../D02-api/course/app/01-routes-delta.md)(17 endpoint)、[C03-pages/course/app/](../../../C03-pages/course/app/)、[C04-prototype/course/app/](../../../C04-prototype/course/app/)。

## 3. 模块边界

- **M-course-learning** vs **M-course-srs**:节内"再做一遍"走 quiz 上下文;次日推送走 SRS 队列;两者共享答题写表(`course_answers`)但分别更新不同游标。
- **M-course-exam** 独立于 SRS:作弊检测、题目顺序锁、提交后报告;答题不进 SRS。

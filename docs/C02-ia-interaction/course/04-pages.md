<!-- TARGET-PATH: docs/C02-ia-interaction/course/04-pages.md -->

# 页面清单

> **阶段**：C02-IN · **功能**：`course`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端（8 页）

| page-id | 标题 | 关联模块 | 主要操作（OP） |
|---------|------|---------|--------------|
| P-app-course-001 | 首页 / 轨道选择 | M-course-learning · M-course-onboarding · M-course-profile | OP-course-app-001~003 |
| P-app-course-002 | 节（lesson）| M-course-learning | OP-course-app-004/005 |
| P-app-course-003 | 答题（quiz）| M-course-learning · M-course-report-app | OP-course-app-009/010/017 |
| P-app-course-004 | SRS 复习队列 | M-course-srs | OP-course-app-011 |
| P-app-course-005 | 错题本 | M-course-srs | OP-course-app-012 |
| P-app-course-006 | 考试列表 | M-course-exam | OP-course-app-013/014 |
| P-app-course-007 | 考试进行 | M-course-exam | OP-course-app-015 |
| P-app-course-008 | 考试报告 / 个人统计 | M-course-exam · M-course-profile | OP-course-app-016 |

---

## admin 端（9 页）

| page-id | 标题 | 关联模块 | 主要操作（OP） |
|---------|------|---------|--------------|
| P-admin-course-001 | 轨道列表 | M-course-content · M-course-i18n-perm-admin | OP-course-admin-001 |
| P-admin-course-002 | 阶段编辑 | M-course-content | OP-course-admin-002 |
| P-admin-course-003 | 章节编辑（拖拽）| M-course-content | OP-course-admin-003 |
| P-admin-course-004 | 节编辑 + KP 绑定 | M-course-content | OP-course-admin-004 |
| P-admin-course-005 | 题目 / 知识点 CRUD | M-course-content | OP-course-admin-005~014 |
| P-admin-course-006 | 学员举报审核 | M-course-report | OP-course-admin-018/019 |
| P-admin-course-007 | 媒资库 | M-course-media | OP-course-admin-020~022 |
| P-admin-course-008 | 考试编辑与预览 | M-course-exam-admin | OP-course-admin-016/022 |
| P-admin-course-009 | 全局搜索 + 统计 | M-course-search | OP-course-admin-023/024 |

> URL / 路由属 D02-L 产出，本阶段不定义。

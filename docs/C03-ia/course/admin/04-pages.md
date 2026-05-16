<!-- TARGET-PATH: docs/C03-ia/course/admin/04-pages.md -->

# 04 · 页面清单(P-ID) · course / **admin**

> Round 5 按端过滤。详细规范在 [C04-pages/course/admin/](../../../C04-pages/course/admin/) 同名文件。

| P-ID | 标题 | 路由 | 关联 M-ID | 主要 OP |
|------|------|------|----------|---------|
| P-admin-course-001 | 轨道列表 | `/admin/course/tracks` | M-content · M-i18n-perm-admin | OP-course-admin-001 |
| P-admin-course-002 | 阶段编辑 | `/admin/course/tracks/:t/stages` | M-content | OP-course-admin-002 |
| P-admin-course-003 | 章节编辑(拖拽) | `/admin/course/stages/:s/chapters` | M-content | OP-course-admin-003 |
| P-admin-course-004 | 节编辑 + KP 绑定 | `/admin/course/chapters/:c/lessons` | M-content | OP-course-admin-004 |
| P-admin-course-005 | 题目 / 知识点 CRUD | `/admin/course/{questions,kps}` | M-content | OP-course-admin-005..014 |
| P-admin-course-006 | 学员举报审核 | `/admin/course/reports` | M-report | OP-course-admin-018, 019 |
| P-admin-course-007 | 媒资库 | `/admin/course/media` | M-media | OP-course-admin-020, 021, 022 |
| P-admin-course-008 | 考试编辑与预览 | `/admin/course/exams` | M-exam-admin | OP-course-admin-016, 022 |
| P-admin-course-009 | 全局搜索 + 统计 | `/admin/course/search` · `/stats` | M-search | OP-course-admin-023, 024 |

共 **9 页**。

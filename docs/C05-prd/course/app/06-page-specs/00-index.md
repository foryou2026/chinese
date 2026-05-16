<!-- TARGET-PATH: docs/C05-prd/course/app/06-page-specs/00-index.md -->

> **本文件为 surface=`app` 视角的页面规格索引(Round 2 从 PRD.md 第 6 章拆出初版,后续 Round 4+ 将按 page-id 展开单页 spec 文件)。**

## 6. 页面清单与原型

| page-id | 路由 | 规格 | 原型(F4 源)|
|---------|------|------|------|
| P-app-course-001 | `/` 或 `/home` | [规格](../../C03-pages/course/P-app-course-001.md) | F4 `_assets/` + P-C-1 顶部 |
| P-app-course-002 | `/learn/...` | [规格](../../C03-pages/course/P-app-course-002.md) | [F4 P-C-1](../../../function/02-course/ai/F4-AI-原型设计/P-C-1-学习地图.html) + [F4 P-C-2](../../../function/02-course/ai/F4-AI-原型设计/P-C-2-节学习页.html) |
| P-app-course-003 | `/lesson/{code}/kp/{id}` | [规格](../../C03-pages/course/P-app-course-003.md) | F4 P-C-2 节学习页内卡片 |
| P-app-course-004 | `/review` | [规格](../../C03-pages/course/P-app-course-004.md) | [F4 P-C-4](../../../function/02-course/ai/F4-AI-原型设计/P-C-4-SRS复习.html) |
| P-app-course-005 | `/wrong` | [规格](../../C03-pages/course/P-app-course-005.md) | [F4 P-C-5](../../../function/02-course/ai/F4-AI-原型设计/P-C-5-错题本.html) |
| P-app-course-006 | `/exam` | [规格](../../C03-pages/course/P-app-course-006.md) | [F4 P-C-6](../../../function/02-course/ai/F4-AI-原型设计/P-C-6-考试中心.html) |
| P-app-course-007 | `/exam/{attemptId}` | [规格](../../C03-pages/course/P-app-course-007.md) | [F4 P-C-7](../../../function/02-course/ai/F4-AI-原型设计/P-C-7-考试进行.html) |
| P-app-course-008 | `/me` | [规格](../../C03-pages/course/P-app-course-008.md) | [F4 P-C-8](../../../function/02-course/ai/F4-AI-原型设计/P-C-8-个人统计.html) |
| P-admin-course-001 | `/admin/course` | [规格](../../C03-pages/course/P-admin-course-001.md) | [F4 P-A-1](../../../function/02-course/ai/F4-AI-原型设计/P-A-1-课程目录总览.html) |
| P-admin-course-002 | `/admin/course/tree` | [规格](../../C03-pages/course/P-admin-course-002.md) | [F4 P-A-2](../../../function/02-course/ai/F4-AI-原型设计/P-A-2-主题-阶段-章列表.html) |
| P-admin-course-003 | `/admin/course/lesson/{code}` | [规格](../../C03-pages/course/P-admin-course-003.md) | [F4 P-A-3](../../../function/02-course/ai/F4-AI-原型设计/P-A-3-节编辑.html) |
| P-admin-course-004 | `/admin/course/kp` | [规格](../../C03-pages/course/P-admin-course-004.md) | [F4 P-A-4](../../../function/02-course/ai/F4-AI-原型设计/P-A-4-KP列表.html) |
| P-admin-course-005 | `/admin/course/question` | [规格](../../C03-pages/course/P-admin-course-005.md) | [F4 P-A-5](../../../function/02-course/ai/F4-AI-原型设计/P-A-5-题目列表.html) |
| P-admin-course-006 | `/admin/course/report` | [规格](../../C03-pages/course/P-admin-course-006.md) | [F4 P-A-6](../../../function/02-course/ai/F4-AI-原型设计/P-A-6-举报处理.html) |
| P-admin-course-007 | `/admin/course/media` | [规格](../../C03-pages/course/P-admin-course-007.md) | [F4 P-A-7](../../../function/02-course/ai/F4-AI-原型设计/P-A-7-媒资库.html) |
| P-admin-course-008 | `/admin/course/exam` | [规格](../../C03-pages/course/P-admin-course-008.md) | [F4 P-A-8](../../../function/02-course/ai/F4-AI-原型设计/P-A-8-考试中心管理.html) |
| P-admin-course-009 | `/admin/course/search` | [规格](../../C03-pages/course/P-admin-course-009.md) | [F4 P-A-9](../../../function/02-course/ai/F4-AI-原型设计/P-A-9-全局搜索.html) |

弹窗 D-1..D-18 详 [`C02/07-error-pages.md §2`](../../C02-ia/course/07-error-pages.md)。

## 待办
- [ ] Round 4: 按 page-id 创建 `06-page-specs/<page-id>.md`,每页对齐 C03-pages/course/app/{page-id}.md

<!-- TARGET-PATH: docs/C03-ia/course/admin/01-feature-catalog.md -->

# 01 · 功能模块清单(M-ID) · course / **admin**

> Round 5 按端过滤。app 端镜像见 [../app/01-feature-catalog.md](../app/01-feature-catalog.md)。

## 1. admin 端模块清单

| M-ID | 名称 | 涵盖 R-ID | 关联 P-ID(本端) |
|------|------|----------|----------------|
| **M-course-content** | 内容骨架与编辑(轨道/阶段/章节/节/KP/题) | R-013, 014, 015, 016, 017, 022, 023 | P-admin-course-001, 002, 003, 004, 005 |
| **M-course-media** | 媒资库与去重 | R-019 | P-admin-course-007 |
| **M-course-report** | 学员举报审核闭环 | R-018, 024 | P-admin-course-006 |
| **M-course-exam-admin** | 考试编辑与预览 | R-011, 020, 025, 027 | P-admin-course-008 |
| **M-course-search** | 全局搜索 + 统计概览 | R-021 | P-admin-course-009 |
| **M-course-i18n-perm-admin** | 5 语校验 + 主题范围 列级权限 + 行级审计 | R-028, 029, 030 | 横切 9 页 |

> **不在 admin 端**(纯 app):M-course-learning / M-course-srs / M-course-exam(参考侧) / M-course-onboarding / M-course-profile。

## 2. 上下游

- 上游:[D01-data](../../../D01-data/data-model.md);[B02 角色](../../../C02-permissions/01-roles.md) `admin.主题范围`。
- 下游:[D02-api/course/admin](../../../D02-api/course/admin/01-routes-delta.md)(24 endpoint)、[C04-pages/course/admin/](../../../C04-pages/course/admin/)、[C05-prototype/course/admin/](../../../C05-prototype/course/admin/)。

## 3. 模块边界

- **M-course-content** vs **M-course-media**:内容编辑器内嵌资源选择器调用媒资 endpoint,不重复上传管理。
- **M-course-report**(审核)与 app 端 `M-course-report-app`(举报入口)通过 `course_reports` 表协作:app insert,admin list + 处置;状态机见 [_shared/state-machines.md](../_shared/state-machines.md#course-report)。

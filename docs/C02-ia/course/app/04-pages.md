<!-- TARGET-PATH: docs/C02-ia/course/app/04-pages.md -->

> **本文件为 surface=`app` 的视角拷贝(Round 1 物理拆分初版,Round 3+ 将按端过滤实质内容)。** 跨端通用部分见 [_shared/flows-shared.md](../_shared/flows-shared.md) 与 [_shared/state-machines.md](../_shared/state-machines.md)。


# 04 · 页面清单(P-ID) · course

> 与 [`function/02-course/ai/F3-AI-页面交互规范/00-index.md`](../../../../function/02-course/ai/F3-AI-页面交互规范/00-index.md) `P-C-*` / `P-A-*` 一一映射。

## 应用端(8)

| 文档 P-ID | F3 P-ID | 名称 | 主路由 | R-ID |
|----------|---------|------|--------|------|
| `P-app-course-001` | `P-C-1` | 首页 / 主题切换 / 引导入口 | `/` 或 `/home` | R-001/002/003 |
| `P-app-course-002` | `P-C-2` | 学习地图 + 节内学习 | `/learn/:track/:stage/:chapter/:lesson` | R-004..008 |
| `P-app-course-003` | `P-C-3` | KP 详情 / 卡片浏览 | `/lesson/:code/kp/:kpId` | R-005/007 |
| `P-app-course-004` | `P-C-4` | SRS 今日复习 | `/review` | R-009/026 |
| `P-app-course-005` | `P-C-5` | 错题本 | `/wrong` | R-010 |
| `P-app-course-006` | `P-C-6` | 考试中心入口 + 列表 | `/exam` | R-011 |
| `P-app-course-007` | `P-C-7` | 考试答题 / 倒计时 | `/exam/:attemptId` | R-011 |
| `P-app-course-008` | `P-C-8` | 我的(统计/账单/设置)| `/me` | R-012 |

## 管理端(9)

| 文档 P-ID | F3 P-ID | 名称 | 主路由 | R-ID |
|----------|---------|------|--------|------|
| `P-admin-course-001` | `P-A-1` | 课程目录总览 | `/admin/course` | R-013 |
| `P-admin-course-002` | `P-A-2` | 主题-阶段-章-节四级列表 | `/admin/course/tree` | R-014/023 |
| `P-admin-course-003` | `P-A-3` | 节编辑 | `/admin/course/lesson/:code` | R-015 |
| `P-admin-course-004` | `P-A-4` | KP 列表 + Drawer | `/admin/course/kp` | R-016/022 |
| `P-admin-course-005` | `P-A-5` | 题目列表 + 双开预览 | `/admin/course/question` | R-017/022/024 |
| `P-admin-course-006` | `P-A-6` | 学员举报处理 | `/admin/course/report` | R-018/024 |
| `P-admin-course-007` | `P-A-7` | 媒资库 | `/admin/course/media` | R-019 |
| `P-admin-course-008` | `P-A-8` | 考试中心管理(分层)| `/admin/course/exam` | R-020/025 |
| `P-admin-course-009` | `P-A-9` | 全局搜索 | `/admin/course/search` | R-021 |

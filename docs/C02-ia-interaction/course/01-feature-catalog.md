<!-- TARGET-PATH: docs/C02-ia-interaction/course/01-feature-catalog.md -->

# 功能模块清单

> **阶段**：C02-IN · **功能**：`course`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端模块

| M-ID | 名称 | 涵盖 R-ID | 关联 P-ID |
|------|------|----------|---------|
| M-course-learning | 节内学习与首页 | R-course-001/003-008 | P-app-course-001/002/003 |
| M-course-srs | SRS 复习与错题本 | R-course-008/009/010/026 | P-app-course-004/005 |
| M-course-exam | 考试中心（4 类）| R-course-011/020/025/027 | P-app-course-006/007/008 |
| M-course-onboarding | 引导 / 定级 / 订阅 | R-course-002/028 | P-app-course-001（首屏子流）|
| M-course-report-app | 学员举报入口（浮层）| R-course-018 | 答题反馈弹窗 D-14（P-app-course-002/003/006）|
| M-course-profile | 个人统计 / 设置 | R-course-001/012 | P-app-course-008 |
| M-course-i18n-perm-app | 5 语 + 主题切换 + RLS 边界 | R-course-028/029 | 横切 8 页 |

> 不在 app 端（纯 admin）：M-course-content / M-course-media / M-course-search / M-course-report（审核侧）。

---

## admin 端模块

| M-ID | 名称 | 涵盖 R-ID | 关联 P-ID |
|------|------|----------|---------|
| M-course-content | 内容骨架与编辑（轨道 / 阶段 / 章节 / 节 / KP / 题）| R-course-013-017/022/023 | P-admin-course-001-005 |
| M-course-media | 媒资库与去重 | R-course-019 | P-admin-course-007 |
| M-course-report | 学员举报审核闭环 | R-course-018/024 | P-admin-course-006 |
| M-course-exam-admin | 考试编辑与预览 | R-course-011/020/025/027 | P-admin-course-008 |
| M-course-search | 全局搜索 + 统计概览 | R-course-021 | P-admin-course-009 |
| M-course-i18n-perm-admin | 5 语校验 + 主题范围列级权限 + 行级审计 | R-course-028-030 | 横切 9 页 |

> 不在 admin 端（纯 app）：M-course-learning / M-course-srs / M-course-exam（参考侧）/ M-course-onboarding / M-course-profile。

---

## 模块边界说明

- **M-course-learning** vs **M-course-srs**：节内"再做一遍"走 quiz 上下文；次日推送走 SRS 队列；两者共享答题写表（`course_answers`）但分别更新不同游标。
- **M-course-exam** 独立于 SRS：作弊检测、题目顺序锁、提交后报告；答题不进 SRS。
- **M-course-report**（admin 审核侧）与 app 端 **M-course-report-app**（举报入口）通过 `course_reports` 表协作：app insert，admin list + 处置。

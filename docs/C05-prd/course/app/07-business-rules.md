<!-- TARGET-PATH: docs/C05-prd/course/app/07-business-rules.md -->

# 07 · 业务规则 · course / **app**

> R-ID 来源 [C01 PRD baseline](../../../C01-prd-baseline/baseline.md)。本文件仅列出在 app 端生效或可观察的规则。

## 学习与 SRS

| R-ID | 规则 | 实现 OP / 状态机 |
|------|------|------------------|
| R-001 | 用户必须选择 1 个轨道才能开始学习 | OP-course-app-002 / `me.current_track` |
| R-003 | 答题立即写库;离线缓存 ≤ 5 条 | OP-course-app-009 |
| R-005 | 节内"再做一遍"不进 SRS,只 reset 节内进度 | OP-course-app-010 |
| R-008 | SRS 间隔基于 SM-2 简化 | `course_srs_state` |
| R-009 | 错题进入"错题本",答对 3 次离开 | OP-course-app-012 |
| R-010 | SRS 每日上限可在订阅页调 | M-onboarding |

## 考试

| R-ID | 规则 |
|------|------|
| R-011 | 考试一旦开始不可重置(只 abandon)|
| R-020 | 考试 30 分钟无心跳自动 abandon |
| R-025 | 报告生成后题目顺序锁定,可分享 |
| R-027 | 4 类考试(节末 / 章末 / 阶段末 / 综合)各有独立提交规则 |

## 学员举报

| R-018 | 举报 24h 冷却(同题 / 同 uid)|

## 多语 / 权限

| R-028 | UI 语种切换不重新登录;音频 key 含 lang |
| R-029 | RLS 仅按 `auth.uid()`,无其他列级权限 |

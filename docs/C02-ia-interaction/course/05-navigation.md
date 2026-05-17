<!-- TARGET-PATH: docs/C02-ia-interaction/course/05-navigation.md -->

# 导航结构

> **阶段**：C02-IN · **功能**：`course`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端

### 顶层导航（底部 Tab）

```
[ 学习 ]  [ 复习 ]  [ 考试 ]  [ 我的 ]
    ↓        ↓        ↓        ↓
 P-001    P-004    P-006    P-008
```

- 一级 4 Tab + 二级页面；层级最多 3 级（Tab → 列表 → 详情）。
- 路由前缀 `/learn`；`/me/*` 独立路径但 Tab 视觉归"我的"。

### 面包屑

- 答题页（P-app-course-003）左上返回 = 弹窗"放弃当前题"，已答案不丢。
- 考试进行中（P-app-course-007）禁用浏览器返回（beforeunload 拦截）。

### 模态层

| 触发 | 类型 | 关闭策略 |
|------|------|---------|
| 选择轨道（首启）| drawer | 必须选择，无关闭 |
| 答题反馈 D-14 | bottom-sheet | 上滑或点 × |
| 订阅 / 付费 | modal | 仅可后退一次，二次后退强制提示 |

### 路由表

| Path | page-id |
|------|---------|
| `/learn` | P-app-course-001 |
| `/learn/lessons/:id` | P-app-course-002 |
| `/learn/lessons/:id/quiz` | P-app-course-003 |
| `/learn/srs` | P-app-course-004 |
| `/learn/wrong` | P-app-course-005 |
| `/learn/exams` | P-app-course-006 |
| `/learn/exams/:id/attempt/:aid` | P-app-course-007 |
| `/learn/exams/:aid/report` | P-app-course-008（报告 view）|
| `/me/stats` | P-app-course-008（统计 view）|

---

## admin 端

### 顶层导航（左侧栏）

```
课程
├─ 轨道（P-001）
├─ 题目 / 知识点（P-005）
├─ 媒资（P-007）
├─ 考试（P-008）
├─ 学员举报（P-006）
└─ 搜索 / 统计（P-009）
```

- 进入轨道后右栏出现二级：阶段（P-002）/ 章节（P-003）/ 节（P-004），面包屑 4 级。
- 路由前缀 `/admin/course/*`。

### 编辑器内层级

P-admin-course-005 知识点 / 题目共用一个编辑器，左侧树 + 右侧表单 + 顶部 Tab（KP / Q）。

### 模态层

| 触发 | 类型 | 关键约束 |
|------|------|---------|
| 删除轨道 / 章节 | 危险确认 modal | 二次输入轨道码确认 |
| 批量导入 | drawer（右）| 预览态 → 提交，过程中不可关闭 |
| 媒资替换 | modal | 显示影响 KP 数，确认才替换 |

### 路由表

| Path | page-id |
|------|---------|
| `/admin/course/tracks` | P-admin-course-001 |
| `/admin/course/tracks/:t/stages` | P-admin-course-002 |
| `/admin/course/stages/:s/chapters` | P-admin-course-003 |
| `/admin/course/chapters/:c/lessons` | P-admin-course-004 |
| `/admin/course/questions` · `/kps` | P-admin-course-005 |
| `/admin/course/reports` | P-admin-course-006 |
| `/admin/course/media` | P-admin-course-007 |
| `/admin/course/exams` | P-admin-course-008 |
| `/admin/course/search` · `/stats` | P-admin-course-009 |

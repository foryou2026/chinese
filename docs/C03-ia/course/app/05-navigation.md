<!-- TARGET-PATH: docs/C03-ia/course/app/05-navigation.md -->

# 05 · 导航与信息层级 · course / **app**

> Round 5 按端过滤。

## 顶层导航(底部 tab)

```
[ 学习 ]  [ 复习 ]  [ 考试 ]  [ 我的 ]
   ↓        ↓        ↓        ↓
P-001    P-004    P-006   P-008
```

- 一级 4 tab + 二级页面;层级最多 3 级(tab → 列表 → 详情)。
- 路由前缀 `/learn`;`/me/*` 独立路径但 tab 视觉归"我的"。

## 面包屑

- 答题页(P-003)左上返回 = 弹窗"放弃当前题",已答案不丢。
- 考试中(P-007)禁用浏览器返回(beforeunload 拦截)。

## 模态层

| 触发 | 类型 | 关闭策略 |
|------|------|---------|
| 选择轨道(首启) | drawer | 必须选择,无关闭 |
| 答题反馈 D-14 | bottom-sheet | 上滑或点 × |
| 订阅/付费 | modal | 仅可后退一次,二次后退强制提示 |

## 深链 / 路由表

| Path | P-ID |
|------|------|
| `/learn` | P-001 |
| `/learn/lessons/:id` | P-002 |
| `/learn/lessons/:id/quiz` | P-003 |
| `/learn/srs` | P-004 |
| `/learn/wrong` | P-005 |
| `/learn/exams` | P-006 |
| `/learn/exams/:id/attempt/:aid` | P-007 |
| `/learn/exams/:aid/report` | P-008(报告 view) |
| `/me/stats` | P-008(统计 view) |

<!-- TARGET-PATH: docs/C03-ia/course/admin/05-navigation.md -->

# 05 · 导航与信息层级 · course / **admin**

> Round 5 按端过滤。

## 顶层导航(左侧栏)

```
课程
├─ 轨道(P-001)
├─ 题目 / 知识点(P-005)
├─ 媒资(P-007)
├─ 考试(P-008)
├─ 学员举报(P-006)
└─ 搜索 / 统计(P-009)
```

- 进入轨道后右栏出现二级:阶段(P-002)/ 章节(P-003)/ 节(P-004),面包屑 4 级。
- 路由前缀 `/admin/course/*`。

## 编辑器内层级

P-005 知识点 / 题目共用一个编辑器,左侧树 + 右侧表单 + 顶部 tab(`KP` / `Q`)。

## 模态层

| 触发 | 类型 | 关键约束 |
|------|------|---------|
| 删除轨道 / 章节 | 危险确认 modal | 二次输入轨道码确认(`super`) |
| 批量导入 | drawer(右) | 预览态 → 提交,过程中不可关闭 |
| 媒资替换 | modal | 显示影响 KP 数,确认才替换 |

## 深链 / 路由表

| Path | P-ID |
|------|------|
| `/admin/course/tracks` | P-001 |
| `/admin/course/tracks/:t/stages` | P-002 |
| `/admin/course/stages/:s/chapters` | P-003 |
| `/admin/course/chapters/:c/lessons` | P-004 |
| `/admin/course/questions` · `/kps` | P-005 |
| `/admin/course/reports` | P-006 |
| `/admin/course/media` | P-007 |
| `/admin/course/exams` | P-008 |
| `/admin/course/search` · `/stats` | P-009 |

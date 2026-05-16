<!-- TARGET-PATH: docs/C06-prd/course/admin/01-overview.md -->

# 01 · 总览 · course / **admin**

> 跨端共享真相在 [`../_shared/`](../_shared/);本文件聚焦 admin 端独有视角。

## 1.1 admin 端定位

`course` admin 端是 **内容运营 + 内容点检 + 发布管控** 三位一体的后台，仅服务 `admin`（遵从 [docs/C02-permissions/01-roles.md](../../../C02-permissions/01-roles.md) 的 2 角色硬约束）。**不是** 学员侧产品的镜像，而是「线下批量生成 → 导入 → 人工点检 → 上架」流水线的可视化与控制面。

## 1.2 admin 端 9 大模块

| # | 模块 | 主页面 |
|---|------|--------|
| 1 | 主题/阶段/章/节骨架 | [P-001](06-page-specs/P-admin-course-001.md) + [P-002](06-page-specs/P-admin-course-002.md) + [P-003](06-page-specs/P-admin-course-003.md) |
| 2 | 节 + KP 绑定 | [P-004](06-page-specs/P-admin-course-004.md) |
| 3 | 题库(7 类 KP × 12 题型) | [P-005](06-page-specs/P-admin-course-005.md) |
| 4 | 学员举报审核 | [P-006](06-page-specs/P-admin-course-006.md) |
| 5 | 媒资库(音/图) | [P-007](06-page-specs/P-admin-course-007.md) |
| 6 | 考试中心(节/章/阶段) | [P-008](06-page-specs/P-admin-course-008.md) |
| 7 | 全局搜索 + 统计 | [P-009](06-page-specs/P-admin-course-009.md) |
| 8 | 批量导入/导出 | 在 P-001~P-008 各自 toolbar 内 |
| 9 | 发布 / 撤回 / 灰度 | 在 P-001~P-008 各页发布按钮（`admin` 同人操作，无打间审批）|

> 2025-11 变更:**删除** "系统内生成工作台"模块(原为题目自动生成 UI);题目改为完全线下批量生成 + 导入。

## 1.3 admin 端关键运营闭环

1. **生产**:线下 AI 批量出题 → 平台导入(JSON / Excel)→ 自动校验格式
2. **点检**:[P-005](06-page-specs/P-admin-course-005.md) 抽检 + 全检流;管理员可批注 / 退回
3. **发布**：[P-001~P-008](06-page-specs/) 各模块 publish/unpublish；unpublish 需二次确认
4. **运营**:[P-006](06-page-specs/P-admin-course-006.md) 举报循环 7 天结案

## 1.4 admin 端非目标

- **不** 提供学员侧学习状态查看(隐私 + 性能);仅汇总统计;
- **不** 提供 AI 实时生成(2025-11 已撤);
- **不** 提供 5 语自动翻译(必须人工填齐 5 key)。

## 1.5 性能基线(admin 端)

| 操作 | 目标 |
|------|------|
| 章节拖拽排序保存 | P95 ≤ 400 ms |
| 节 + KP 绑定批量保存 ≤ 100 条 | P95 ≤ 800 ms |
| 题目搜索 / 翻页 100 行 | P95 ≤ 500 ms |
| 媒资上传(单文件 ≤ 50 MB) | 走预签名 URL 直传对象存储 |
| 全量发布单主题 | 异步任务,< 30 s 完成 |

> admin 路由:`/api/admin/首版/*` ≡ 短路径 `/admin/首版/*`。

<!-- TARGET-PATH: docs/C05-prd/course/admin/06-page-specs/P-admin-course-006.md -->

# Page Spec · P-admin-course-006 · 学员举报审核

> PRD 视角单页规格 · course / `admin` 端。来源真相见各 C 阶段文档,本文件只做汇总与索引。

## 1. 标识

| 字段 | 值 |
|------|----|
| P-ID | `P-admin-course-006` |
| 标题 | 学员举报审核 |
| feature | `course` |
| surface | `admin` |
| 路由(规范) | 见 [C02 05-navigation.md](../../../../C02-ia/course/admin/05-navigation.md) |
| 角色可见 | 见 [C05 08-roles-permissions.md](../08-roles-permissions.md) |

## 2. 上游来源

| 维度 | 文档 |
|------|------|
| 交互规范(N) | [`C03-pages/course/admin/P-admin-course-006.md`](../../../../C03-pages/course/admin/P-admin-course-006.md) |
| 场景脚本(N) | [`C03-pages/course/admin/P-admin-course-006.scenarios.md`](../../../../C03-pages/course/admin/P-admin-course-006.scenarios.md)(若存在) |
| HTML 原型(H) | [`C04-prototype/course/admin/pages/`](../../../../C04-prototype/course/admin/pages/) |
| 状态原型 | [`C04-prototype/course/admin/states/`](../../../../C04-prototype/course/admin/states/) |
| 关联 M-ID | [`C02-ia/course/admin/01-feature-catalog.md`](../../../../C02-ia/course/admin/01-feature-catalog.md) |
| 关联 R-ID | [`07-business-rules.md`](../07-business-rules.md) |

## 3. 一句话价值

> _待补:由 PRD 撰写人在 Round 7+ 实质化(从 C01 baseline 中抽出本页对应的用户价值陈述)。_

## 4. 主交互(摘要 ≤ 5 行)

> 仅做摘要,不重复 C03 详细步骤。

1. 用户进入本页 → 加载初始数据(见上方 C03 文档第 §2 节)。
2. 主操作 → 详细见 C03 §3。
3. 异常 / 边界 → 见 C03 §5。
4. 离开 / 跳转 → 见 [`C02 02-flows.md`](../../../../C02-ia/course/admin/02-flows.md)。

## 5. 关键业务规则(仅本页相关 R-ID)

> 抽取自 [`../07-business-rules.md`](../07-business-rules.md);写明哪几条 R-* 在本页落地;PRD 撰写人 Round 7+ 实质化。

## 6. 数据 / 接口边界(展示态)

> 本字段在 D 阶段产出后再回填;当前仅占位。前端编码可直接从 C03 + C04 mock-data.js 推导。

## 7. 视觉 / 组件(↑ B04)

- 主要组件:见 [`C03-pages/course/admin/P-admin-course-006.md` §视觉与组件](../../../../C03-pages/course/admin/P-admin-course-006.md)。
- 组件契约:[`B04-design/design-system/05-components/`](../../../../B04-design/design-system/05-components/)(Round 4 已实质化)。

## 8. 截图

| 状态 | 路径 |
|------|------|
| 正常态 | `assets/screenshots/P-admin-course-006.png`(占位) |
| 空态 | 见 [`C04 states/`](../../../../C04-prototype/course/admin/states/) |
| 错误态 | 同上 |
| 加载态 | 同上 |
| 无权 | 同上 |

## 9. 变更

| 日期 | 内容 | 提交人 |
|------|------|--------|
| 2026-05-16 | Round 6 创建框架 | AI |

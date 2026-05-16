<!-- TARGET-PATH: docs/C05-prd/auth/app/06-page-specs/P-auth-003.md -->

# Page Spec · P-auth-003 · 邮箱验证 / 重发

> PRD 视角单页规格 · auth / `app` 端。来源真相见各 C 阶段文档,本文件只做汇总与索引。

## 1. 标识

| 字段 | 值 |
|------|----|
| P-ID | `P-auth-003` |
| 标题 | 邮箱验证 / 重发 |
| feature | `auth` |
| surface | `app` |
| 路由(规范) | 见 [C02 05-navigation.md](../../../../C02-ia/auth/app/05-navigation.md) |
| 角色可见 | 见 [C05 08-roles-permissions.md](../08-roles-permissions.md) |

## 2. 上游来源

| 维度 | 文档 |
|------|------|
| 交互规范(N) | [`C03-pages/auth/app/P-auth-003.md`](../../../../C03-pages/auth/app/P-auth-003.md) |
| 场景脚本(N) | [`C03-pages/auth/app/P-auth-003.scenarios.md`](../../../../C03-pages/auth/app/P-auth-003.scenarios.md)(若存在) |
| HTML 原型(H) | [`C04-prototype/auth/app/`](../../../../C04-prototype/auth/app/) |
| 关联 M-ID | [`C02-ia/auth/app/01-feature-catalog.md`](../../../../C02-ia/auth/app/01-feature-catalog.md) |
| 关联 R-ID | [`07-business-rules.md`](../07-business-rules.md) |

## 3. 一句话价值

> _待补:由 PRD 撰写人在 Round 7+ 实质化(从 C01 baseline 中抽出本页对应的用户价值陈述)。_

## 4. 主交互(摘要 ≤ 5 行)

> 仅做摘要,不重复 C03 详细步骤。

1. 用户进入本页 → 加载初始数据(见上方 C03 文档第 §2 节)。
2. 主操作 → 详细见 C03 §3。
3. 异常 / 边界 → 见 C03 §5。
4. 离开 / 跳转 → 见 [`C02 02-flows.md`](../../../../C02-ia/auth/app/02-flows.md)。

## 5. 关键业务规则(仅本页相关 R-ID)

> 抽取自 [`../07-business-rules.md`](../07-business-rules.md);写明哪几条 R-* 在本页落地;PRD 撰写人 Round 7+ 实质化。

## 6. 数据 / 接口边界(展示态)

> 本字段在 D 阶段产出后再回填;当前仅占位。前端编码可直接从 C03 + C04 HTML 静态片段推导。

## 7. 视觉 / 组件(↑ B04)

- 主要组件:见 [`C03-pages/auth/app/P-auth-003.md` §视觉与组件](../../../../C03-pages/auth/app/P-auth-003.md)。
- 组件契约:[`B04-design/design-system/05-components/`](../../../../B04-design/design-system/05-components/)(Round 4 已实质化)。

## 8. 状态文字描述

> 原型只承担默认态（见上方 H 原型链接）。空 / 加载 / 错误 / 无权限态不出图，由本节文字描述。

| 状态 | 触发 | 表现 | 文案（→ B03 voice-tone） |
|------|------|------|---------------------------|
| 默认 | 进入页面、数据正常 | 见上方 H 原型 | — |
| 加载 | 首屏数据 / 提交中 | 骨架屏 / 主按钮 loading | _待补_ |
| 空 | 列表 / 查询无结果 | 占位插画 + 主操作 CTA | _待补_ |
| 错误 | 网络 / 接口失败 | 错误图标 + 文案 + 重试 | _待补_ |
| 无权限 | 角色越权（若适用） | 无权限组件 + 返回链接 | _待补_ |

> _PRD 撰写人 Round 7+ 把上表「触发 / 表现 / 文案」实质化，参考 C03 §5 异常分支。_

## 9. 变更

| 日期 | 内容 | 提交人 |
|------|------|--------|
| 2026-05-16 | Round 6 创建框架 | AI |

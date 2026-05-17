<!-- TARGET-PATH: docs/B02-experience-design/design-system/05-components/09-avatars-badges-tags.md -->

# 05.09 · 头像 / 徽章 / 状态标签

> 状态标签上游:[`04-status-colors.md §一`](../04-status-colors.md) → 同步至 [04-status-colors.md](../04-status-colors.md)。
> ui-kit 导出:`StatusTag` / `Avatar` / `Badge`。

## 一、状态标签 `StatusTag`
> **禁止手写颜色**,必须使用 `<StatusTag status="..." />`。颜色映射见 [04-status-colors.md](../04-status-colors.md)。

| 状态语义 | 背景色 | 文字色 | 适用枚举 |
| ---- | ---- | ---- | ---- |
| 初始 / 草稿 | `--bg-active` | `--text-secondary` | `draft` / `pending` |
| 进行中 | `--bg-active` + 1px `--border-strong` 虚线 | `--text-primary` | `active` / `processing` / `in_progress` |
| 成功 | `--success-soft` | `--success` | `done` / `completed` / `success` / `paid` |
| 警告 | `--warning-soft` | `--warning` | `warning` / `pending_review` / `overdue` |
| 失败 / 拒绝 / 取消 | `--danger-soft` | `--danger` | `failed` / `rejected` / `cancelled` / `refunded` |
| 已归档 / 已关闭 | `--bg-active` | `--text-tertiary` | `archived` / `closed` |

形状:`radius-pill`,高度 22px,内边距左右 8px,字号 `text-tag`。图标可选(在文字左 4px),尺寸 12px。

## 二、头像 `Avatar`
| 尺寸 | 用途 |
| ---- | ---- |
| 24px | 表格内 / 评论列表 |
| 32px | 顶栏 / 卡片摘要 |
| 48px | 个人中心 / 卡片大图 |
| 64px | 弹窗 / 详情页头部 |

- 形状:`radius-full`(圆形)。
- 占位:无头像时显示首字符 + `--brand-soft` 底 + `--brand` 字。
- 边框:可选 2px `--bg-elevated`(用于头像堆叠时)。

## 三、徽章 `Badge`
| 类型 | 形态 |
| ---- | ---- |
| 数字徽章 | 圆角矩形,最小宽 16px,高 16px,字号 10px,色 `--text-on-brand` 底 `--brand`;> 99 显示 `99+` |
| 红点 | 8×8 圆点,色 `--brand`,定位元素右上角偏 -2px |
| 标识徽章 | 形似 `StatusTag` 但更小(高 16px) |

## Anatomy（结构组成）
- `StatusTag`：`radius-pill` 容器 + 可选 12px 图标 + 文字（i18n key）。
- `Avatar`：圆形容器（4 档尺寸）+ 图片或首字符占位 + 可选 2px 描边。
- `Badge`：数字徽章 / 红点 / 标识徽章三型，定位元素右上角偏 -2px。

## 反例（禁止形态）
- 用 `StatusTag` 渲染非语义信息（如分类标签 → 应用普通 Tag 组件）。
- 状态颜色手写（必须走 [04-status-colors.md](../04-status-colors.md) 映射）。
- 数字徽章直接显示 `100`（应 `99+`）。
- 头像缺图时用灰底问号（应首字符 + `--brand-soft` 底）。
- 红点不带 `aria-label`（屏幕阅读器无法感知未读）。

## 可访问性（a11y 强化）
- `StatusTag` 必须配 `aria-label`（含具体语义，如 “状态：已完成”），不能仅靠颜色。
- `Avatar` `<img>` 必须 `alt`（含用户名）；占位首字符可设 `aria-label="{name}"`。
- `Badge` 数字徽章 `aria-label="未读：{n} 条"`；红点 `role="status"` + `aria-label`。
- 颜色不是唯一区分手段（必须有文字或图标语义）。

## 空态
- 头像无图 → 自动首字符占位；状态标签必须有值（不允许空 `StatusTag`）。

## 错误态
- 不适用（这些原子组件本身无错误态；数据缺失由上层处理）。


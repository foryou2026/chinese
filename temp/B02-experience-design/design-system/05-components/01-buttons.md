<!-- TARGET-PATH: docs/B02-experience-design/design-system/05-components/01-buttons.md -->

# 05.01 · 按钮 Buttons

> 上游:[`04-status-colors.md §二`](../04-status-colors.md)。
> ui-kit 导出:`GlassButton`,变体 prop `variant: "primary" | "secondary" | "danger" | "ghost" | "link"`。

## 一、变体矩阵

| 变体 | 场景 | 背景 | 文字 | 边框 | 高度 | 圆角 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| `primary` | 创建 / 提交 | `--brand` | `--text-on-brand` | 无 | 36 / 32 / 28 | `radius-sm` |
| `secondary` | 筛选 / 导出 | `glass-button`(毛玻璃)| `--text-primary` | `--border-subtle` | 36 / 32 / 28 | `radius-sm` |
| `danger` | 删除 / 重置 | `--danger-soft` | `--danger` | `--danger` 1px | 36 | `radius-sm` |
| `ghost` | 表格内操作 | 透明 | `--text-primary` | 无 | 28 | `radius-sm` |
| `link` | 表单内跳转 | 透明 | `--brand` | 无 | 行内 | — |

## 二、尺寸
- `sm = 28px` / `md = 32px`(默认)/ `lg = 36px`;移动端默认 `lg`(便于触控)。
- 图标按钮(icon-only):36×36 / 32×32 正方形,必须提供 `aria-label`。

## 三、状态
- `hover`:`primary` → `--brand-hover`;`secondary` / `ghost` 叠加 `--bg-hover`;`danger` → 实色 `--brand` + 白字。
- `active`:`primary` → `--brand-active`。
- `disabled`:背景 `--bg-active`,文字 `--text-disabled`,边框 `--border-subtle`,`cursor: not-allowed`,**禁止 hover 变化**。
- `loading`:左侧加 14px Spinner,文字保持,自动 `disabled`;详见 [`06-interactions §1`](../06-interactions.md)。
- `focus-visible`:2px ring `--ring`。

## 四、约束
- 每个区段 / 弹窗内**全局只允许 1 个 `primary`**(主按钮唯一原则)。
- 按钮组间距:**8px**(`--space-2`)。
- 文案使用动词原型,5 语言 key 走 `shared-i18n`,无内联字面量。

## Anatomy（结构组成）
- 容器：`<button>`（不可用 `<div>`）；类名 `glass-button` + `data-variant`。
- 左插槽（可选）：14px 图标 / `Spinner`；
- 文字插槽：`<span class="btn-label">`；
- 右插槽（可选）：14px 图标 / 下拉箭头；
- focus-visible 时整体 2px ring `--ring`。

## 反例（禁止形态）
- 用 `<a class="btn-primary">` 代替 `<button>`（破坏语义、键盘体验）。
- 一个区段出现 2 个 `primary`（违反主按钮唯一原则）。
- loading 时只切图标不 disabled（用户可重复点击触发重复请求）。
- 把删除按钮做成 `primary` 红色实色（应使用 `danger` 变体的弱实/边框样式）。
- 文字内联字面量（应走 `shared-i18n`）。

## 可访问性（a11y 强化）
- `<button type="button|submit|reset">` 必填；图标按钮必须 `aria-label`。
- 禁用态使用 `disabled` 原生属性（**不要**仅靠样式），并保持 4.5:1 文本对比度。
- loading 时配 `aria-busy="true"` 与 `aria-live="polite"` 文本（屏幕阅读器朗读“处理中”）。
- focus ring 必须在毛玻璃面板上仍可见（2px `--ring`）。

## 空态
- 空态不适用（按钮总是渲染文案 / 图标）；若无文案 → 必为图标按钮且带 `aria-label`。

## 错误态
- 按钮自身无错误态；其触发的操作错误由 [Toast](06-toasts-alerts.md) / 表单内联反馈承接。
- `useAsyncAction` 异常自动恢复 disabled，并以 Toast 朗读错误码对应文案（详见 [`06-interactions.md §1`](../06-interactions.md)）。


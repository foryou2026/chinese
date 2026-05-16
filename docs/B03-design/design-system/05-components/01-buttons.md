<!-- TARGET-PATH: docs/B03-design/design-system/05-components/01-buttons.md -->

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

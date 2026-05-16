<!-- TARGET-PATH: docs/B04-design/design-system/05-components/00-index.md -->

# 05 · 组件 · 目录

> 实现库:**shadcn/ui** + Radix Primitives,主题层在 `system/packages/ui-kit/`。
> 所有业务可见组件**必须毛玻璃化**(`glass-button` / `glass-modal` / `glass-toast` / `glass-panel`),禁止裸用 shadcn 原始组件。
> Token 唯一来源 [01-tokens.md](../01-tokens.md);状态色映射详见 [04-status-colors.md](../04-status-colors.md)。
> 上游规范:[`04-status-colors.md`](../04-status-colors.md)。

## 组件清单

| 文件 | 组件 | ui-kit 导出名 |
| ---- | ---- | ---- |
| [01-buttons.md](01-buttons.md) | 按钮(主/次要/危险/文字/链接/图标/Loading)| `GlassButton` |
| [02-forms.md](02-forms.md) | 表单(Input/Select/Combobox/DatePicker/校验/帮助文案)| `Form*` 经 ui-kit 二次封装 |
| [03-tables.md](03-tables.md) | 表格(空/加载/虚拟滚动/排序/操作列)| `GlassCard` + TanStack Table |
| [04-modals.md](04-modals.md) | 弹窗(默认/大尺寸/全屏移动端)| `GlassModal` |
| [05-drawers.md](05-drawers.md) | 抽屉(右侧/移动满屏)| `GlassDrawer` |
| [06-toasts-alerts.md](06-toasts-alerts.md) | Toast(成功/错误/警告/信息)+ 确认弹窗 | `GlassToast` + `Confirm` |
| [07-empty-loading.md](07-empty-loading.md) | 空状态 / 加载骨架 / Spinner | `EmptyState` + `Skeleton` |
| [08-popovers-tooltips.md](08-popovers-tooltips.md) | 气泡 / 工具提示 / 弹层 | `glass-panel` 风格 |
| [09-avatars-badges-tags.md](09-avatars-badges-tags.md) | 头像 / 徽章 / 状态标签 | `StatusTag` |
| [10-tabs-accordion.md](10-tabs-accordion.md) | Tab / 折叠面板 | `GlassTabs` |
| [11-cards-glass.md](11-cards-glass.md) | 卡片(玻璃拟态基类)| `GlassCard` |
| [12-decorations.md](12-decorations.md) | 装饰元素(分隔线/光晕/底纹)| 无独立组件,内联 CSS |

## 全局规则
- 任何组件视觉状态(default / hover / active / disabled / loading / focus-visible)必须遵循 [04-status-colors.md](../04-status-colors.md) 的状态色映射,禁止手写颜色字面量。
- 暗黑模式适配走 [07-responsive-dark.md](../07-responsive-dark.md) CSS 变量翻转,组件代码不写 `dark:` 分支。
- 5 语言文案(zh/en/vi/th/id)必须由 [`shared-i18n`](../../../system/packages/shared-i18n/) 提供 key,组件不内联文字字面量。
- 无障碍:对照度 WCAG AA,所有交互元素 keyboard reachable + `focus-visible` 2px ring `--ring`。

<!-- TARGET-PATH: docs/B03-design/design-system/05-components/10-tabs-accordion.md -->

# 05.10 · Tab / 折叠

> ui-kit 导出:`GlassTabs` / `Accordion`(基于 Radix)。

## 一、Tab `GlassTabs`
| 属性 | 值 |
| ---- | ---- |
| 容器 | `glass-panel` 底 + 横向排布 |
| 高度 | 桌面 40px / 移动 44px |
| 选中态 | 文字 `--brand` + 底部 2px `--brand` 下划线 + 1.5x 字重 |
| 未选中 | 文字 `--text-secondary` |
| hover | `--bg-hover` |
| 间距 | tab 之间 24px;首尾 padding 16px |
| 切换动效 | 下划线滑动,`--motion-base` |

### 变体
- `pills`:无下划线,选中态为 `--brand-soft` 底 + `--brand` 字 + `radius-pill`。
- `vertical`:左侧导航形态;选中态为左侧 2px `--brand` 竖线 + `--bg-active` 底。

## 二、折叠 `Accordion`
| 属性 | 值 |
| ---- | ---- |
| 容器 | `<GlassCard>` 包裹 |
| 行高(收起态) | 56px |
| 展开动效 | 高度 0 → auto,`--motion-base` |
| 图标 | 右侧 `chevron-down` 16px,展开时旋转 180° |
| 多开 | 默认允许多 panel 同时展开;可通过 `singleOpen` prop 限单开 |
| 分隔 | panel 间 1px `--border-subtle` |

## Anatomy（结构组成）
- `GlassTabs`：横向 tab 列表 + 选中下划线 + 内容面板；变体 `pills` / `vertical`。
- `Accordion`：折叠面板列表，每项标题 + 右侧 `chevron-down`（旋转 180° 表示展开）+ 内容区，1px 分隔。

## 反例（禁止形态）
- 用 Tab 承载主流程切换（应改为路由）。
- Tab 数量 > 6 仍单行（应横向滚动或改为下拉）。
- 折叠面板默认全部展开（违反“折叠以减少噪音”初衷）。
- 折叠面板嵌套超过 2 层（认知负担大，应改为分级页面）。
- Tab 与下方内容颜色不区分，用户找不到边界。

## 可访问性（a11y 强化）
- `role="tablist"` / `tab` / `tabpanel` 三件套；`aria-selected` 与 `aria-controls` 必填。
- 键盘：左右箭头切换 tab（`vertical` 用上下）；`Home/End` 跳首尾；Tab 仅进入选中 panel。
- `Accordion`：触发按钮 `aria-expanded`、`aria-controls` 指向内容区 `id`；Enter/Space 切换。

## 空态
- Tab 内容为空时，`tabpanel` 渲染 `EmptyState`（紧凑变体）。
- Accordion 列表为空时，整体容器渲染 `EmptyState`。

## 错误态
- Tab/Accordion 切换加载失败：在对应 panel 内显示 `ErrorState` + “重试”，不破坏 tab/accordion 自身结构。


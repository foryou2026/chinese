# 组件：Table

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：展示结构化列表数据（学习记录、排行榜、词汇表）
- 禁忌：不用于展示非结构化内容（用 Card List）；移动端优先用卡片列表替代

## 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| default | 标准表格 | 学习记录、词汇列表 |
| compact | 紧凑行高 40px | 排行榜 |
| striped | 斑马纹交替背景 | 长列表提升可读性 |

## 尺寸

| 属性 | default | compact |
|------|---------|---------|
| 行高 | 48px | 40px |
| 表头高度 | 44px | 40px |
| 单元格 padding | `var(--space-3)` `var(--space-4)` | `var(--space-2)` `var(--space-3)` |
| 字号 | `var(--text-sm)` | `var(--text-sm)` |

## 表面材质

| 属性 | 值 |
|------|-----|
| 整体容器 | `.glass` — `var(--glass-bg)` + `backdrop-filter: var(--glass-blur)` 毛玻璃面板包裹 |
| 边框 | `1px solid var(--glass-border)` |
| 内层高光 | `inset 0 1px 0 0 var(--glass-inset)` |
| 圆角 | `var(--radius-lg)` |
| 阴影 | `0 6px 18px var(--glass-shadow)` |
| 数字对齐 | `font-variant-numeric: tabular-nums` |

## 状态

| 状态 | 表现 |
|------|------|
| 默认 | 毛玻璃面板背景，底部 `1px solid var(--color-neutral-200)` 分隔线 |
| hover（行） | `var(--glass-bg-card)` 背景 |
| focus（行） | `var(--focus-ring)` 围绕整行 |
| active（行选中） | `var(--color-brand-50)` 背景 + 左侧 3px `var(--color-brand-default)` 指示器 |
| disabled（行） | `opacity: 0.45`, `pointer-events: none` |
| loading | Skeleton 行（3-5 行占位，`var(--glass-bg-card)` 背景 shimmer） |
| empty | 空态组件居中（见 09-loading.md Empty） |
| error | Alert Banner（danger 变体）替代表格内容 |

## 表头

| 属性 | 值 |
|------|-----|
| 背景 | `var(--glass-bg-card)` |
| 字重 | `var(--weight-medium)` |
| 字体 | `var(--font-display)` |
| 颜色 | `var(--color-neutral-500)` |
| position | `sticky; top: 0`（表头固定） |

## 排序

| 状态 | 图标 |
|------|------|
| 未排序 | 上下双箭头，`var(--color-neutral-300)` |
| 升序 | 上箭头，`var(--color-brand-default)` |
| 降序 | 下箭头，`var(--color-brand-default)` |

## 筛选

- 表头列筛选图标（漏斗），点击弹出 Popover（`var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)`）
- 激活筛选时图标变为 `var(--color-brand-default)`
- 筛选器内支持 Input / Select / DatePicker

## 分页

见 11-pagination.md。表格底部嵌入分页组件。

## 响应式

| 断点 | 策略 |
|------|------|
| ≥lg | 标准表格 |
| md | 隐藏次要列，横向滚动 |
| <md | 卡片列表替代（每行数据一张 `.glass` 卡片） |

## 行为

| 交互 | 行为 |
|------|------|
| 列排序 | 点击表头切换 无→升→降→无 |
| 行选择 | Checkbox 列（可选），Shift+Click 范围选 |
| 键盘 | Tab 移动焦点到行，Enter 展开/操作 |
| 拖拽排序 | 可选功能，左侧拖拽手柄 |

## a11y

- [ ] `role="table"` / `role="grid"`
- [ ] 表头 `scope="col"`
- [ ] 排序列 `aria-sort="ascending/descending/none"`
- [ ] 选中行 `aria-selected="true"`
- [ ] 空态提供描述文字

---

## 99. 待确认问题

无

# 组件：Modal / Drawer / Popover / Tooltip / Dropdown

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## 遮罩层（通用）

| 属性 | 值 |
|------|-----|
| 背景 | `rgba(9, 9, 11, 0.50)` (深空黑半透) |
| 模糊 | `backdrop-filter: blur(4px)` |
| z-index | `var(--z-modal)` - 1 |

---

## Modal

### 用途与禁忌

- 用途：需要用户确认的操作（删除）、重要信息展示、表单填写
- 禁忌：不用于简单提示（用 Toast）；不用于长流程（用独立页面）

### 变体

| 变体 | 宽度 | 示例语境 |
|------|------|---------|
| sm | 400px | 确认对话框 |
| md | 520px | 表单弹窗 |
| lg | 680px | 详情预览 |
| fullscreen | 100vw（移动端） | 移动端表单 |

### 材质

| 属性 | 值 |
|------|-----|
| 背景 | `var(--glass-bg-elevated)` |
| 模糊 | `backdrop-filter: var(--glass-blur-lg)` |
| 边框 | `1px solid var(--glass-border)` |
| 顶部高光 | `::before` — `inset 0 1px 0 0 var(--glass-inset)` |
| 圆角 | `var(--radius-xl)`（移动端 fullscreen 时顶部圆角，底部 0） |
| 阴影 | `0 8px 40px -4px var(--glass-shadow-elevated)` |
| z-index | `var(--z-modal)` |
| body 滚动 | 锁定 |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 居中显示，遮罩 + 毛玻璃面板 |
| 进入 | 从 `scale(0.95) opacity(0)` → `scale(1) opacity(1)`，`var(--motion-slow)` `var(--easing-out)` |
| 退出 | 反向，`var(--motion-fast)` |
| loading | 内容区 Skeleton（`var(--glass-bg-card)` shimmer），按钮 disabled |
| error | 内容区显示 Alert（danger 变体） |

### Anatomy

```
[Backdrop 深空黑半透 + blur]
┌───────────────────────┐
│ ░░ 1px inset 高光 ░░░ │  ← var(--glass-inset)
│ [Title]         [X]   │  ← 标题栏 56px，var(--font-display)
├───────────────────────┤
│                       │
│    [Content]          │  ← 可滚动，max-height 70vh
│                       │
├───────────────────────┤
│      [取消] [确认]     │  ← 底部操作栏 64px
└───────────────────────┘
```

### 行为

| 交互 | 行为 |
|------|------|
| 点击遮罩 | 关闭（确认类弹窗禁止此行为） |
| Esc | 关闭 |
| Tab | 焦点陷阱（焦点不离开弹窗） |
| 打开时 | 焦点移到首个可交互元素 |
| 关闭后 | 焦点回到触发元素 |

---

## Drawer

### 变体

| 变体 | 方向 | 宽度/高度 | 示例语境 |
|------|------|----------|---------|
| right | 从右滑入 | 400px（桌面）/ 100vw（移动） | 详情面板、编辑表单 |
| left | 从左滑入 | 280px | 移动端导航 |
| bottom | 从下滑入 | 自适应（max 80vh） | app 移动端操作面板 |

### 材质

同 Modal：`var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` + `1px solid var(--glass-border)`。

开口侧有圆角 `var(--radius-xl)`，贴边侧圆角为 0。

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 遮罩 + 面板滑入 |
| 进入 | `translateX(100%)` → `translateX(0)`，`var(--motion-slow)` `var(--easing-out)` |
| 退出 | 反向，`var(--motion-fast)` |
| loading | 内容 Skeleton |

### Bottom Drawer（app 移动端核心交互）

| 属性 | 值 |
|------|-----|
| 拖拽手柄 | 顶部 36px 宽 `var(--color-neutral-300)` 条，可拖拽 |
| 吸附点 | 30% / 60% / 90% 屏幕高度 |
| 向下拖拽超阈值 | 关闭 |
| 顶部圆角 | `var(--radius-xl)` |

---

## Popover

### 用途

点击触发的浮动面板，承载筛选器、操作菜单等结构化内容。

| 属性 | 值 |
|------|-----|
| 触发 | 点击 |
| 材质 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur)` |
| 边框 | `1px solid var(--glass-border)` |
| 内层高光 | `inset 0 1px 0 0 var(--glass-inset)` |
| 定位 | 相对触发元素，自动翻转 |
| 圆角 | `var(--radius-lg)` |
| 阴影 | `0 8px 40px -4px var(--glass-shadow-elevated)` |
| z-index | `var(--z-popover)` |
| 关闭 | 点击外部 / Esc |
| 动画 | `scale(0.95) opacity(0)` → `scale(1) opacity(1)`，`var(--motion-fast)` |

---

## Tooltip

### 用途

hover/focus 触发的纯文字提示，不承载交互元素。

| 属性 | 值 |
|------|-----|
| 触发 | hover(300ms 延迟) + focus |
| 材质 | `.glass-dark` — `background: rgba(15, 23, 42, 0.88); backdrop-filter: var(--glass-blur-sm)` |
| 文字 | `var(--color-neutral-0)` (纯白) |
| 字号 | `var(--text-xs)` |
| padding | `var(--space-1)` `var(--space-2)` |
| 圆角 | `var(--radius-sm)` |
| max-width | 200px |
| z-index | `var(--z-tooltip)` |
| 箭头 | 6px 三角形指向触发元素 |
| 动画 | `opacity 0→1`，`var(--motion-fast)` |

### 位置

top（默认）/ bottom / left / right，空间不足自动翻转。

---

## Dropdown

### 用途

点击触发的操作菜单列表。

| 属性 | 值 |
|------|-----|
| 触发 | 点击按钮/图标 |
| 材质 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` |
| 边框 | `1px solid var(--glass-border)` |
| 内层高光 | `inset 0 1px 0 0 var(--glass-inset)` |
| min-width | 160px |
| max-height | 320px（可滚动） |
| 圆角 | `var(--radius-lg)` |
| 阴影 | `0 8px 40px -4px var(--glass-shadow-elevated)` |
| z-index | `var(--z-dropdown)` |

### 菜单项

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | transparent | `var(--color-neutral-700)` |
| hover | `var(--glass-bg-card)` | `var(--color-neutral-800)` |
| focus | `var(--focus-ring)` | — |
| active | `var(--glass-bg)` | `var(--color-neutral-900)` |
| disabled | transparent | `var(--color-neutral-400)` |
| destructive | transparent | `var(--color-danger-500)` |
| destructive hover | `var(--color-danger-50)` | `var(--color-danger-700)` |

| 属性 | 值 |
|------|-----|
| 项高度 | 40px |
| padding | `0 var(--space-3)` |
| 图标 | 可选，左侧 20px，间距 8px |
| 分隔线 | `1px solid var(--color-neutral-200)`，margin `var(--space-1)` 0 |

### 行为

| 交互 | 行为 |
|------|------|
| 上下键 | 移动高亮 |
| Enter/Space | 选中 |
| Esc | 关闭 |
| 点击外部 | 关闭 |
| 打开时 | 高亮第一项 |

---

## a11y 汇总

| 组件 | role | 关键 aria |
|------|------|----------|
| Modal | dialog | `aria-modal="true"`, `aria-labelledby`(title) |
| Drawer | dialog | `aria-modal="true"`, `aria-labelledby`(title) |
| Popover | — | `aria-expanded` on trigger |
| Tooltip | tooltip | `aria-describedby` on trigger |
| Dropdown | menu | `aria-expanded`, `menuitem` on items |

---

## 99. 待确认问题

无

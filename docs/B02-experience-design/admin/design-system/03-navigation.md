# 导航（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：02-layout.md, 01-tokens.md
> **冻结状态**：未冻结

---

## TopBar

| 属性 | 值 |
|------|-----|
| 高度 | 48px |
| 背景 | `var(--glass-bg-card)` + `backdrop-filter: var(--glass-blur)` — 毛玻璃面板 |
| 底部边框 | 1px solid `var(--glass-border)` |
| 内边距 | 0 `var(--space-4)` |
| position | `sticky; top: 0` |
| z-index | `var(--z-sticky)` |
| 左侧 | Logo 标识 + 品牌名（`var(--font-sans)`, `var(--weight-semibold)`） |
| 中部 | 全局搜索框（可选，`var(--radius-md)` 圆角输入框） |
| 右侧 | 通知铃铛图标 + 用户头像 + 下拉菜单 |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 毛玻璃面板 + 底部 1px 玻璃边框 |
| 滚动后 | 增加 `box-shadow: var(--shadow-sm)` |

### 移动端（<lg）

| 属性 | 值 |
|------|-----|
| 左侧 | 汉堡图标（触发 SideBar 抽屉） |
| 中部 | Logo 品牌名 |
| 右侧 | 用户头像 |

---

## SideBar（桌面端 >=lg）

| 属性 | 值 |
|------|-----|
| 展开宽度 | 240px |
| 折叠宽度 | 48px |
| 背景 | `var(--glass-bg)` + `backdrop-filter: var(--glass-blur)` — 毛玻璃面板 |
| 右侧边框 | 1px solid `var(--glass-border)` |
| position | `fixed; left: 0` |
| 高度 | 100vh |
| z-index | `var(--z-sticky)` |
| 顶部 | Logo 区域（48px 高，与 TopBar 对齐） |
| 底部 | 折叠/展开切换按钮 |

### 菜单项结构

```
┌──────────────────────────┐
│  [icon 20px]  [label]    │  ← 展开态
│  [icon 20px]             │  ← 折叠态
└──────────────────────────┘
```

| 属性 | 值 |
|------|-----|
| 菜单项高度 | 36px |
| 菜单项 padding | `0 var(--space-3)` |
| 图标尺寸 | 20px |
| 图标-文字间距 | 8px |
| 字号 | `var(--text-sm)` |
| 字重 | `var(--weight-regular)` |
| 分组标题 | `var(--text-xs)`, `var(--weight-semibold)`, `var(--text-muted)`, `text-transform: uppercase` |
| 分组间距 | `var(--space-5)` (20px) |
| 菜单项圆角 | `var(--radius-sm)` (6px) |

### 菜单项状态

| 状态 | 背景 | 文字颜色 | 图标颜色 | 左侧指示器 |
|------|------|---------|---------|-----------|
| 默认 | transparent | `var(--text-secondary)` | `var(--text-secondary)` | 无 |
| hover | `var(--color-neutral-100)` | `var(--text-primary)` | `var(--text-primary)` | 无 |
| active（当前页） | `var(--color-neutral-100)` | `var(--text-primary)` | `var(--text-primary)` | 2px `var(--color-accent)` 左侧竖线 |
| focus | `var(--focus-ring)` | -- | -- | -- |
| disabled | transparent | `var(--text-muted)` | `var(--text-muted)` | 无 |

### 子菜单

| 属性 | 值 |
|------|-----|
| 缩进 | 左侧 padding 增加 20px（图标宽度） |
| 展开/折叠 | 父菜单项右侧箭头旋转 90deg |
| 动画 | height auto，`var(--motion-base)` |

### 折叠/展开

| 属性 | 值 |
|------|-----|
| 过渡 | `var(--motion-base)` |
| 折叠后 | 仅显示图标（居中），hover 显示 Tooltip（`var(--color-neutral-900)` 实色背景） |
| 触发按钮 | SideBar 底部，双箭头图标 |

---

## Breadcrumb

| 属性 | 值 |
|------|-----|
| 字号 | `var(--text-sm)` |
| 字体 | `var(--font-sans)` |
| 分隔符 | `/`，颜色 `var(--text-muted)` |
| 间距 | 6px |
| 当前项 | `var(--text-primary)`, `var(--weight-medium)` |
| 历史项 | `var(--color-accent)`, 可点击 |
| hover（历史项） | 下划线 |
| 位置 | Content Area 顶部，TopBar 下方 |
| 溢出 | 中间项折叠为 `...`，点击展开 Dropdown |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 正常展示路径 |
| hover（历史项） | 下划线 |
| focus | `var(--focus-ring)` |
| loading | 末尾项显示 Skeleton 占位 |

### a11y

- `<nav aria-label="breadcrumb">`
- 有序列表 `<ol>`
- 当前项 `aria-current="page"`

---

## 移动端抽屉导航（<lg）

| 属性 | 值 |
|------|-----|
| 触发 | TopBar 左侧汉堡图标 |
| 宽度 | 280px |
| 方向 | 从左滑入 |
| 背景 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` — 强毛玻璃面板 |
| 右侧边框 | 1px solid `var(--glass-border)` |
| 遮罩 | `rgba(0, 0, 0, 0.40)` + `backdrop-filter: blur(4px)` |
| z-index | `var(--z-modal)` |
| 动画 | `translateX(-100%)` -> `translateX(0)`，`var(--motion-base)` |
| 关闭 | 点击遮罩 / X 按钮 |
| 内容 | 与桌面端 SideBar 菜单项一致 |

---

## 99. 待确认问题

无

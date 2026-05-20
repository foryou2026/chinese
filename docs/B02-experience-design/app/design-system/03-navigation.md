# 导航

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：02-layout.md, 01-tokens.md
> **冻结状态**：未冻结

---

## TopBar（app 桌面端 + admin 全端）

| 属性 | 值 |
|------|-----|
| 高度 | 56px |
| 背景 | var(--color-bg-primary) |
| 底部边框 | 1px solid var(--color-border) |
| 内边距 | 0 var(--space-6) |
| position | sticky top: 0 |
| z-index | var(--z-sticky) |
| 左侧 | Logo + 系统名称 |
| 中部 | 导航链接（admin 桌面）/ 空（app） |
| 右侧 | 语言切换 + 用户头像 |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 底部 1px 边框 |
| 滚动后 | 增加 var(--shadow-sm) |

---

## BottomBar（app 移动端 <lg）

| 属性 | 值 |
|------|-----|
| 高度 | 56px + env(safe-area-inset-bottom) |
| 背景 | var(--color-bg-primary) |
| 顶部边框 | 1px solid var(--color-border) |
| Tab 数量 | 5 |
| 图标尺寸 | 24px |
| 标签字号 | var(--text-xs) |
| position | fixed bottom: 0 |
| z-index | var(--z-fixed) |

### Tab Item 状态

| 状态 | 图标颜色 | 标签颜色 | 背景 |
|------|---------|---------|------|
| 默认 | var(--color-neutral-400) | var(--color-neutral-400) | 透明 |
| hover | var(--color-neutral-600) | var(--color-neutral-600) | 透明 |
| active（当前页） | var(--color-primary-500) | var(--color-primary-500) | 透明 |
| pressed | var(--color-primary-600) | var(--color-primary-600) | var(--color-primary-50) |

### 滚动行为

向下滚动隐藏（translateY(100%)），向上滚动显示。过渡 var(--motion-normal) var(--ease-default)。

---

## SideBar（admin 桌面端 ≥lg）

| 属性 | 值 |
|------|-----|
| 展开宽度 | 240px |
| 折叠宽度 | 64px |
| 背景 | var(--color-bg-primary) |
| 右侧边框 | 1px solid var(--color-border) |
| position | fixed left: 0 |
| 高度 | 100vh |
| z-index | var(--z-fixed) |

### 菜单项状态

| 状态 | 背景 | 文字颜色 | 左侧指示器 |
|------|------|---------|-----------|
| 默认 | 透明 | var(--color-text-secondary) | 无 |
| hover | var(--color-neutral-100) | var(--color-text-primary) | 无 |
| active（当前页） | var(--color-primary-50) | var(--color-primary-600) | 3px var(--color-primary-500) |
| focus | 焦点环 2px var(--color-ring) | — | — |
| disabled | 透明 | var(--color-neutral-300) | 无 |

### 折叠/展开

过渡 var(--motion-normal) var(--ease-default)。折叠后仅显示图标，hover 显示 tooltip。

---

## Breadcrumb（admin）

| 属性 | 值 |
|------|-----|
| 字号 | var(--text-sm) |
| 分隔符 | `/`，颜色 var(--color-neutral-400) |
| 当前项 | var(--color-text-primary)，font-weight var(--font-medium) |
| 历史项 | var(--color-primary-500)，可点击 |
| hover | 下划线 |

---

## 移动端抽屉导航（admin <lg）

| 属性 | 值 |
|------|-----|
| 触发 | TopBar 左侧汉堡图标 |
| 宽度 | 280px |
| 方向 | 从左滑入 |
| 遮罩 | rgba(0,0,0,0.5) |
| 动画 | var(--motion-slow) var(--ease-out) |
| 关闭 | 点击遮罩 / 滑动 / X 按钮 |

---

## 99. 待确认问题

无

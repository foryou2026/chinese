# 布局

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：01-tokens.md, docs/B01-architecture/07-i18n-responsive.md
> **冻结状态**：未冻结

---

## 断点

沿用 B01 定义：

| 断点 | 宽度 | 目标设备 |
|------|------|---------|
| sm | ≥480px | 大屏手机 |
| md | ≥768px | 平板竖屏 |
| lg | ≥1024px | 平板横屏/小笔记本 |
| xl | ≥1280px | 桌面 |
| 2xl | ≥1536px | 大桌面 |

最小宽度：320px。

> 断点值与 `tokens.css` 中 `--bp-sm`~`--bp-2xl` 逐字一致。

## 容器

| 规则 | 说明 |
|------|------|
| 宽度 | 100%，`max-width: var(--container-max)` = `none`（B01 要求全宽自适应） |
| 内边距 | `padding-inline: var(--container-pad)` — 响应式阶梯见下表 |
| Grid | CSS Grid / Flexbox（流体布局） |
| 窄容器 | `.container-narrow` max-width 880px（阅读/卡片流） |
| 表单容器 | `.container-form` max-width 640px（单列表单） |

### 容器内边距阶梯

| 断点 | `--container-pad` |
|------|-------------------|
| <768px | 24px |
| ≥768px | 28px |
| ≥1024px | 36px |
| ≥1280px | 48px |
| ≥1536px | 64px |
| ≥1920px | 96px |

> 密度切换覆盖：`compact` 统一 16px，`elder` 统一 32px。

## 页面背景

| 属性 | 值 |
|------|-----|
| 基底 | `var(--page-bg)` — 微蓝白 #FAFBFF（light）/ 深空黑 #09090B（dark） |
| 极光 | `.mesh-gradient-bg` — 3 个 blob 径向渐变（薰衣草+玫瑰粉+薄荷青），缓慢飘移动画 |

## 页面结构 — app 系统

```
┌─────────────────────────────┐
│    TopBar 毛玻璃 (桌面 ≥lg)   │  ← .glass-bar
├─────────────────────────────┤
│                             │
│   Content Area（极光渐变底）  │
│   (全宽, 可滚动, 卡片=.glass) │
│                             │
├─────────────────────────────┤
│  BottomBar 毛玻璃 (移动 <lg)  │  ← .glass-bar
└─────────────────────────────┘
```

## 页面结构 — admin 系统

```
┌──────┬──────────────────────┐
│      │  TopBar (.glass-bar)  │
│ Side │──────────────────────│
│ Bar  │                      │
│      │  Content (.container) │
│(.glass│  (极光渐变底, 可滚动)  │
│ -bar)│                      │
└──────┴──────────────────────┘
```

| 维度 | app | admin |
|------|-----|-------|
| 桌面导航 | TopBar (.glass-bar) | SideBar(.glass-bar, 可折叠) + TopBar |
| 移动导航 | BottomBar(5 tab, .glass-bar) | 汉堡菜单 + Drawer(.glass) |
| SideBar 宽度 | 无 | 展开 240px / 折叠 64px |
| TopBar 高度 | 56px | 56px |
| BottomBar 高度 | 56px + safe-area-inset | 无 |

## 间距系统

基准：4px (`var(--space-1)`)

| 场景 | 间距 |
|------|------|
| 组件内 padding | `var(--space-2)` ~ `var(--space-4)` (8-16px) |
| 卡片间 gap | `var(--space-4)` (16px) |
| 区块间 gap | `var(--space-6)` ~ `var(--space-7)` (24-32px) |
| 页面顶部留白 | `var(--space-4)` 移动 / `var(--space-6)` 桌面 |

## 滚动行为

| 场景 | 行为 |
|------|------|
| 主内容区 | 原生滚动，TopBar 固定 (.glass-bar + `position: sticky`) |
| BottomBar | 向下滚动隐藏，向上滚动显示（app 移动端） |
| SideBar | 独立滚动（admin 桌面端） |
| 弹窗/抽屉 | 锁定 body 滚动 |

## 表面材质规则

| 层级 | 材质 | 用途 |
|------|------|------|
| 底层 | 极光渐变 mesh gradient | body 背景 |
| 面板层 | `.glass` / `.glass-card` | 卡片、内容区 |
| 导航层 | `.glass-bar` | TopBar / BottomBar / SideBar |
| 弹出层 | `.glass-elevated` | Modal / Drawer / Dropdown |
| 暗浮层 | `.glass-dark` | Tooltip |

> 毛玻璃为唯一表面语言（P1 原则），不使用纯白/纯灰实色背景。

---

## 99. 待确认问题

无

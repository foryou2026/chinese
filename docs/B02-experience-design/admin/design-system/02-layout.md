# 布局（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：01-tokens.md
> **冻结状态**：未冻结

---

## 断点

沿用全局定义：

| 断点 | 宽度 | 目标设备 |
|------|------|---------|
| sm | >=480px | 大屏手机 |
| md | >=768px | 平板竖屏 |
| lg | >=1024px | 平板横屏/小笔记本 |
| xl | >=1280px | 桌面 |
| 2xl | >=1536px | 大桌面 |

最小宽度：320px。

> 断点值与 `01-tokens.md` 中 `--bp-sm`~`--bp-2xl` 逐字一致。

## 容器

| 规则 | 说明 |
|------|------|
| 宽度 | 100%，`max-width: none`（流体全宽自适应） |
| 内边距 | `padding-inline: var(--container-pad)` — 响应式阶梯见下表 |
| Grid | CSS Grid / Flexbox（流体布局） |
| 窄容器 | `.container-narrow` max-width 880px（阅读/卡片流） |
| 表单容器 | `.container-form` max-width 640px（单列表单） |

### 容器内边距阶梯

| 断点 | `--container-pad` |
|------|-------------------|
| <768px | 16px |
| >=768px | 24px |
| >=1024px | 24px |
| >=1280px | 32px |
| >=1536px | 32px |

> admin 内边距比 app 更小更紧凑——管理后台追求信息密度最大化。

## 页面背景

| 属性 | Light 模式 | Dark 模式 |
|------|-----------|-----------|
| 页面底色 | `var(--surface-page)` = #FFFFFF | #111827 |
| 卡片/区块 | `var(--surface-primary)` = #F9FAFB + 1px `var(--border-color)` | #1F2937 + 1px #374151 |
| 弹出层 | `var(--surface-elevated)` = #FFFFFF + `var(--shadow-md)` | #1F2937 + `var(--shadow-md)` |

> admin 不使用极光渐变背景和毛玻璃材质。所有表面为纯实色。

## 页面结构

```
┌──────┬──────────────────────────────┐
│      │  TopBar 48px (sticky)         │
│ Side │───────────────────────────────│
│ Bar  │                               │
│      │  Content Area                 │
│ 240px│  (纯白/深灰底, 流体, 可滚动)   │
│      │                               │
│      │                               │
└──────┴──────────────────────────────┘
```

| 维度 | 说明 |
|------|------|
| SideBar | 固定左侧，展开 240px / 折叠 48px |
| TopBar | 粘性定位，高度 48px |
| Content Area | 剩余空间，纯实色背景，内容可滚动 |
| 移动端（<lg） | 无 SideBar，汉堡菜单 + Drawer 导航 |

## SideBar 尺寸

| 属性 | 展开态 | 折叠态 |
|------|--------|--------|
| 宽度 | 240px | 48px |
| position | fixed, left: 0 | fixed, left: 0 |
| 高度 | 100vh | 100vh |
| 背景 | `var(--surface-page)` | `var(--surface-page)` |
| 右侧边框 | 1px solid `var(--border-color)` | 1px solid `var(--border-color)` |

## TopBar 尺寸

| 属性 | 值 |
|------|-----|
| 高度 | 48px |
| position | sticky, top: 0 |
| 背景 | `var(--surface-page)` |
| 底部边框 | 1px solid `var(--border-color)` |
| 左偏移 | 跟随 SideBar 宽度（展开 240px / 折叠 48px / 移动端 0） |
| z-index | `var(--z-sticky)` |

## 间距系统

基准：4px (`var(--space-1)`)

| 场景 | 间距 |
|------|------|
| 组件内 padding | `var(--space-2)` ~ `var(--space-3)` (8-12px) |
| 卡片间 gap | `var(--space-3)` ~ `var(--space-4)` (12-16px) |
| 区块间 gap | `var(--space-5)` ~ `var(--space-6)` (20-24px) |
| 页面顶部留白 | `var(--space-4)` (16px) |

> admin 间距整体比 app 更紧凑。

## 滚动行为

| 场景 | 行为 |
|------|------|
| 主内容区 | 原生滚动，TopBar 固定 (`position: sticky`) |
| SideBar | 独立滚动，菜单超长时内部可滚动 |
| 弹窗/抽屉 | 锁定 body 滚动 |
| 表格水平滚动 | 允许，自定义滚动条样式 |

## 表面材质规则

| 层级 | 材质 | 用途 |
|------|------|------|
| 底层 | 纯实色 `var(--surface-page)` | body 页面背景 |
| 面板层 | 纯实色 `var(--surface-primary)` + 1px `var(--border-color)` | 卡片、表格容器 |
| 导航层 | 纯实色 `var(--surface-page)` + 1px `var(--border-color)` | TopBar / SideBar |
| 弹出层 | 纯实色 `var(--surface-elevated)` + `var(--shadow-md)` | Modal / Drawer / Dropdown |
| 暗浮层 | 纯实色 `var(--color-neutral-900)` | Tooltip |

> admin 不使用毛玻璃（`backdrop-filter`）。所有表面使用不透明纯实色 + 1px 边框定义边界。

---

## 99. 待确认问题

无

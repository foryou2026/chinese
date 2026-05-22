# 导航

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：02-layout.md, 01-tokens.md
> **冻结状态**：未冻结

---

## 导航架构总览

| 断点 | 导航方式 |
|------|---------|
| >=lg（桌面/平板横屏） | TopBar（顶部导航栏） |
| <lg（移动/平板竖屏） | BottomBar（底部标签栏） |

> app 端不使用 SideBar 和 Breadcrumb（这两者为 admin 系统专属）。

---

## TopBar（app 桌面端 >=lg）

| 属性 | 值 |
|------|-----|
| 高度 | 56px |
| 材质 | `.glass-bar` — `background: var(--glass-bg); backdrop-filter: var(--glass-blur)` |
| 底部高光 | `border-bottom: 1px solid var(--glass-border)` |
| 顶部高光 | `::before` — `inset 0 1px 0 rgba(255,255,255,.90)` |
| 内边距 | `0 var(--container-pad)` |
| position | `sticky; top: 0` |
| z-index | `var(--z-sticky)` |
| 左侧 | Logo（`.brand-mark` 品牌标识 + `--font-display` 品牌名） |
| 中部 | 导航链接（学习/发现/排行榜/商店） |
| 右侧 | Streak 火焰 + XP 徽章 + 用户头像 |

### 导航链接状态

| 状态 | 文字颜色 | 底部指示器 | 背景 |
|------|---------|-----------|------|
| 默认 | `var(--color-neutral-500)` | 无 | transparent |
| hover | `var(--color-neutral-700)` | 无 | `var(--glass-bg)` 圆角区域 |
| active（当前页） | `var(--color-brand-default)` | `3px var(--color-brand-default)` 圆头底线 | transparent |
| focus | `var(--focus-ring)` | — | — |

### 滚动行为

| 状态 | 表现 |
|------|------|
| 默认 | 毛玻璃面板 + 底部玻璃边框 |
| 滚动后 | 增加 `box-shadow: var(--shadow-sm)` |

### Streak / XP 显示

| 元素 | 规格 |
|------|------|
| Streak 火焰 | 24px 图标，`var(--color-streak)` 色，旁显天数数字 |
| XP 徽章 | 圆角胶囊 `var(--radius-pill)`，`var(--color-xp)` 背景，白色数字 |

---

## BottomBar（app 移动端 <lg）

| 属性 | 值 |
|------|-----|
| 高度 | 56px + `env(safe-area-inset-bottom)` |
| 材质 | `.glass-bar` — 毛玻璃面板 |
| 顶部高光 | `border-top: 1px solid var(--glass-border)` |
| Tab 数量 | 5 |
| 图标尺寸 | 24px |
| 标签字号 | `var(--text-xs)` |
| 标签字体 | `var(--font-display)` |
| position | `fixed; bottom: 0` |
| z-index | `var(--z-sticky)` |

### 5 Tab 定义

| 序号 | Tab | 图标描述 | 说明 |
|------|-----|---------|------|
| 1 | 学习 | 书本/路径 | Quest Path 主页 |
| 2 | 发现 | 指南针/探索 | 课程发现、推荐 |
| 3 | 排行榜 | 奖杯/皇冠 | 排名竞赛 |
| 4 | 商店 | 钻石/商店 | 虚拟货币/道具商店 |
| 5 | 我的 | 用户头像 | 个人中心、设置 |

### Tab Item 状态

| 状态 | 图标颜色 | 标签颜色 | 背景 | 动效 |
|------|---------|---------|------|------|
| 默认 | `var(--color-neutral-400)` | `var(--color-neutral-400)` | 透明 | — |
| hover | `var(--color-neutral-600)` | `var(--color-neutral-600)` | 透明 | — |
| active（当前页） | `var(--color-brand-default)` | `var(--color-brand-default)` | 透明 | 图标 `scale(1.1)` 弹簧动效 `var(--easing-spring)` |
| pressed | `var(--color-brand-active)` | `var(--color-brand-active)` | `var(--color-brand-50)` 圆角椭圆 | `scale(0.9)` → `scale(1)` 弹簧回弹 |

> 当前页 Tab 图标切换为 filled（实心）版本，非当前页使用 outlined（线性）版本。

### 滚动行为

向下滚动隐藏（`translateY(100%)`），向上滚动显示。过渡 `var(--motion-base)` `var(--easing-out)`。

---

## 移动端抽屉导航（app <lg 补充入口）

| 属性 | 值 |
|------|-----|
| 触发 | "我的" Tab 页内或特定入口 |
| 宽度 | 280px |
| 方向 | 从右滑入 |
| 材质 | `.glass-elevated` — 强毛玻璃面板 + `--glass-blur-lg` |
| 遮罩 | `rgba(15, 23, 42, 0.50)` + `backdrop-filter: blur(4px)` |
| 动画 | `var(--motion-slow)` `var(--easing-out)` |
| 关闭 | 点击遮罩 / 滑动 / X 按钮 |
| 内容 | 用户信息卡片 + 设置/主题/密度/语言切换列表 |

---

## 99. 待确认问题

无

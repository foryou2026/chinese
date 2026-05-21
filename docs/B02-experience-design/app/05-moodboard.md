# Moodboard

> **阶段**：B02-XS 体验设计
> **角色**：体验总监 + 设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app（admin 引用本文件）
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-direction.md, 02-references.md
> **冻结状态**：未冻结

---

## 关键词（8 个，带可验证含义）

| 形容词 | 可验证含义 | 反例 |
|-------|----------|------|
| 极光漫射 | 页面背景为多彩 mesh gradient blob（薰衣草+玫瑰粉+薄荷青），缓慢飘移，营造沉浸式氛围 | 纯白/纯灰/暖黄底 |
| 棱光玻璃 | 所有面板/卡片/弹层使用 `backdrop-filter: blur(24~36px) saturate(1.8)` 毛玻璃 + 内顶高光 + 微光边框 | 传统实色 box-shadow 卡片 |
| 靛蓝主调 | 主色锚定靛蓝 #6366F1（HSL 239, 84%, 67%），5 套主题色可切换 | 沉闷暗蓝/暖黄/灰褐 |
| 信息密实 | 默认表格行高 44px、正文 16px、卡片 padding 20-24px；不为留白牺牲一屏信息量 | 大留白极简 SaaS |
| 弹性灵敏 | 所有可交互元素使用 spring 缓动（cubic-bezier(.16,1,.3,1)），hover/active ≤120ms 触发 | 线性缓动 / 无反馈 |
| 五色可换 | brand 色通过 `data-accent` 整体切换（indigo/rose/emerald/amber/violet），所有 UI 自动跟随 | 写死 hex 的单一配色 |
| 三密可调 | `data-density` 支持 default/compact/elder 三档密度，字号/间距/按钮高度响应式切换 | 固定单一密度 |
| 深邃双模 | dark mode 为独立设计（深空黑 #09090B + 宝石色 mesh blob），非简单反色；毛玻璃参数全套覆盖 | 纯黑 #000 或反色补丁 |

---

## 主色族（Brand · 5 主题色族）

| 主题色 | 锚定值 | 色相描述 | 气质标签 |
|--------|--------|---------|---------|
| indigo（默认） | #6366F1 | 靛蓝 | 智慧 · 沉稳 · 现代科技 |
| rose | #F43F5E | 玫瑰红 | 热情 · 活力 · 社交 |
| emerald | #10B981 | 翡翠绿 | 自然 · 成长 · 清新 |
| amber | #F59E0B | 琥珀金 | 温暖 · 能量 · 高级 |
| violet | #8B5CF6 | 紫晶 | 创意 · 梦幻 · 灵感 |

> 按钮/链接/焦点环/Tag 只用 `--color-brand-*`，禁止直接引用具体色族。

---

## 中性色族（冷灰阶，accent 无关）

| 级别 | 色值 | 用途 |
|------|------|------|
| neutral-0 | #FFFFFF | 纯白 · 文字落在 brand 上 |
| neutral-50 | #F8FAFC | 最浅灰 · 卡片背景辅助 |
| neutral-100 | #F1F5F9 | 淡灰 |
| neutral-200 | #E2E8F0 | 描边/分隔线 |
| neutral-300 | #CBD5E1 | 禁用态边框 |
| neutral-400 | #94A3B8 | placeholder 文字 |
| neutral-500 | #64748B | 辅助文字 |
| neutral-600 | #475569 | 次要文字 |
| neutral-700 | #334155 | 副文 · 标题 |
| neutral-800 | #1E293B | 深色层 |
| neutral-900 | #0F172A | 正文 |
| neutral-950 | #020617 | 最深 |

---

## 字体族

| 角色 | 字体栈 | 用途 |
|------|--------|------|
| 无衬线（sans） | Inter, Noto Sans SC, system-ui, sans-serif | 正文/表单/按钮/导航/全部 UI |
| 展示（display） | Inter, Noto Sans SC, system-ui, sans-serif | 标题（高字重区分层级） |
| 等宽（mono） | JetBrains Mono, Fira Code, monospace | 代码/数字场景 |
| 汉字学习（hanzi） | Noto Serif SC, Source Han Serif SC, serif | 学习内容中的汉字展示 |
| 书法（brush） | LXGW WenKai, Ma Shan Zheng, cursive | 仅限品牌 Logo |

| 字重 | 值 | 用途 |
|------|-----|------|
| regular | 400 | 正文 |
| medium | 500 | 次标题、按钮 |
| semibold | 600 | 标题 |
| bold | 700 | 大标题、数值强调 |

> 数字统一 `font-variant-numeric: tabular-nums`。

---

## 圆角

| 场景 | Token | 值 | 理由 |
|------|-------|-----|------|
| 小元素/Tag | --radius-sm | 8px | 精致小圆角 |
| 按钮/输入 | --radius-md | 12px | 现代感 |
| 卡片/面板 | --radius-lg | 16px | 玻璃面板圆角 |
| 强卡片/模态 | --radius-xl | 24px | 强浮起层级感 |
| 抽屉/Hero | --radius-2xl | 32px | 最外层容器 |
| 胶囊按钮/头像 | --radius-pill | 9999px | 胶囊形 |

---

## 阴影（毛玻璃体系）

| 级别 | 值 | 用途 |
|------|-----|------|
| shadow-sm | 0 2px 8px rgba(0,0,30,0.06) | 微浮起 |
| shadow-md | 0 6px 18px rgba(0,0,30,0.08) | 标准卡片 |
| shadow-lg | 0 14px 38px rgba(0,0,30,0.12) | 弹层/模态 |
| glass inner | inset 0 1px 0 0 var(--glass-inset) | 毛玻璃面板顶部高光 |
| glass outer | 0 4px 24px -1px var(--glass-shadow) | 毛玻璃面板外阴影 |

> 暗色模式下阴影 rgba 增强至 0.30~0.50，inset 高光降至 rgba(255,255,255,0.05)。

---

## 密度

| 维度 | default | compact | elder |
|------|---------|---------|-------|
| 正文字号 | 16px | 14px | 19px |
| 按钮高度 | 44px | 34px | 56px |
| 表格行高 | 44px | 36px | 56px |
| 卡片 padding | 20-24px | 12-16px | 28-36px |
| 间距基准 | 4px | 4px | 4px |

---

## 动效

| 类型 | 时长 | 缓动 |
|------|------|------|
| hover/focus | 150ms | cubic-bezier(.16,1,.3,1) |
| 展开/收起 | 250ms | cubic-bezier(.16,1,.3,1) |
| 模态进出 | 350ms | cubic-bezier(.16,1,.3,1) |
| 按钮浮起 | 200ms | cubic-bezier(.16,1,.3,1) |
| mesh blob 飘移 | 20-25s | ease-in-out |

> 必须支持 `prefers-reduced-motion: reduce`：所有动效降级为 0ms。

---

## 暗黑模式策略

| 项目 | 决定 |
|------|------|
| 是否必须 | 必须 |
| 基底 | 深空黑 #09090B（非纯黑，zinc-950） |
| 中性色 | 冷灰阶反转（zinc 系列暗底浅字） |
| 毛玻璃 | glass 参数全套覆盖（rgba(255,255,255,0.03~0.07) 基底） |
| brand 色 | 暗模式提亮一档（default→brand-400） |
| 状态色 | 暗模式下文字提亮、背景改为 18% 透明度 |
| mesh blob | 改为宝石色调（violet/cyan/pink），opacity 降低 |
| 切换方式 | `<html data-mode="light|dark|auto">`，auto 跟随系统 |

---

## 99. 待确认问题

无

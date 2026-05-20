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
| 温润如瓷 | 中性色使用暖墨灰阶 #1F1A14~#FFFBF0（非纯灰/冷灰），页面背景为宣纸渐变 | 纯灰 #808080 或冷蓝 #64748b |
| 薄玻璃覆 | 所有面板/卡片/弹层必须使用 `backdrop-filter: blur(22~34px)` 毛玻璃 + 顶部 1px 高光 | 传统实色 box-shadow 卡片 |
| 墨青主调 | 主色锚定宋瓷墨青 #1B3A5C（HSL 212, 53%, 23%），5 套主题色可切换 | 科技蓝 #3B82F6 或纯黑 |
| 信息密实 | 默认表格行高 44px、表单字号 17px、卡片 padding 20~24px；不为留白牺牲一屏信息量 | 大留白极简 SaaS |
| 触觉灵敏 | 所有可交互元素 hover/active 态 ≤120ms 触发，按钮浮起 translateY(-1px) | 点击无反馈的静态元素 |
| 五色可换 | brand 色通过 `data-accent` 整体切换（ink/cinnabar/jade/gold/graphite），所有 UI 自动跟随 | 写死 hex 的单一配色 |
| 三密可调 | `data-density` 支持 default/compact/elder 三档密度，字号/间距/按钮高度响应式切换 | 固定单一密度 |
| 墨夜双模 | dark mode 为独立设计（墨夜渐变 #0B1626→#14304F），非简单反色；毛玻璃参数全套覆盖 | 纯黑 #000 OLED 或反色补丁 |

---

## 主色族（Brand · 5 主题色族）

| 主题色 | 锚定值 | 色相描述 | 文化含义 |
|--------|--------|---------|---------|
| ink（默认） | #1B3A5C | 宋瓷墨青 | 汝窑天青釉 |
| cinnabar | #B14545 | 朱砂红 | 万历朱砂印 |
| jade | #4A6F5A | 翠玉绿 | 翡翠玉器 |
| gold | #B8923A | 鎏金黄 | 鎏金铜器 |
| graphite | #443B30 | 古墨棕 | 宋墨松烟 |

> 按钮/链接/焦点环/Tag 只用 `--color-brand-*`，禁止直接引用具体色族。

---

## 中性色族（暖墨灰阶，accent 无关）

| 级别 | 色值 | 用途 |
|------|------|------|
| neutral-0 | #FFFBF0 | 暖白纸 · 文字落在 brand 上 |
| neutral-50 | #F8F2E0 | 浅米 · 页面背景起始 |
| neutral-100 | #F0E8D2 | 淡米 |
| neutral-200 | #E5DCC7 | 描边/分隔线 |
| neutral-300 | #C5BBA8 | 禁用态边框 |
| neutral-400 | #9C9080 | placeholder 文字 |
| neutral-500 | #6F6452 | 茶灰 · 辅助文字 |
| neutral-600 | #56493A | 次要文字 |
| neutral-700 | #3D3327 | 副文 · 标题 |
| neutral-800 | #2A2218 | 深色层 |
| neutral-900 | #1F1A14 | 暖墨 · 正文 |
| neutral-950 | #100D0A | 最深 |

---

## 字体族

| 角色 | 字体栈 | 用途 |
|------|--------|------|
| 行楷（brush） | Ma Shan Zheng, STKaiti, cursive | 仅限品牌名/Hero H1/印鉴 |
| 宋体（display） | ZCOOL XiaoWei, Source Han Serif SC, Noto Serif SC, serif | 标题/按钮文字 |
| 黑体（sans） | Noto Sans SC, PingFang SC, Microsoft YaHei, system-ui, sans-serif | 正文/表单 |
| 等宽（mono） | JetBrains Mono, SF Mono, Consolas, monospace | 代码/数字场景 |

| 字重 | 值 | 用途 |
|------|-----|------|
| regular | 400 | 正文 |
| medium | 500 | 次标题 |
| semibold | 600 | 标题、按钮 |
| bold | 700 | 大标题、数值 |

> 数字统一 `font-variant-numeric: tabular-nums`。

---

## 圆角

| 场景 | Token | 值 | 理由 |
|------|-------|-----|------|
| 按钮/输入/Tag | --radius-md | 12px | 温润，对齐宋瓷器型 |
| 卡片/面板 | --radius-lg | 18px | 大圆角玻璃感 |
| 强卡片/模态 | --radius-xl | 26px | 强浮起层级感 |
| 抽屉/Hero | --radius-2xl | 34px | 最外层容器 |
| 印鉴/头像 | --radius-pill | 999px | 圆形 |

---

## 阴影（毛玻璃体系）

| 级别 | 值 | 用途 |
|------|-----|------|
| shadow-sm | 0 2px 8px rgba(14,31,56,0.08) | 微浮起 |
| shadow-md | 0 6px 18px rgba(14,31,56,0.12) | 标准卡片 |
| shadow-lg | 0 14px 38px rgba(14,31,56,0.18) | 弹层/模态 |
| glass-shadow | 6px 24px + inset 1px 高光 | 毛玻璃面板默认 |
| glass-shadow-lg | 14px 38px + inset 1px 高光 | 毛玻璃面板 hover |

> 暗色模式下阴影改为深墨 rgba(0,0,0,0.40~0.48)，inset 高光改为月白蓝。

---

## 密度

| 维度 | default | compact | elder |
|------|---------|---------|-------|
| 正文字号 | 17px | 15px | 20px |
| 按钮高度 | 44px | 34px | 64px |
| 表格行高 | 44px | 36px | 64px |
| 卡片 padding | 20-24px | 12-16px | 28-36px |
| 间距基准 | 4px | 4px | 4px |

---

## 动效

| 类型 | 时长 | 缓动 |
|------|------|------|
| hover/focus | 120ms | cubic-bezier(.2,.8,.2,1) |
| 展开/收起 | 200ms | cubic-bezier(.2,.8,.2,1) |
| 模态进出 | 320ms | cubic-bezier(.2,.8,.2,1) |
| 按钮浮起 | 200ms | cubic-bezier(.2,.8,.2,1) |

> 必须支持 `prefers-reduced-motion: reduce`：所有动效降级为 0ms。

---

## 暗黑模式策略

| 项目 | 决定 |
|------|------|
| 是否必须 | 必须 |
| 基底 | 墨夜渐变 #0B1626→#14304F→#0E1F38 |
| 中性色 | 灰阶反转（暗底浅字） |
| 毛玻璃 | glass 参数全套覆盖（rgba(20,48,79,...) 基底） |
| brand 色 | 暗模式提亮一档（default→brand-400） |
| 宣纸纹理 | 关闭（opacity: 0） |
| 切换方式 | `<html data-mode="light|dark|auto">`，auto 跟随系统 |

---

## 99. 待确认问题

无

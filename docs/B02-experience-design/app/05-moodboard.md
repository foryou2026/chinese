# Moodboard

> **阶段**：B02-XS 体验设计
> **角色**：体验总监 + 设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-direction.md, 02-references.md
> **冻结状态**：未冻结

---

## 关键词（8 个，带可验证含义）

| 形容词 | 可验证含义 | 反例 |
|-------|----------|------|
| 闯关冒险 | 首页呈现蜿蜒关卡路径，节点有完成/进行中/锁定三态视觉 | 纯列表菜单 / 传统课程目录 |
| 毛玻璃层次 | 导航栏/卡片/弹层使用 `backdrop-filter: blur(20px) saturate(1.8)` + 内顶高光 + 半透明边框 | 纯实色卡片 / 无深度感 |
| 弹跳有趣 | 按钮按下 `scale(0.95)` → 释放 `scale(1.02)` spring 回弹；答对有星星/粒子飞散庆祝 | 无反馈的静默 UI |
| 进度可见 | 每屏至少一个进度指示器（进度条/圆环/关卡完成度），用户随时知道自己在哪里 | 无进度感知 |
| 五色可换 | brand 色通过 `data-accent` 整体切换（indigo/rose/emerald/amber/violet），所有 UI 自动跟随 | 写死 hex 的单一配色 |
| 移动优先 | 核心流程从 375px 起设计，大按钮（48px+）、大触控区、底部导航 | 仅桌面端适配 |
| 奖励驱动 | XP 数值 / 连胜天数 / 等级 / 成就徽章，持续正向激励 | 无激励的纯学习 |
| 深邃双模 | dark mode 为独立设计（深色底 + 柔和毛玻璃），非简单反色 | 纯黑 #000 或反色补丁 |

---

## 主色族（Brand · 5 主题色族）

| 主题色 | 锚定值 | 色相描述 | 气质标签 |
|--------|--------|---------|---------|
| indigo（默认） | #6366F1 | 靛蓝 | 智慧 · 沉稳 · 探索 |
| rose | #F43F5E | 玫瑰红 | 热情 · 活力 · 挑战 |
| emerald | #10B981 | 翡翠绿 | 成长 · 自然 · 成功 |
| amber | #F59E0B | 琥珀金 | 温暖 · 能量 · 奖励 |
| violet | #8B5CF6 | 紫晶 | 创意 · 梦幻 · 冒险 |

> 按钮/链接/焦点环/进度条/XP 标签只用 `--color-brand-*`，禁止直接引用具体色族。

---

## 游戏化状态色

| 色彩角色 | 色值 | 用途 |
|---------|------|------|
| 正确/通过 | 翡翠绿 #10B981 | 答对反馈、关卡完成、成就解锁 |
| 错误/未通过 | 红 #EF4444 | 答错反馈、失败提示 |
| XP/经验值 | 琥珀金 #F59E0B | XP 标签、经验值增长 |
| 连胜/火焰 | 橙红 #F97316 | 连胜提示、火焰图标 |
| 锁定/未解锁 | 冷灰 #94A3B8 | 未解锁关卡、锁定内容 |

---

## 中性色族（冷灰阶，accent 无关）

| 级别 | 色值 | 用途 |
|------|------|------|
| neutral-0 | #FFFFFF | 纯白 · 文字落在 brand 上 |
| neutral-50 | #F8FAFC | 最浅灰 · 卡片背景辅助 |
| neutral-100 | #F1F5F9 | 淡灰 |
| neutral-200 | #E2E8F0 | 描边/分隔线 |
| neutral-300 | #CBD5E1 | 禁用态边框 |
| neutral-400 | #94A3B8 | placeholder 文字 / 锁定态 |
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
| 等宽（mono） | JetBrains Mono, Fira Code, monospace | 代码/数字/XP 计数场景 |
| 汉字学习（hanzi） | Noto Serif SC, Source Han Serif SC, serif | 学习内容中的汉字展示 |
| 书法（brush） | LXGW WenKai, Ma Shan Zheng, cursive | 仅限品牌 Logo |

| 字重 | 值 | 用途 |
|------|-----|------|
| regular | 400 | 正文 |
| medium | 500 | 次标题、按钮 |
| semibold | 600 | 标题、XP 数值 |
| bold | 700 | 大标题、关卡数值强调 |
| extrabold | 800 | 超大数字展示（如连胜天数） |

> 数字统一 `font-variant-numeric: tabular-nums`。

---

## 圆角

| 场景 | Token | 值 | 理由 |
|------|-------|-----|------|
| 小元素/Tag | --radius-sm | 8px | 精致小圆角 |
| 按钮/输入 | --radius-md | 12px | 圆润现代感 |
| 学习卡片 | --radius-lg | 16px | 游戏卡片圆角 |
| 关卡节点 | --radius-xl | 20px | 突出游戏感 |
| 模态/弹层 | --radius-2xl | 24px | 强浮起层级感 |
| 胶囊按钮/XP 标签 | --radius-pill | 9999px | 胶囊形 |

---

## 阴影（毛玻璃体系 + 游戏化投影）

| 级别 | 值 | 用途 |
|------|-----|------|
| shadow-sm | 0 2px 8px rgba(0,0,30,0.06) | 微浮起 |
| shadow-md | 0 4px 16px rgba(0,0,30,0.10) | 卡片 / 关卡节点 |
| shadow-lg | 0 12px 32px rgba(0,0,30,0.14) | 弹层/模态 |
| shadow-btn | 0 4px 0 0 色值加深版 | 按钮底部立体阴影（多邻国风格） |
| glass inner | inset 0 1px 0 0 var(--glass-inset) | 毛玻璃面板顶部高光 |
| glass outer | 0 4px 24px -1px var(--glass-shadow) | 毛玻璃面板外阴影 |

> 暗色模式下阴影 rgba 增强至 0.30~0.50，inset 高光降至 rgba(255,255,255,0.05)。

---

## 密度

| 维度 | default | compact | elder |
|------|---------|---------|-------|
| 正文字号 | 16px | 14px | 19px |
| 按钮高度 | 48px | 38px | 56px |
| 关卡节点大小 | 64px | 52px | 80px |
| 卡片 padding | 20-24px | 14-16px | 28-36px |
| 间距基准 | 4px | 4px | 4px |

---

## 动效

| 类型 | 时长 | 缓动 |
|------|------|------|
| 按钮按下 | 100ms | cubic-bezier(.16,1,.3,1) |
| 按钮弹回 | 200ms | cubic-bezier(.34,1.56,.64,1) (spring overshoot) |
| hover/focus | 150ms | cubic-bezier(.16,1,.3,1) |
| 展开/收起 | 250ms | cubic-bezier(.16,1,.3,1) |
| 模态进出 | 350ms | cubic-bezier(.16,1,.3,1) |
| 答对庆祝 | 500ms | cubic-bezier(.34,1.56,.64,1) |
| XP 飘字 | 800ms | cubic-bezier(.16,1,.3,1) |
| mesh blob 飘移 | 20-25s | ease-in-out |

> 必须支持 `prefers-reduced-motion: reduce`：所有动效降级为 0ms。

---

## 暗黑模式策略

| 项目 | 决定 |
|------|------|
| 是否必须 | 必须 |
| 基底 | 深空灰 #111827（非纯黑，gray-900） |
| 中性色 | 冷灰阶反转 |
| 毛玻璃 | glass 参数全套覆盖（rgba(255,255,255,0.04~0.08) 基底） |
| brand 色 | 暗模式提亮一档（default→brand-400） |
| 状态色 | 暗模式下文字提亮、背景改为 18% 透明度 |
| mesh blob | 改为宝石色调（violet/cyan/pink），opacity 降低 |
| 切换方式 | `<html data-mode="light|dark|auto">`，auto 跟随系统 |

---

## 99. 待确认问题

无

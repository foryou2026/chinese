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
| 触觉灵敏 | 所有可交互元素 active 态 <100ms 触发；按钮按下缩放 scale(0.97) | 点击无反馈的静态按钮 |
| 游戏驱动 | 核心流程包含 XP/streak/等级中至少 2 种；正确答案触发庆祝微动画 | 纯文字学习报告 |
| 移动原生 | 底部 Tab Bar 导航；核心功能≤2 次触控到达；全宽布局无两侧留白 | PC 后台系统 responsive 缩放 |
| 温暖中性 | neutral 色 hue 210-230、saturation 8-12%；非纯灰、非冷蓝 | 纯灰 #808080 或冷蓝 #64748b(sat=0) |
| 沉浸暗黑 | dark mode 背景 #0f172a（偏蓝灰），非纯黑；层级用 opacity 区分 | 纯黑 #000000 OLED 方案 |
| 双色活力 | 主色 cyan #06b6d4 + 强调色 orange #f97316 双色调；不混用第三主色 | 彩虹多色或单色灰阶 |
| 圆润亲和 | 卡片/按钮 border-radius 12px；输入框 8px；不超过 16px（避免儿童化） | 直角 0px 或胶囊 9999px 满屏 |
| 呼吸留白 | 卡片间距≥16px；段落间距≥12px；单屏可交互元素≤7 个 | 信息密集电商列表页 |

---

## 主色族

| 角色 | 色值 | 用途 |
|------|------|------|
| primary-500（主色） | #06b6d4 | 主按钮、链接、选中态、导航高亮 |
| primary-400 | #22d3ee | hover 态、图表强调 |
| primary-600 | #0891b2 | active 态、深色背景上的主色 |
| primary-100 | #cffafe | 浅色标签背景、选中行背景 |
| accent-500（强调色） | #f97316 | CTA 按钮、奖励/XP 标识、通知角标 |
| accent-400 | #fb923c | hover 态 |
| accent-600 | #ea580c | active 态 |

---

## 中性色族

| 级别 | 色值 | 用途 |
|------|------|------|
| neutral-50 | #f8fafc | 页面背景（light） |
| neutral-100 | #f1f5f9 | 卡片背景（light） |
| neutral-200 | #e2e8f0 | 分隔线、边框 |
| neutral-300 | #cbd5e1 | 禁用态边框 |
| neutral-400 | #94a3b8 | placeholder 文字 |
| neutral-500 | #64748b | 次要文字 |
| neutral-600 | #475569 | 正文文字（light） |
| neutral-700 | #334155 | 标题文字（light）/ 卡片背景（dark） |
| neutral-800 | #1e293b | 深色背景层 |
| neutral-900 | #0f172a | dark mode 主背景 |
| neutral-950 | #020617 | dark mode 最深层 |

> 中性色基于 Tailwind Slate 色阶（hue ~215, saturation ~10%），带暖灰偏移。

---

## 字体族

| 角色 | 字体栈 | 理由 |
|------|--------|------|
| 西文/越南语/印尼语 | Inter, system-ui, sans-serif | 支持越南语变音符，Google Fonts 免费 |
| 泰语 | Noto Sans Thai, system-ui, sans-serif | Google Fonts 免费，覆盖泰语全字符 |
| 中文 | "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif | 沿用 B01 系统字体栈 |
| 等宽 | "JetBrains Mono", "Fira Code", monospace | 代码/数字场景 |
| 数字 | font-variant-numeric: tabular-nums | 对齐 XP/分数等数值 |

| 字重 | 值 | 用途 |
|------|-----|------|
| normal | 400 | 正文 |
| medium | 500 | 次标题、按钮文字 |
| semibold | 600 | 标题、强调 |
| bold | 700 | 大标题、数值突出 |

---

## 圆角

| 场景 | 值 | 理由 |
|------|-----|------|
| 按钮/输入框 | 8px | 亲和但不幼稚 |
| 卡片/弹窗 | 12px | 圆润卡片感，对齐 REF-2 Duolingo |
| 标签/徽章 | 16px | 胶囊形，视觉区分 |
| 头像 | 9999px（圆形） | 行业惯例 |
| 底部弹出面板 | 顶部 16px，底部 0 | 对齐 REF-3 Grab bottom sheet |

---

## 阴影

| 级别 | 值 | 用途 |
|------|-----|------|
| sm | 0 1px 2px 0 rgb(0 0 0 / 0.05) | 卡片默认 |
| md | 0 4px 6px -1px rgb(0 0 0 / 0.1) | 卡片 hover / 下拉菜单 |
| lg | 0 10px 15px -3px rgb(0 0 0 / 0.1) | 弹窗 / 抽屉 |

> 暗色模式下阴影替换为边框（1px neutral-700），阴影不可见。

---

## 密度

| 维度 | 值 |
|------|-----|
| 间距基准 | 4px |
| 卡片间距 | 16px |
| 按钮高度 sm/md/lg | 32px / 40px / 48px |
| 输入框高度 | 44px |
| 表格行高 | 48px |
| 最小字号 | 12px |
| 表格密度 | 标准（行高 48px，移动触控友好） |
| 表单密度 | 标准（字段间距 16px） |

---

## 动效

| 类型 | 时长 | 缓动 |
|------|------|------|
| hover/focus 状态切换 | 100ms | ease-out |
| 展开/收起 | 150ms | ease-in-out |
| 弹窗进入/退出 | 200ms | ease-out / ease-in |
| 页面转场 | 300ms（红线上限） | ease-in-out |
| 庆祝动画（撒花/星星） | 200ms 触发 + CSS animation | spring(0.175, 0.885, 0.32, 1.275) |

> 必须支持 `prefers-reduced-motion: reduce`：所有动效降级为 0ms。

---

## 暗黑模式策略

| 项目 | 决定 |
|------|------|
| 是否必须 | 必须 |
| 基底色 | #0f172a（slate-900，偏蓝灰） |
| 层级 | 背景 → 卡片 → 弹窗，用 neutral-800/700 逐级提亮 |
| 文字 | 主文字 #f8fafc，次要 #94a3b8 |
| 主色调整 | primary-400 (#22d3ee) 替代 primary-500 提升对比度 |
| 阴影 | 关闭，用 1px border neutral-700 替代 |
| 切换方式 | `<html data-mode="light|dark|auto">`，auto 跟随系统 |
| 默认 | auto（跟随系统偏好） |

---

## 99. 待确认问题

无

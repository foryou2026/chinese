# 响应式与暗黑模式

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：01-tokens.md, 02-layout.md
> **冻结状态**：未冻结

---

## 断点行为

| 组件/模式 | <480px (mobile) | 480-767px (sm) | 768-1023px (md) | 1024-1279px (lg) | >=1280px (xl+) |
|----------|----------------|----------------|-----------------|------------------|---------------|
| app 导航 | BottomBar | BottomBar | BottomBar | TopBar | TopBar |
| Quest Path | 单列居中 | 单列居中 | 单列居中 | 双列可选 | 双列可选 |
| Modal | 全屏 | 全屏 | 居中弹窗(.glass) | 居中弹窗(.glass) | 居中弹窗(.glass) |
| Form | 单列全宽 | 单列全宽 | 双列 | 双列 | 双列 |
| 按钮组 | 纵向堆叠全宽 | 横向排列 | 横向排列 | 横向排列 | 横向排列 |
| 容器内边距 | 24px | 24px | 28px | 36px | 48px~96px |
| 毛玻璃 blur | 16px (减负) | 24px | 24px | 24px | 24px |
| 排行榜 | 简化列表 | 简化列表 | 完整表格 | 完整表格 | 完整表格 |

---

## DOM 三轴标记

| 轴 | 属性 | 取值 | 默认 |
|----|------|------|------|
| 模式 | `data-mode` | light / dark / auto | auto |
| 主题色 | `data-accent` | indigo / rose / emerald / amber / violet | indigo |
| 密度 | `data-density` | default / compact / elder | default |

> 三轴均在 `<html>` 元素上设置，JS 初始化时从 localStorage 读取或使用默认值。

---

## 暗黑模式 — 深灰映射

### 页面背景

| 属性 | Light | Dark |
|------|-------|------|
| `--page-bg` | #FAFBFF (微蓝白) | #111827 (深灰 gray-900) |
| mesh blob | 薰衣草+玫瑰粉+薄荷青，高 opacity | 紫晶+青+玫红，低 opacity |

> 暗黑模式基底色从原 #09090B（纯黑 zinc-950）调整为 #111827（深灰 gray-900），减少视觉压迫感，更适合长时间学习使用。

### 中性灰阶反转

| Token | Light | Dark |
|-------|-------|------|
| `--color-neutral-0` | #FFFFFF | #111827 |
| `--color-neutral-50` | #F8FAFC | #1F2937 |
| `--color-neutral-100` | #F1F5F9 | #374151 |
| `--color-neutral-200` | #E2E8F0 | #4B5563 |
| `--color-neutral-300` | #CBD5E1 | #6B7280 |
| `--color-neutral-400` | #94A3B8 | #9CA3AF |
| `--color-neutral-500` | #64748B | #D1D5DB |
| `--color-neutral-600` | #475569 | #E5E7EB |
| `--color-neutral-700` | #334155 | #F3F4F6 |
| `--color-neutral-800` | #1E293B | #F9FAFB |
| `--color-neutral-900` | #0F172A | #FAFAFA |
| `--color-neutral-950` | #020617 | #FFFFFF |

### 品牌色调整

| Token | Light | Dark | 原因 |
|-------|-------|------|------|
| `--color-brand-default` | brand-600 | brand-400 | 暗底提升对比度 |
| `--color-brand-hover` | brand-500 | brand-300 | 同上 |
| `--color-brand-active` | brand-700 | brand-500 | 同上 |
| `--color-brand-ring` | 0.30 alpha | 0.28 alpha | 暗底调整光晕 |

### 毛玻璃参数

| Token | Light | Dark |
|-------|-------|------|
| `--glass-bg` | `rgba(255,255,255, 0.60)` | `rgba(255,255,255, 0.03)` |
| `--glass-bg-card` | `rgba(255,255,255, 0.65)` | `rgba(255,255,255, 0.05)` |
| `--glass-bg-elevated` | `rgba(255,255,255, 0.75)` | `rgba(255,255,255, 0.07)` |
| `--glass-border` | `rgba(255,255,255, 0.70)` | `rgba(255,255,255, 0.08)` |
| `--glass-inset` | `rgba(255,255,255, 0.90)` | `rgba(255,255,255, 0.05)` |

### 状态色

| 状态 | Light 文字 | Dark 文字 | Light 背景 | Dark 背景 |
|------|-----------|-----------|-----------|-----------|
| success | #10B981 | #34D399 | #ECFDF5 | `rgba(16,185,129, 0.12)` |
| warning | #F59E0B | #FBBF24 | #FFFBEB | `rgba(245,158,11, 0.12)` |
| danger | #EF4444 | #FCA5A5 | #FEF2F2 | `rgba(239,68,68, 0.12)` |
| info | #3B82F6 | #93C5FD | #EFF6FF | `rgba(59,130,246, 0.12)` |

### 游戏化色

| 色名 | Light | Dark |
|------|-------|------|
| `--color-xp` | #F59E0B | #FBBF24 (提亮) |
| `--color-streak` | #F97316 | #FB923C (提亮) |
| `--color-locked` | #94A3B8 | #6B7280 (降低) |
| `--shadow-btn` | `0 4px 0 0 color-700` | `0 4px 0 0 color-900` (加深阴影) |

---

## 密度切换

| Token | default | compact | elder |
|-------|---------|---------|-------|
| `--space-3` | 12px | 8px | 16px |
| `--space-4` | 16px | 12px | 22px |
| `--space-5` | 20px | 16px | 28px |
| `--space-6` | 24px | 22px | 36px |
| `--text-base` | 16px | 14px | 19px |
| `--text-md` | 18px | 15px | 21px |
| `--text-lg` | 22px | 22px | 24px |
| `--container-pad` | 响应式阶梯 | 16px | 32px |
| Quest 节点尺寸 | 64px | 52px | 80px |
| BottomBar 图标 | 24px | 20px | 28px |

---

## 五色主题

通过 `[data-accent]` 切换品牌色族：

| accent | 色名 | 主色 -500 | 用途 |
|--------|------|-----------|------|
| indigo | 靛蓝 | #6366F1 | 默认，智慧沉稳 |
| rose | 玫瑰 | #F43F5E | 热情活力 |
| emerald | 翡翠 | #10B981 | 自然清新 |
| amber | 琥珀 | #F59E0B | 温暖能量 |
| violet | 紫晶 | #8B5CF6 | 创意灵感 |

每套 accent 在 `themes.css` 中覆盖 `--color-brand-50`~`--color-brand-900` 全色阶 + 语义别名。

> 注意：`--shadow-btn` 的颜色值在每套 accent 下自动跟随 `--color-brand-700`（light）/ `--color-brand-900`（dark）。

---

## 99. 待确认问题

无

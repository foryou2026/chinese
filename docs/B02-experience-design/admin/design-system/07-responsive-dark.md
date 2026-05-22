# 响应式与暗黑模式（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：01-tokens.md, 02-layout.md
> **冻结状态**：未冻结

---

## 断点行为

| 组件/模式 | <480px (mobile) | 480-767px (sm) | 768-1023px (md) | 1024-1279px (lg) | >=1280px (xl+) |
|----------|----------------|----------------|-----------------|------------------|---------------|
| admin 导航 | 汉堡+抽屉 | 汉堡+抽屉 | 汉堡+抽屉 | SideBar 折叠 48px | SideBar 展开 240px |
| TopBar | 汉堡+Logo+头像 | 汉堡+Logo+头像 | 汉堡+搜索+头像 | 搜索+通知+头像 | 搜索+通知+头像 |
| 表格 | 卡片列表 | 卡片列表 | 横向滚动 | 完整表格 | 完整表格 |
| Modal | 全屏 | 全屏 | 居中弹窗 | 居中弹窗 | 居中弹窗 |
| Form | 单列全宽 | 单列全宽 | 双列 | 双列 | 双列 |
| 按钮组 | 纵向堆叠全宽 | 横向排列 | 横向排列 | 横向排列 | 横向排列 |
| 容器内边距 | 16px | 16px | 24px | 24px | 32px |
| 表格行高 | -- | -- | 40px | 40px | 40px |

---

## DOM 二轴标记

| 轴 | 属性 | 取值 | 默认 |
|----|------|------|------|
| 模式 | `data-mode` | light / dark | light |
| 密度 | `data-density` | default / compact | default |

> 两轴均在 `<html>` 元素上设置，JS 初始化时从 localStorage 读取或使用默认值。
> admin 不支持 `data-accent` 和 `data-mode="auto"`。admin 的暗黑模式必须手动切换。

---

## 暗黑模式 — 完整映射表

### 页面背景

| 属性 | Light | Dark |
|------|-------|------|
| `--surface-page` | #FFFFFF | #111827 |
| `--surface-primary` | #F9FAFB | #1F2937 |
| `--surface-elevated` | #FFFFFF | #1F2937 |

### 中性灰阶反转

| Token | Light | Dark |
|-------|-------|------|
| `--color-neutral-0` | #FFFFFF | #111827 |
| `--color-neutral-50` | #F9FAFB | #1F2937 |
| `--color-neutral-100` | #F3F4F6 | #374151 |
| `--color-neutral-200` | #E5E7EB | #4B5563 |
| `--color-neutral-300` | #D1D5DB | #6B7280 |
| `--color-neutral-400` | #9CA3AF | #9CA3AF |
| `--color-neutral-500` | #6B7280 | #D1D5DB |
| `--color-neutral-600` | #4B5563 | #E5E7EB |
| `--color-neutral-700` | #374151 | #F3F4F6 |
| `--color-neutral-800` | #1F2937 | #F9FAFB |
| `--color-neutral-900` | #111827 | #FAFAFA |
| `--color-neutral-950` | #030712 | #FFFFFF |

### 按钮色反转

| Token | Light | Dark |
|-------|-------|------|
| `--btn-primary-bg` | #18181B | #FAFAFA |
| `--btn-primary-bg-hover` | #27272A | #F4F4F5 |
| `--btn-primary-bg-active` | #09090B | #E4E4E7 |
| `--btn-primary-text` | #FAFAFA | #18181B |
| `--btn-secondary-bg` | #FFFFFF | #1F2937 |
| `--btn-secondary-bg-hover` | #F9FAFB | #374151 |
| `--btn-secondary-bg-active` | #F3F4F6 | #4B5563 |
| `--btn-secondary-text` | #374151 | #F3F4F6 |
| `--btn-secondary-border` | #D1D5DB | #4B5563 |

### 链接与焦点色

| Token | Light | Dark |
|-------|-------|------|
| `--color-accent` | #3B82F6 | #60A5FA |
| `--color-accent-hover` | #2563EB | #93C5FD |
| `--focus-ring` | `0 0 0 3px rgba(59,130,246,0.30)` | `0 0 0 3px rgba(96,165,250,0.30)` |

### 边框与文字

| Token | Light | Dark |
|-------|-------|------|
| `--border-color` | #E5E7EB | #374151 |
| `--text-primary` | #111827 | #FAFAFA |
| `--text-secondary` | #6B7280 | #9CA3AF |
| `--text-muted` | #9CA3AF | #6B7280 |

### 阴影

| Token | Light | Dark |
|-------|-------|------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | `0 1px 2px rgba(0,0,0,0.30)` |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.07)` | `0 4px 6px rgba(0,0,0,0.40)` |
| `--shadow-lg` | `0 10px 25px rgba(0,0,0,0.10)` | `0 10px 25px rgba(0,0,0,0.50)` |

### 状态色

| 状态 | Light 文字 | Dark 文字 | Light 背景 | Dark 背景 |
|------|-----------|-----------|-----------|-----------|
| success | #10B981 | #34D399 | #ECFDF5 | `rgba(16,185,129, 0.12)` |
| warning | #F59E0B | #FBBF24 | #FFFBEB | `rgba(245,158,11, 0.12)` |
| danger | #EF4444 | #FCA5A5 | #FEF2F2 | `rgba(239,68,68, 0.12)` |
| info | #3B82F6 | #93C5FD | #EFF6FF | `rgba(59,130,246, 0.12)` |

---

## 密度切换

| Token | default | compact |
|-------|---------|---------|
| `--space-3` | 12px | 8px |
| `--space-4` | 16px | 12px |
| `--space-5` | 20px | 16px |
| `--space-6` | 24px | 22px |
| `--text-base` | 16px | 14px |
| `--text-md` | 18px | 15px |
| `--container-pad` | 响应式阶梯 | 12px |
| 表格行高 | 40px | 32px |
| 菜单项高度 | 36px | 28px |
| TopBar 高度 | 48px | 40px |

> admin 仅支持 default + compact 两档。不支持 elder 模式——管理后台面向运营/管理人员，无需适老化。

### CSS 实现

```css
[data-density="default"] { /* 默认值，所有 token 不变 */ }
[data-density="compact"] {
  --text-base: 14px;
  --text-md: 15px;
  --space-3: 8px;
  --space-4: 12px;
  --space-5: 16px;
  --space-6: 22px;
}
```

---

## 99. 待确认问题

无

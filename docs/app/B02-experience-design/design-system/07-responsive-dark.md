# 响应式与暗黑模式

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：01-tokens.md, 02-layout.md
> **冻结状态**：未冻结

---

## 断点行为

| 组件/模式 | <640px (mobile) | 640-767px (sm) | 768-1023px (md) | 1024-1279px (lg) | ≥1280px (xl+) |
|----------|----------------|----------------|-----------------|------------------|---------------|
| app 导航 | BottomBar | BottomBar | BottomBar | TopBar | TopBar |
| admin 导航 | 汉堡+抽屉 | 汉堡+抽屉 | 汉堡+抽屉 | SideBar折叠 | SideBar展开 |
| 表格 | 卡片列表 | 卡片列表 | 横向滚动 | 完整表格 | 完整表格 |
| Modal | 全屏 | 全屏 | 居中弹窗 | 居中弹窗 | 居中弹窗 |
| Form | 单列全宽 | 单列全宽 | 双列 | 双列 | 双列 |
| 按钮组 | 纵向堆叠全宽 | 横向排列 | 横向排列 | 横向排列 | 横向排列 |
| 内边距 | 16px | 16px | 24px | 24px | 32px |

---

## 暗黑模式 Token 映射

### 语义色

| Token | Light | Dark |
|-------|-------|------|
| --color-bg-primary | #ffffff | #0f172a |
| --color-bg-secondary | #f8fafc | #1e293b |
| --color-bg-tertiary | #f1f5f9 | #334155 |
| --color-text-primary | #0f172a | #f8fafc |
| --color-text-secondary | #475569 | #94a3b8 |
| --color-text-tertiary | #94a3b8 | #64748b |
| --color-text-inverse | #ffffff | #0f172a |
| --color-border | #e2e8f0 | #334155 |
| --color-border-strong | #cbd5e1 | #475569 |
| --color-ring | #06b6d4 | #22d3ee |

### 主色调整

| Token | Light | Dark | 原因 |
|-------|-------|------|------|
| 主色（交互） | primary-500 #06b6d4 | primary-400 #22d3ee | 暗底提升对比度 |
| 强调色（交互） | accent-500 #f97316 | accent-400 #fb923c | 同上 |
| 主色（背景填充） | primary-500 | primary-600 #0891b2 | 降低暗底上的刺眼感 |

### 阴影替换

| Light | Dark |
|-------|------|
| box-shadow: var(--shadow-*) | box-shadow: none; border: 1px solid var(--color-border) |

### 状态色

| 状态 | Light 文字 | Dark 文字 | Light 背景 | Dark 背景 |
|------|-----------|-----------|-----------|-----------|
| success | #10b981 | #34d399 | #d1fae5 | rgba(16,185,129,0.15) |
| warning | #f59e0b | #fbbf24 | #fef3c7 | rgba(245,158,11,0.15) |
| error | #ef4444 | #f87171 | #fee2e2 | rgba(239,68,68,0.15) |
| info | #3b82f6 | #60a5fa | #dbeafe | rgba(59,130,246,0.15) |

---

## CSS 实现

```css
:root, [data-mode="light"] {
  /* Light mode tokens (默认) */
  --color-bg-primary: #ffffff;
  --color-bg-secondary: #f8fafc;
  --color-bg-tertiary: #f1f5f9;
  --color-text-primary: #0f172a;
  --color-text-secondary: #475569;
  --color-text-tertiary: #94a3b8;
  --color-text-inverse: #ffffff;
  --color-border: #e2e8f0;
  --color-border-strong: #cbd5e1;
  --color-ring: #06b6d4;
}

[data-mode="dark"] {
  --color-bg-primary: #0f172a;
  --color-bg-secondary: #1e293b;
  --color-bg-tertiary: #334155;
  --color-text-primary: #f8fafc;
  --color-text-secondary: #94a3b8;
  --color-text-tertiary: #64748b;
  --color-text-inverse: #0f172a;
  --color-border: #334155;
  --color-border-strong: #475569;
  --color-ring: #22d3ee;
}

@media (prefers-color-scheme: dark) {
  [data-mode="auto"] {
    --color-bg-primary: #0f172a;
    --color-bg-secondary: #1e293b;
    --color-bg-tertiary: #334155;
    --color-text-primary: #f8fafc;
    --color-text-secondary: #94a3b8;
    --color-text-tertiary: #64748b;
    --color-text-inverse: #0f172a;
    --color-border: #334155;
    --color-border-strong: #475569;
    --color-ring: #22d3ee;
  }
}
```

---

## DOM 三轴标记

| 轴 | 属性 | 取值 | 默认 |
|----|------|------|------|
| 模式 | `data-mode` | light / dark / auto | auto |
| 主题色 | `data-accent` | accent-1（cyan+orange，默认）| accent-1 |
| 密度 | `data-density` | default / compact | default |

> 三轴均在 `<html>` 元素上设置，JS 初始化时从 localStorage 读取或使用默认值。

---

## 99. 待确认问题

无

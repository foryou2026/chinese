# 组件：Toast / Alert / Banner

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## Toast

### 用途与禁忌

- 用途：轻量操作反馈（保存成功、复制成功、网络恢复）
- 禁忌：不用于需要用户操作的提示（用 Alert/Modal）；不用于错误详情（用 Alert）

### 变体

| 变体 | 左侧色条 | 图标色 |
|------|---------|--------|
| success 翠玉 | `var(--color-success-500)` | `var(--color-success-500)` |
| danger 朱砂 | `var(--color-danger-500)` | `var(--color-danger-500)` |
| warning 鎏金 | `var(--color-warning-500)` | `var(--color-warning-500)` |
| info 青花 | `var(--color-info-500)` | `var(--color-info-500)` |

### 材质

| 属性 | 值 |
|------|-----|
| 背景 | `var(--glass-2)` |
| 模糊 | `backdrop-filter: var(--glass-blur)` |
| 边框 | `var(--glass-border)` |
| 左侧色条 | 3px 状态色 |
| 顶部高光 | `::before` inset 1px |
| min-width | 280px |
| max-width | 420px |
| padding | `var(--space-3)` `var(--space-4)` |
| 圆角 | `var(--radius-lg)` |
| 阴影 | `var(--glass-shadow-lg)` |

### 位置与行为

| 属性 | 值 |
|------|-----|
| 位置 | 顶部居中（移动端）/ 右上角（桌面端） |
| z-index | `var(--z-toast)` |
| 自动关闭 | 3s（success/info）/ 5s（warning/danger） |
| 手动关闭 | 右侧 X 按钮 |
| 堆叠 | 最多 3 条，新的在上方推入 |
| 进入动画 | 从上方滑入 + fadeIn，`var(--motion-slow)` |
| 退出动画 | fadeOut + 向右滑出，`var(--motion-fast)` |
| 滑动关闭 | 移动端左/右滑动关闭 |

### Anatomy

```
┌─┬────────────────────────────────┐
│ │ [icon] [message]         [X]   │  ← .glass-2 + backdrop-filter
│ │        [action link?]          │
└─┴────────────────────────────────┘
↑ 3px 状态色条
```

- action link：可选，如"撤销"，`var(--color-brand-default)` 文字

### a11y

- `role="status"`（success/info）/ `role="alert"`（danger/warning）
- `aria-live="polite"`（success/info）/ `"assertive"`（danger/warning）

---

## Alert

### 用途与禁忌

- 用途：页面内嵌的状态信息（表单错误汇总、警告说明、操作引导）
- 禁忌：不用于临时反馈（用 Toast）

### 变体

| 变体 | 左侧色条 | 背景 | 图标 |
|------|---------|------|------|
| success 翠玉 | `var(--color-success-500)` | `var(--glass-1)` | check-circle |
| danger 朱砂 | `var(--color-danger-500)` | `var(--glass-1)` | x-circle |
| warning 鎏金 | `var(--color-warning-500)` | `var(--glass-1)` | alert-triangle |
| info 青花 | `var(--color-info-500)` | `var(--glass-1)` | info |

### 材质

| 属性 | 值 |
|------|-----|
| 背景 | `var(--glass-1)` + `backdrop-filter: var(--glass-blur-sm)` |
| 边框 | `var(--glass-border)` |
| 左侧色条 | 4px 状态色 |

### Anatomy

```
┌─┬──────────────────────────┐
│ │ [icon] [title?]    [X?]  │  ← .glass-1 + backdrop-filter
│ │ [description]             │
│ │ [action button?]          │
└─┴──────────────────────────┘
  ↑ 4px 状态色条
```

| 属性 | 值 |
|------|-----|
| padding | `var(--space-3)` `var(--space-4)` |
| 圆角 | `var(--radius-md)` |
| 可关闭 | 可选，右上角 X |
| title 字体 | `var(--font-display)`，`var(--weight-semibold)` |
| description 字号 | `var(--text-sm)` |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 静态显示 |
| hover | 无变化 |
| focus（关闭按钮） | `var(--focus-ring)` |
| dismissing | fadeOut `var(--motion-fast)` + 高度折叠 |

---

## Banner

### 用途与禁忌

- 用途：全局级通知（系统维护、新版本、重要公告），位于页面最顶部
- 禁忌：不用于操作反馈（用 Toast）；同时最多 1 条

### Anatomy

```
┌──────────────────────────────────────────┐
│ [icon?] [message]  [action?]  [dismiss]  │
└──────────────────────────────────────────┘
```

| 属性 | 值 |
|------|-----|
| 高度 | 44px |
| 宽度 | 100% |
| 背景（info） | `linear-gradient(135deg, var(--color-brand-700), var(--color-brand-600))` |
| 背景（warning） | `linear-gradient(135deg, var(--color-warning-700), var(--color-warning-500))` |
| 背景（danger） | `linear-gradient(135deg, var(--color-danger-700), var(--color-danger-500))` |
| 文字 | white |
| 位置 | 页面最顶部，在 TopBar 之上 |
| z-index | `var(--z-toast)` |

---

## 99. 待确认问题

无

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

| 变体 | 左侧图标色 | 背景 |
|------|-----------|------|
| success | var(--color-success) | var(--color-bg-primary) |
| error | var(--color-error) | var(--color-bg-primary) |
| warning | var(--color-warning) | var(--color-bg-primary) |
| info | var(--color-info) | var(--color-bg-primary) |

### 尺寸

| 属性 | 值 |
|------|-----|
| min-width | 280px |
| max-width | 420px |
| padding | 12px 16px |
| 圆角 | var(--radius-lg) |
| 阴影 | var(--shadow-lg) |

### 位置与行为

| 属性 | 值 |
|------|-----|
| 位置 | 顶部居中（移动端）/ 右上角（桌面端） |
| z-index | var(--z-toast) |
| 自动关闭 | 3s（success/info）/ 5s（warning/error） |
| 手动关闭 | 右侧 X 按钮 |
| 堆叠 | 最多 3 条，新的在上方推入 |
| 进入动画 | 从上方滑入 + fadeIn，var(--motion-slow) |
| 退出动画 | fadeOut + 向右滑出，var(--motion-fast) |
| 滑动关闭 | 移动端左/右滑动关闭 |

### Anatomy

```
┌───────────────────────────────┐
│ [icon] [message]        [X]  │
│        [action link?]        │
└───────────────────────────────┘
```

- action link：可选，如"撤销"，var(--color-primary-500) 文字

### a11y

- role="status"（success/info）/ role="alert"（error/warning）
- aria-live="polite"（success/info）/ "assertive"（error/warning）

---

## Alert

### 用途与禁忌

- 用途：页面内嵌的状态信息（表单错误汇总、警告说明、操作引导）
- 禁忌：不用于临时反馈（用 Toast）

### 变体

| 变体 | 左侧色条 | 背景 | 图标 |
|------|---------|------|------|
| success | var(--color-success) | var(--color-success-light) | check-circle |
| error | var(--color-error) | var(--color-error-light) | x-circle |
| warning | var(--color-warning) | var(--color-warning-light) | alert-triangle |
| info | var(--color-info) | var(--color-info-light) | info |

### Anatomy

```
┌─┬──────────────────────────┐
│ │ [icon] [title?]    [X?]  │
│ │ [description]             │
│ │ [action button?]          │
└─┴──────────────────────────┘
  ↑ 4px 色条
```

| 属性 | 值 |
|------|-----|
| padding | 12px 16px |
| 圆角 | var(--radius-md) |
| 左侧色条 | 4px |
| 可关闭 | 可选，右上角 X |
| title 字重 | var(--font-semibold) |
| description 字号 | var(--text-sm) |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 静态显示 |
| hover | 无变化 |
| focus（关闭按钮） | 焦点环 |
| dismissing | fadeOut var(--motion-fast) + 高度折叠 |
| loading | 无（Alert 不含 loading 态） |

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
| 背景 | var(--color-primary-500)（info）/ var(--color-warning)（warning）/ var(--color-error)（error） |
| 文字 | white |
| 位置 | 页面最顶部，在 TopBar 之上 |
| z-index | var(--z-toast) |

---

## 99. 待确认问题

无

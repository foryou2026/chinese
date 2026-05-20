# 组件：Pagination / Breadcrumb

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Pagination

### 用途与禁忌

- 用途：分页导航（表格、列表底部）
- 禁忌：短列表（<20 条）不需分页；无限滚动场景用"加载更多"按钮

### 变体

| 变体 | 说明 | 适用 |
|------|------|------|
| full | 上一页/下一页 + 页码 + 跳转 + 每页条数 | admin 表格 |
| simple | 上一页/下一页 + 当前页/总页数 | app 列表 |
| load-more | "加载更多"按钮 | app 信息流 |

### 尺寸（full/simple）

| 属性 | 值 |
|------|-----|
| 页码按钮尺寸 | 36px x 36px |
| 字号 | `var(--text-sm)` |
| 数字字体 | `tabular-nums` |
| 间距 | `var(--space-1)` |
| 圆角 | `var(--radius-md)` |

### 页码按钮状态

| 状态 | 背景 | 文字 | 边框 |
|------|------|------|------|
| 默认 | transparent | `var(--color-neutral-500)` | 无 |
| hover | `var(--glass-3)` | `var(--color-neutral-700)` | 无 |
| focus | `var(--focus-ring)` | — | — |
| active（当前页） | `var(--color-brand-default)` | `var(--color-brand-on)` | 无 |
| disabled（上一页/下一页） | transparent | `var(--color-neutral-300)` | 无 |

### 省略号

- 页码过多时中间显示 `...`
- hover 显示跳转输入框（Popover，`.glass-strong`）

### load-more 变体

| 状态 | 表现 |
|------|------|
| 默认 | `.proto-btn-secondary` "加载更多" |
| loading | 按钮 loading 态 |
| 无更多 | 文字 "已全部加载"，`var(--color-neutral-400)` |

### 行为

| 交互 | 行为 |
|------|------|
| 键盘 | Tab 移动焦点，Enter 选中 |
| 页码切换 | 滚动到列表顶部 |

---

## Breadcrumb

### 用途与禁忌

- 用途：展示页面层级路径（admin 为主）
- 禁忌：不用于 app 用户端（移动端空间不足，用返回按钮）

### 样式

| 属性 | 值 |
|------|-----|
| 字号 | `var(--text-sm)` |
| 分隔符 | `/` 或 `>`，`var(--color-neutral-400)` |
| 间距 | 8px |
| 当前项 | `var(--color-neutral-700)`, `var(--weight-medium)` |
| 历史项 | `var(--color-brand-500)`，hover 下划线 |
| 溢出 | 中间项折叠为 `...`，点击展开 Dropdown（`.glass-strong`） |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 正常展示 |
| hover（历史项） | 下划线 |
| focus | `var(--focus-ring)` |
| loading | 末尾项 Skeleton |

### a11y

- `<nav aria-label="breadcrumb">`
- 有序列表 `<ol>`
- 当前项 `aria-current="page"`

---

## 99. 待确认问题

无

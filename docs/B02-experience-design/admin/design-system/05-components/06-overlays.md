# 组件：Modal / Drawer / Popover / Tooltip / Dropdown（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Modal

### 尺寸

| 尺寸 | 宽度 | 适用 |
|------|------|------|
| sm | 400px | 确认对话框 |
| md | 520px | 表单弹窗 |
| lg | 680px | 复杂表单、详情预览 |

### 材质

| 属性 | 值 |
|------|-----|
| 背景 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` — 毛玻璃面板 |
| 边框 | 1px solid `var(--glass-border)` |
| 顶部高光 | `inset 0 1px 0 0 var(--glass-inset)` |
| 圆角 | `var(--radius-xl)` |
| 阴影 | `0 10px 30px var(--glass-shadow-elevated)` |
| 遮罩 | `rgba(0,0,0,0.40)` + `backdrop-filter: blur(4px)` |

### 结构

- header: 56px，标题 + 关闭按钮
- body: 内容区，可滚动
- footer: 64px，操作按钮靠右

### 动效

- 入场：`opacity 0→1` + `scale 0.97→1`，200ms ease-out
- 退场：反向

---

## Drawer

| 方向 | 宽度/高度 | 适用 |
|------|----------|------|
| right | 400px | 详情面板、编辑侧栏 |
| left | 280px | 移动端导航 |
| bottom | max 80vh | 移动端操作面板 |

### 材质

| 属性 | 值 |
|------|-----|
| 背景 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` — 毛玻璃面板 |
| 边框 | 1px solid `var(--glass-border)` |
| 阴影 | `0 8px 24px var(--glass-shadow-elevated)` |

---

## Dropdown

| 属性 | 值 |
|------|-----|
| 背景 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` — 毛玻璃面板 |
| 边框 | 1px solid `var(--glass-border)` |
| 顶部高光 | `inset 0 1px 0 0 var(--glass-inset)` |
| 圆角 | `var(--radius-md)` |
| 阴影 | `0 6px 20px var(--glass-shadow-elevated)` |
| 菜单项高 | 36px |
| 菜单项 hover | `var(--surface-hover)` |
| 分隔线 | 1px solid `var(--border-color)` |
| 危险项 | `var(--color-danger-500)` 文字色 |

---

## Tooltip

| 属性 | 值 |
|------|-----|
| 背景 | `rgba(17, 24, 39, 0.92)` + `backdrop-filter: var(--glass-blur-sm)` — 暗色毛玻璃 |
| 文字 | #F9FAFB |
| 字号 | `var(--text-xs)` |
| 圆角 | `var(--radius-sm)` |
| padding | `var(--space-1) var(--space-2)` |
| 最大宽度 | 200px |
| 延迟 | 300ms 显示，0ms 隐藏 |

---

## 通用规则

- 所有浮层统一使用 `backdrop-filter` 毛玻璃材质，与 admin 整体 Frost 风格保持一致
- 遮罩层使用 `backdrop-filter: blur(4px)` 轻度模糊
- 提供 `@supports not (backdrop-filter)` 实色回退
- Escape 关闭
- 焦点锁定在 Modal/Drawer 内
- 关闭后焦点回到触发元素

## a11y 验收点

- [ ] Modal/Drawer: `role="dialog"` + `aria-modal="true"`
- [ ] Tooltip: `role="tooltip"` + 触发元素 `aria-describedby`
- [ ] Dropdown: `role="menu"` + 子项 `role="menuitem"`
- [ ] Escape 关闭
- [ ] 焦点陷阱（Modal/Drawer）

---

## 99. 待确认问题

无

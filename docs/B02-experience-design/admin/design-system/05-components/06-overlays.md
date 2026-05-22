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
| 背景 | `var(--surface-elevated)` |
| 边框 | 1px solid `var(--border-color)` |
| 圆角 | `var(--radius-lg)` |
| 阴影 | `var(--shadow-lg)` |
| 遮罩 | `rgba(0,0,0,0.50)` |

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
| 背景 | `var(--surface-elevated)` |
| 边框 | 1px solid `var(--border-color)` |
| 阴影 | `var(--shadow-lg)` |

---

## Dropdown

| 属性 | 值 |
|------|-----|
| 背景 | `var(--surface-elevated)` |
| 边框 | 1px solid `var(--border-color)` |
| 圆角 | `var(--radius-md)` |
| 阴影 | `var(--shadow-lg)` |
| 菜单项高 | 36px |
| 菜单项 hover | `var(--surface-hover)` |
| 分隔线 | 1px solid `var(--border-color)` |
| 危险项 | `var(--color-danger-500)` 文字色 |

---

## Tooltip

| 属性 | 值 |
|------|-----|
| 背景 | `var(--color-neutral-900)` |
| 文字 | white |
| 字号 | `var(--text-xs)` |
| 圆角 | `var(--radius-sm)` |
| padding | `var(--space-1) var(--space-2)` |
| 最大宽度 | 200px |
| 延迟 | 300ms 显示，0ms 隐藏 |

---

## 通用规则

- 所有浮层使用实色背景，**禁止** backdrop-filter
- 遮罩层不使用模糊效果
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

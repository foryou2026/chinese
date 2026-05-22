# 组件：Input / Textarea / Select（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：用户文本输入、单值选择
- 禁忌：多选用 Checkbox/Tag；开关用 Switch；富文本用专用编辑器

---

## Input

### 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| default | 标准单行输入 | 用户名、邮箱 |
| password | 带显示/隐藏切换 | 密码输入 |
| search | 左侧搜索图标 + 右侧清除按钮 | 全局搜索、列表筛选 |

### 尺寸

| 尺寸 | 高度 | padding-x | 字号 | 圆角 |
|------|------|-----------|------|------|
| sm | 32px | 10px | `var(--text-sm)` | `var(--radius-sm)` |
| md | 36px | 12px | `var(--text-base)` | `var(--radius-md)` |
| lg | 44px | 14px | `var(--text-base)` | `var(--radius-md)` |

### 材质

| 属性 | Light 模式 | Dark 模式 |
|------|-----------|-----------|
| 背景 | `var(--surface-page)` #FFFFFF | `var(--surface-primary)` |
| 边框 | 1px solid `var(--border-color)` #E5E7EB | 1px solid `var(--border-color)` #374151 |
| 圆角 | `var(--radius-md)` 8px | 同左 |

### 状态

| 状态 | 边框 | 背景 | 其他 |
|------|------|------|------|
| 默认 | `var(--border-color)` | `var(--surface-page)` | -- |
| hover | `var(--border-hover)` | 同默认 | -- |
| focus | `var(--color-accent)` | 同默认 | `var(--focus-ring)` |
| error | `var(--color-danger-500)` | 同默认 | `0 0 0 3px rgba(239,68,68,0.15)` |
| disabled | `var(--border-color)` | `var(--color-neutral-100)` | `opacity: 0.5` |
| readonly | transparent | `var(--surface-primary)` | 无光标 |

---

## Textarea

- 同 Input 材质/状态
- 最小高度 88px，可垂直 resize
- padding: `var(--space-3)`

---

## Select

- 同 Input 材质/尺寸/状态
- `appearance: none`，右侧下拉箭头图标
- padding-right: 36px（为箭头留位）

---

## 通用规则

| 规则 | 说明 |
|------|------|
| 标签 | 上方，`var(--text-sm)`，`var(--weight-medium)` |
| 必填标记 | `*` 红色 `var(--color-danger-500)` |
| 错误消息 | 下方，`var(--text-xs)`，`var(--color-danger-500)` |
| 帮助文字 | 下方，`var(--text-xs)`，`var(--text-muted)` |
| 字段间距 | `var(--space-4)` 16px |

## 反例

- 不使用毛玻璃 backdrop-filter
- 不使用品牌色发光光晕（app 专属）
- 不使用 `var(--glass-*)` 变量

## a11y 验收点

- [ ] `<label>` 与 `<input>` 通过 `for`/`id` 关联
- [ ] error 态 `aria-invalid="true"` + `aria-describedby` 指向错误消息
- [ ] disabled 态 `disabled` 属性
- [ ] readonly 态 `readonly` 属性
- [ ] 颜色对比度 >= 4.5:1

---

## 99. 待确认问题

无

# 组件：Toast / Alert / Banner（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## Toast

| 属性 | 值 |
|------|-----|
| 位置 | 右上角 |
| 最大宽度 | 420px |
| 最小宽度 | 280px |
| 背景 | `var(--surface-elevated)` |
| 边框 | 1px solid `var(--border-color)` |
| 圆角 | `var(--radius-md)` |
| 阴影 | `var(--shadow-lg)` |
| 状态指示 | 左侧 3px 色条 |
| 自动消失 | info/success 3s，warning/error 5s |
| 最大堆叠 | 3 条 |

### 状态色条

| 类型 | 色条颜色 | 图标颜色 |
|------|---------|---------|
| success | `var(--color-success-500)` | `var(--color-success-500)` |
| error | `var(--color-danger-500)` | `var(--color-danger-500)` |
| warning | `var(--color-warning-500)` | `var(--color-warning-500)` |
| info | `var(--color-info-500)` | `var(--color-info-500)` |

---

## Alert

| 属性 | 值 |
|------|-----|
| 背景 | `var(--surface-primary)` |
| 边框 | 1px solid `var(--border-color)` |
| 左侧色条 | 4px solid 对应状态色 |
| 圆角 | `var(--radius-md)` |
| 可关闭 | 右上角关闭按钮（可选） |

---

## Banner

| 属性 | 值 |
|------|-----|
| 高度 | 44px |
| 宽度 | 100% |
| 位置 | 页面顶部 |
| info | `var(--btn-primary-bg)` 背景 + 白色文字 |
| warning | `var(--color-warning-50)` 背景 + `var(--color-warning-700)` 文字 |
| error | `var(--color-danger-50)` 背景 + `var(--color-danger-700)` 文字 |

---

## 反例

- 不使用毛玻璃 Toast
- 不使用弹跳入场动效

## a11y 验收点

- [ ] Toast: `role="status"` (info/success) / `role="alert"` (error/warning)
- [ ] Alert: `role="alert"` 或 `role="status"`
- [ ] 关闭按钮 `aria-label="关闭"`
- [ ] 自动消失的 Toast 不阻塞键盘操作

---

## 99. 待确认问题

无

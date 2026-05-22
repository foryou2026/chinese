# 组件：Checkbox / Radio / Switch（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Checkbox

| 属性 | 值 |
|------|-----|
| 尺寸 | 18px x 18px |
| 圆角 | `var(--radius-xs)` 2px |
| 边框 | 1px solid `var(--border-color)` |
| 选中背景 | `var(--btn-primary-bg)` |
| 选中图标 | 白色 ✓ |
| 过渡 | `var(--motion-fast)` |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 空白方框 |
| hover | 边框 `var(--border-hover)` |
| checked | 黑底白勾（light）/ 白底黑勾（dark） |
| indeterminate | 黑底白横线 |
| disabled | `opacity: 0.5` |
| focus | `var(--focus-ring)` |

---

## Radio

| 属性 | 值 |
|------|-----|
| 尺寸 | 18px x 18px |
| 圆角 | `var(--radius-pill)` |
| 边框 | 1px solid `var(--border-color)` |
| 选中 | 黑色实心圆点 6px |

### 状态

同 Checkbox，选中态为实心圆点。

---

## Switch

| 属性 | 值 |
|------|-----|
| 轨道尺寸 | 36px x 20px |
| 圆点尺寸 | 16px |
| 关闭轨道 | `var(--color-neutral-300)` |
| 开启轨道 | `var(--btn-primary-bg)` |
| 过渡 | `var(--motion-fast)` |

### 状态

| 状态 | 表现 |
|------|------|
| off | 灰色轨道，圆点靠左 |
| on | 黑色轨道（light）/ 白色轨道（dark），圆点靠右 |
| disabled | `opacity: 0.5` |
| focus | `var(--focus-ring)` |

---

## 通用标签规则

- 标签在右侧，间距 `var(--space-2)`
- 字号 `var(--text-sm)`
- 支持 description 副文本

## 反例

- 不使用品牌色渐变
- 不使用动画弹跳

## a11y 验收点

- [ ] Checkbox: `role="checkbox"` + `aria-checked`
- [ ] Radio: `role="radio"` + `aria-checked`，组内 `role="radiogroup"`
- [ ] Switch: `role="switch"` + `aria-checked`
- [ ] 所有组件 `aria-label` 或关联 `<label>`

---

## 99. 待确认问题

无

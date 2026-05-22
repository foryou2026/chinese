# 组件：Empty / Skeleton / Spinner / ProgressBar（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Skeleton

| 属性 | 值 |
|------|-----|
| 背景 | `var(--color-neutral-200)` |
| 动画 | shimmer 扫光，1.5s 循环 |
| 圆角 | `var(--radius-sm)` |

### 预设

| 预设 | 尺寸 |
|------|------|
| text | 16px 高，100% 宽 |
| title | 24px 高，60% 宽 |
| avatar-sm | 32px 圆形 |
| avatar-md | 40px 圆形 |
| image | 16:9 比例 |

---

## Spinner

| 尺寸 | 宽高 | 边框宽 |
|------|------|--------|
| sm | 16px | 2px |
| md | 24px | 3px |
| lg | 40px | 4px |

| 属性 | 值 |
|------|-----|
| 轨道色 | `var(--color-neutral-200)` |
| 活动色 | `var(--btn-primary-bg)` |
| 反色轨道 | `rgba(255,255,255,0.25)` |
| 反色活动 | white |
| 动画 | 旋转 0.7s linear 无限 |

---

## ProgressBar

| 尺寸 | 高度 |
|------|------|
| sm | 4px |
| md | 8px |
| lg | 12px |

| 属性 | 值 |
|------|-----|
| 背景 | `var(--color-neutral-200)` |
| 填充 | `var(--btn-primary-bg)` |
| 圆角 | `var(--radius-pill)` |
| 过渡 | `var(--motion-base)` |
| 不确定态 | 40% 宽度左右滑动 |

### 状态变体

| 变体 | 填充色 |
|------|--------|
| success | `var(--color-success-500)` |
| warning | `var(--color-warning-500)` |
| danger | `var(--color-danger-500)` |

---

## Empty

| 属性 | 值 |
|------|-----|
| 最小高度 | 200px |
| 图标尺寸 | 48px |
| 图标色 | `var(--color-neutral-300)` |
| 标题字号 | `var(--text-base)` |
| 描述字号 | `var(--text-sm)` |
| 描述颜色 | `var(--text-muted)` |
| 背景 | `var(--surface-primary)` |
| 边框 | 1px solid `var(--border-color)` |
| 圆角 | `var(--radius-lg)` |

---

## 反例

- Spinner 不使用品牌色渐变
- ProgressBar 不使用渐变填充
- 不使用游戏化动效（庆祝、弹跳）

## a11y 验收点

- [ ] Spinner: `aria-label="加载中"` 或包裹 `aria-busy="true"` 容器
- [ ] ProgressBar: `role="progressbar"` + `aria-valuenow`/`aria-valuemin`/`aria-valuemax`
- [ ] Skeleton: 容器 `aria-busy="true"` + `aria-label`

---

## 99. 待确认问题

无

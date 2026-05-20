# 组件：Checkbox / Radio / Switch

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

| 组件 | 用途 | 禁忌 |
|------|------|------|
| Checkbox | 多选、同意条款、布尔字段 | 不用于互斥选择（用 Radio） |
| Radio | 互斥单选（3-7 项） | 不用于 >7 项（用 Select） |
| Switch | 即时生效的开关 | 不用于表单提交后才生效的选择（用 Checkbox） |

---

## Checkbox

### 尺寸

| 尺寸 | 框尺寸 | 标签字号 | 间距 |
|------|--------|---------|------|
| md | 20px x 20px | `var(--text-base)` | 8px |

### 状态

| 状态 | 边框 | 背景 | 勾选图标 |
|------|------|------|---------|
| 默认（未选） | `2px var(--color-neutral-300)` | transparent | 无 |
| 默认（已选） | 无 | `var(--color-brand-default)` | white check |
| hover（未选） | `2px var(--color-brand-400)` | transparent | 无 |
| hover（已选） | 无 | `var(--color-brand-hover)` | white check |
| focus | `var(--focus-ring)` | 同上 | 同上 |
| active | — | `var(--color-brand-active)` | white check |
| disabled（未选） | `2px var(--color-neutral-200)` | `var(--color-neutral-100)` | 无 |
| disabled（已选） | 无 | `var(--color-neutral-300)` | white check |
| error | `2px var(--color-danger-500)` | — | — |
| indeterminate | 无 | `var(--color-brand-default)` | white dash |

### 动画

选中/取消：`scale(0 → 1)` + check 路径绘制，`var(--motion-fast)`。

---

## Radio

### 尺寸

| 尺寸 | 外圈直径 | 内圈直径 | 标签字号 |
|------|---------|---------|---------|
| md | 20px | 10px | `var(--text-base)` |

### 状态

| 状态 | 外圈 | 内圈 |
|------|------|------|
| 默认（未选） | `2px var(--color-neutral-300)` | 无 |
| 默认（已选） | `2px var(--color-brand-default)` | `var(--color-brand-default)` |
| hover（未选） | `2px var(--color-brand-400)` | 无 |
| hover（已选） | `2px var(--color-brand-hover)` | `var(--color-brand-hover)` |
| focus | `var(--focus-ring)` | 同上 |
| disabled | `2px var(--color-neutral-200)` | `var(--color-neutral-300)` |
| error | `2px var(--color-danger-500)` | — |

### 布局

| 排列 | 使用场景 |
|------|---------|
| 垂直堆叠 | ≥3 项 |
| 水平排列 | 2-3 项且标签短 |
| 间距 | 选项间 `var(--space-3)` |

---

## Switch

### 尺寸

| 尺寸 | 轨道宽 | 轨道高 | 滑块直径 |
|------|--------|--------|---------|
| md | 44px | 24px | 20px |

### 状态

| 状态 | 轨道色 | 滑块色 | 位置 |
|------|--------|--------|------|
| 默认（关） | `var(--color-neutral-300)` | white | 左 |
| 默认（开） | `var(--color-brand-default)` | white | 右 |
| hover（关） | `var(--color-neutral-400)` | white | 左 |
| hover（开） | `var(--color-brand-hover)` | white | 右 |
| focus | `var(--focus-ring)` 套住轨道 | — | — |
| active | — | `scale(1.1)` | 过渡中 |
| disabled（关） | `var(--color-neutral-200)` | `var(--color-neutral-100)` | 左 |
| disabled（开） | `var(--color-brand-200)` | white | 右 |
| loading | 同当前状态 | spinner 替代滑块 | 固定 |

### 动画

滑块移动：`var(--motion-fast)` `var(--easing-out)`。

### 行为

| 交互 | 行为 |
|------|------|
| 点击轨道/标签 | 切换 |
| 拖拽滑块 | 实时跟手，释放后吸附 |
| Space/Enter | 切换 |
| 即时生效 | Switch 切换后立即执行操作，不依赖表单提交 |

### a11y

- `role="switch"`
- `aria-checked="true/false"`
- 必须有 `aria-label` 或关联标签

---

## 99. 待确认问题

无

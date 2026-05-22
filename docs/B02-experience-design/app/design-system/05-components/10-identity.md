# 组件：Avatar / Badge / Tag / Chip

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Avatar

### 用途

展示用户/系统头像。

### 尺寸

| 尺寸 | 直径 | 字号(fallback) | 场景 |
|------|------|---------------|------|
| xs | 24px | `var(--text-xs)` | 评论列表、行内提及 |
| sm | 32px | `var(--text-sm)` | 导航栏、消息列表 |
| md | 40px | `var(--text-base)` | 用户卡片、设置页 |
| lg | 64px | `var(--text-xl)` | 个人主页 |
| xl | 96px | `var(--text-2xl)` | 编辑头像 |

### 样式

| 属性 | 值 |
|------|-----|
| 圆角 | `var(--radius-pill)` （圆形） |
| 边框 | `2px var(--color-neutral-0)` （暖白，在深色背景上） |
| fallback（无图） | 首字母大写，背景 `var(--color-brand-100)`，文字 `var(--color-brand-600)` |
| 加载失败 | 同 fallback |
| 在线状态 | 右下角 `var(--color-success-500)` 圆点（10px），2px 白色边框 |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 显示图片或 fallback |
| hover | 可选，叠加 `var(--glass-bg-card)` 遮罩 + 编辑图标 |
| loading | Skeleton 圆形（`var(--glass-bg-card)` + shimmer） |

### Avatar Group

- 重叠排列，每个头像左偏移 -8px
- 最多显示 5 个，超出显示 "+N"
- "+N" 使用 `var(--color-neutral-200)` 背景，`var(--color-neutral-600)` 文字

---

## Badge

### 用途

数字角标或状态点，附着在其他元素（图标、头像）右上角。

### 变体

| 变体 | 说明 | 示例 |
|------|------|------|
| dot | 无数字，仅红点 | 未读标记 |
| count | 数字 | 消息数 3 |
| max | 超限显示 "99+" | 通知 99+ |

### 样式

| 属性 | dot | count |
|------|-----|-------|
| 尺寸 | 8px 圆 | min-width 20px, height 20px |
| 背景 | `var(--color-danger-500)` (red) | `var(--color-danger-500)` |
| 文字 | 无 | white, `var(--text-xs)`, `var(--weight-semibold)` |
| 圆角 | `var(--radius-pill)` | `var(--radius-pill)` |
| padding | 0 | 0 6px |
| 位置 | 右上角，偏移 -4px | 右上角，偏移 -8px |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | 显示 |
| 0 值 | 隐藏（不显示 "0"） |
| 进入 | `scale(0→1)` `var(--motion-fast)` `var(--easing-spring)` |
| 退出 | `scale(1→0)` `var(--motion-fast)` |

---

## Tag

### 用途

静态标签，展示分类、状态、属性。不可交互或仅可删除。

### 变体

| 变体 | 说明 |
|------|------|
| filled | 有色背景 + 深色文字 |
| outline | 边框 + 有色文字 |

### 颜色

| 颜色 | 背景(filled) | 文字 | 边框(outline) |
|------|-------------|------|--------------|
| brand | `var(--color-brand-100)` | `var(--color-brand-700)` | `var(--color-brand-300)` |
| neutral | `var(--color-neutral-100)` | `var(--color-neutral-600)` | `var(--color-neutral-300)` |
| success emerald | `var(--color-success-50)` | `var(--color-success-700)` | — |
| warning amber | `var(--color-warning-50)` | `var(--color-warning-700)` | — |
| danger red | `var(--color-danger-50)` | `var(--color-danger-700)` | — |
| info blue | `var(--color-info-50)` | `var(--color-info-700)` | — |

### 尺寸

| 尺寸 | 高度 | padding-x | 字号 |
|------|------|-----------|------|
| sm | 22px | 8px | `var(--text-xs)` |
| md | 28px | 10px | `var(--text-sm)` |

### 样式

| 属性 | 值 |
|------|-----|
| 圆角 | `var(--radius-xl)` |
| 可删除 | 可选，右侧 X 按钮（16px），hover 变深 |
| 图标 | 可选，左侧 14px |

---

## Chip

### 用途

可交互的选择标签，支持选中/取消。用于多选筛选场景。

### 与 Tag 的区别

| 维度 | Tag | Chip |
|------|-----|------|
| 交互 | 无/仅删除 | 可选中/取消 |
| 场景 | 展示属性 | 筛选条件 |
| cursor | default | pointer |

### 状态

| 状态 | 背景 | 文字 | 边框 |
|------|------|------|------|
| 默认（未选） | transparent | `var(--color-neutral-500)` | `1px solid var(--color-neutral-200)` |
| hover（未选） | `var(--glass-bg-card)` | `var(--color-neutral-700)` | `1px solid var(--color-neutral-300)` |
| 选中 | `var(--color-brand-50)` | `var(--color-brand-default)` | `1px solid var(--color-brand-300)` |
| hover（选中） | `var(--color-brand-100)` | `var(--color-brand-hover)` | `1px solid var(--color-brand-400)` |
| focus | `var(--focus-ring)` | — | — |
| disabled | `var(--color-neutral-50)` | `var(--color-neutral-400)` | `1px solid var(--color-neutral-200)` |

| 属性 | 值 |
|------|-----|
| 高度 | 32px |
| padding | `0 var(--space-3)` |
| 圆角 | `var(--radius-pill)` |
| 选中图标 | 左侧 check 16px（选中态追加） |
| 过渡 | `var(--motion-fast)` |

---

## 99. 待确认问题

无

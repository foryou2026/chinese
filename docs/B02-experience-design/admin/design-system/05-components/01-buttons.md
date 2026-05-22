# 组件：Button / IconButton（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：触发操作（提交、导航、确认、取消、删除）
- 禁忌：不用于纯导航链接（用 `<a>` 标签）；不用于切换状态（用 Switch）

## 变体

| 变体 | 说明 | CSS class | 示例语境 |
|------|------|-----------|---------|
| primary | 纯黑底白字（light）/ 纯白底黑字（dark） | `.admin-btn-primary` | 提交表单、新建资源 |
| secondary | 白底 + 1px 边框 | `.admin-btn-secondary` | 取消、返回、次要操作 |
| ghost | 透明底 -> hover 变灰底 | `.admin-btn-ghost` | 工具栏操作、更多选项 |
| destructive | 红色底白字 | `.admin-btn-destructive` | 删除、封禁 |
| success | 绿色底白字 | `.admin-btn-success` | 审核通过、发布 |
| icon-only | 透明方块 -> hover 变灰底 | `.admin-btn-icon` | 关闭、搜索、编辑、设置 |
| link | 蓝色文字链接 | `.admin-btn-link` | 内联操作、"查看详情" |

## 尺寸

| 尺寸 | 高度 | padding-x | 字号 | 图标尺寸 | 圆角 |
|------|------|-----------|------|---------|------|
| sm | 36px | 16px | `var(--text-sm)` 14px | 16px | `var(--radius-md)` 8px |
| md | 44px | 20px | `var(--text-sm)` 14px | 18px | `var(--radius-md)` 8px |
| lg | 52px | 28px | `var(--text-base)` 16px | 20px | `var(--radius-md)` 8px |

> 移动端最小触控区域 48px，sm 按钮需确保包含 padding 后 >=48px。

## 通用按钮属性

| 属性 | 值 |
|------|-----|
| 字体 | `var(--font-sans)` |
| 字重 | `var(--weight-medium)` |
| 过渡 | `var(--motion-fast)` (100ms ease) |
| hover | 背景色变化，无 translateY 浮起 |
| 按下 | 背景色加深，无 scale 缩放 |

## 状态

### primary 变体（纯黑/纯白）

| 状态 | 背景 | 文字 | 其他 |
|------|------|------|------|
| 默认 | `var(--btn-primary-bg)` #18181B | `var(--btn-primary-text)` #FAFAFA | -- |
| hover | `var(--btn-primary-bg-hover)` #27272A | #FAFAFA | -- |
| focus | 同默认 | -- | `var(--focus-ring)` |
| active | `var(--btn-primary-bg-active)` #09090B | #FAFAFA | -- |
| disabled | `opacity: 0.50` | -- | `cursor: not-allowed; pointer-events: none` |
| loading | 同默认 opacity:0.70 | hidden | Spinner 替代文字 |

### secondary 变体（白底边框）

| 状态 | 背景 | 文字 | 边框 |
|------|------|------|------|
| 默认 | `var(--btn-secondary-bg)` #FFFFFF | `var(--btn-secondary-text)` #374151 | 1px solid `var(--btn-secondary-border)` #D1D5DB |
| hover | `var(--btn-secondary-bg-hover)` #F9FAFB | #374151 | #D1D5DB |
| focus | 同默认 | -- | `var(--focus-ring)` |
| active | `var(--btn-secondary-bg-active)` #F3F4F6 | #374151 | #D1D5DB |
| disabled | `opacity: 0.50` | -- | -- |

### ghost 变体（透明底）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | transparent | `var(--text-secondary)` #6B7280 |
| hover | `var(--color-neutral-100)` #F3F4F6 | `var(--text-primary)` #111827 |
| active | `var(--color-neutral-200)` #E5E7EB | `var(--text-primary)` |
| disabled | transparent, `opacity: 0.50` | -- |

### destructive 变体（危险红）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | `var(--color-danger-500)` #EF4444 | white |
| hover | `var(--color-danger-700)` #B91C1C | white |
| active | #991B1B | white |
| disabled | `opacity: 0.50` | -- |

### success 变体（成功绿）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | `var(--color-success-500)` #10B981 | white |
| hover | `var(--color-success-700)` #047857 | white |
| active | #065F46 | white |
| disabled | `opacity: 0.50` | -- |

### icon-only 变体

| 状态 | 背景 | 图标颜色 |
|------|------|---------|
| 默认 | `var(--glass-bg)` + `backdrop-filter: var(--glass-blur-sm)` | `var(--text-secondary)` |
| hover | `var(--glass-bg-card)` | `var(--text-primary)` |
| active | `var(--glass-bg-elevated)` | `var(--text-primary)` |
| disabled | transparent, `opacity: 0.50` | -- |

| 尺寸 | 宽高 | 图标 | 圆角 |
|------|------|------|------|
| sm | 36px x 36px | 16px | `var(--radius-md)` |
| md | 44px x 44px | 18px | `var(--radius-md)` |
| lg | 52px x 52px | 20px | `var(--radius-md)` |

### link 变体（文字链接）

| 状态 | 文字 | 装饰 |
|------|------|------|
| 默认 | `var(--color-accent)` #3B82F6 | 无下划线 |
| hover | `var(--color-accent-hover)` #2563EB | 下划线 |
| active | #1D4ED8 | 下划线 |
| disabled | `var(--text-muted)`, `opacity: 0.50` | 无 |

## Anatomy

```
┌───────────────────────────┐
│ [icon?] [label] [icon?]    │  ← 纯实色背景，无渐变，无毛玻璃
└───────────────────────────┘

Loading 态：
┌───────────────────────────┐
│        [spinner]           │
└───────────────────────────┘
```

- 图标可选，支持 left/right 位置
- loading 态 spinner 居中，文字隐藏但保留宽度（防止按钮宽度跳变）

## 行为

| 交互 | 行为 |
|------|------|
| 键盘 Enter/Space | 触发 click |
| Tab | 聚焦，显示焦点环 `var(--focus-ring)` |
| disabled 时 Tab | 跳过 |
| loading 时点击 | 忽略（pointer-events: none） |
| 双击 | 防抖，忽略第二次 |

## 反例

- 不使用渐变背景（admin 使用纯实色）
- 不使用毛玻璃 backdrop-filter
- 不使用 inset 高光 `::before`
- 不使用 translateY(-1px) hover 浮起
- 不使用 scale(0.98) 按下缩放
- 不使用 ripple 水波纹动画
- 不使用胶囊形（`radius-pill`）作为默认

## a11y 验收点

- [ ] `role="button"`（非 `<button>` 元素时）
- [ ] disabled 时 `aria-disabled="true"`
- [ ] loading 时 `aria-busy="true"` + spinner 有 `aria-label="加载中"`
- [ ] icon-only 按钮必须有 `aria-label`
- [ ] 颜色对比度 >=4.5:1（文字/背景）

---

## 99. 待确认问题

无

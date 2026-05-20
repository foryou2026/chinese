# 组件：Button / IconButton

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：触发操作（提交、导航、确认、取消）
- 禁忌：不用于纯导航链接（用 `<a>` 标签）；不用于切换状态（用 Switch）

## 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| primary | 主色填充，白色文字 | 提交表单、开始学习 |
| accent | 强调色(orange)填充，白色文字 | CTA、领取奖励、立即开始 |
| secondary | 白色/透明填充，主色边框+文字 | 取消、返回、次要操作 |
| ghost | 透明背景，主色文字 | 工具栏操作、更多选项 |
| destructive | error 色填充，白色文字 | 删除、注销 |
| icon-only | 仅图标，圆形或方形 | 关闭、搜索、设置 |

## 尺寸

| 尺寸 | 高度 | padding-x | 字号 | 图标尺寸 | 圆角 |
|------|------|-----------|------|---------|------|
| sm | 32px | 12px | var(--text-sm) | 16px | var(--radius-md) |
| md | 40px | 16px | var(--text-sm) | 20px | var(--radius-md) |
| lg | 48px | 24px | var(--text-base) | 20px | var(--radius-lg) |

> 移动端最小触控区域 44px，sm 按钮需确保包含 padding 后 ≥44px。

## 状态

### primary 变体

| 状态 | 背景 | 文字 | 边框 | 其他 |
|------|------|------|------|------|
| 默认 | var(--color-primary-500) | white | 无 | — |
| hover | var(--color-primary-600) | white | 无 | — |
| focus | var(--color-primary-500) | white | 焦点环 2px | outline-offset: 2px |
| active | var(--color-primary-700) | white | 无 | transform: scale(0.97) |
| disabled | var(--color-neutral-200) | var(--color-neutral-400) | 无 | cursor: not-allowed |
| loading | var(--color-primary-500) opacity:0.7 | hidden | 无 | Spinner 替代文字 |

### secondary 变体

| 状态 | 背景 | 文字 | 边框 | 其他 |
|------|------|------|------|------|
| 默认 | transparent | var(--color-primary-500) | 1px var(--color-primary-500) | — |
| hover | var(--color-primary-50) | var(--color-primary-600) | 1px var(--color-primary-600) | — |
| focus | transparent | var(--color-primary-500) | 焦点环 | — |
| active | var(--color-primary-100) | var(--color-primary-700) | 1px var(--color-primary-700) | scale(0.97) |
| disabled | transparent | var(--color-neutral-400) | 1px var(--color-neutral-200) | not-allowed |
| loading | transparent opacity:0.7 | hidden | 1px var(--color-primary-500) | Spinner |

### ghost 变体

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | transparent | var(--color-primary-500) |
| hover | var(--color-neutral-100) | var(--color-primary-600) |
| active | var(--color-neutral-200) | var(--color-primary-700) |
| disabled | transparent | var(--color-neutral-400) |

### accent 变体

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | var(--color-accent-500) | white |
| hover | var(--color-accent-600) | white |
| active | var(--color-accent-700) | white |
| disabled | var(--color-neutral-200) | var(--color-neutral-400) |

### destructive 变体

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | var(--color-error) | white |
| hover | #dc2626 | white |
| active | #b91c1c | white |
| disabled | var(--color-neutral-200) | var(--color-neutral-400) |

## Anatomy

```
┌─────────────────────────┐
│ [icon?] [label] [icon?] │
└─────────────────────────┘

Loading 态：
┌─────────────────────────┐
│      [spinner]          │
└─────────────────────────┘
```

- 图标可选，支持 left/right 位置
- loading 态 spinner 居中，文字隐藏但保留宽度（防止按钮宽度跳变）

## 行为

| 交互 | 行为 |
|------|------|
| 键盘 Enter/Space | 触发 click |
| Tab | 聚焦，显示焦点环 |
| disabled 时 Tab | 跳过 |
| loading 时点击 | 忽略（pointer-events: none） |
| 双击 | 防抖，忽略第二次 |

## 与 token 的对应

| 属性 | token |
|------|-------|
| 圆角 | var(--radius-md) / var(--radius-lg) |
| 字重 | var(--font-medium) |
| 过渡 | var(--motion-fast) var(--ease-default) |
| 按下缩放 | transform: scale(0.97)，var(--motion-fast) |

## 反例

- 不使用渐变背景填充
- 不使用 ripple 水波纹动画
- 不使用胶囊形（radius-full）作为默认——仅特殊场景（如浮动操作按钮）使用

## a11y 验收点

- [ ] `role="button"`（非 `<button>` 元素时）
- [ ] disabled 时 `aria-disabled="true"`
- [ ] loading 时 `aria-busy="true"` + spinner 有 `aria-label="加载中"`
- [ ] icon-only 按钮必须有 `aria-label`
- [ ] 颜色对比度 ≥4.5:1（文字/背景）

---

## 99. 待确认问题

无

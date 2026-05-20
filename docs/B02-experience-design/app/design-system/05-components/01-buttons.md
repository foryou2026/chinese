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

| 变体 | 说明 | CSS class | 示例语境 |
|------|------|-----------|---------|
| primary | 墨青渐变 + 毛玻璃高光 | `.proto-btn-primary` | 提交表单、开始学习 |
| secondary | 强毛玻璃 + 品牌色边框 | `.proto-btn-secondary` | 取消、返回、次要操作 |
| ghost | 透明→hover 毛玻璃 | `.proto-btn-ghost` | 工具栏操作、更多选项 |
| glass | 标准毛玻璃面板 | `.proto-btn-glass` | 卡片内操作、筛选 |
| destructive | 朱砂渐变 + 毛玻璃 | `.proto-btn-destructive` | 删除、注销 |
| success | 翠玉渐变 + 毛玻璃 | `.proto-btn-success` | 确认、完成 |
| icon-only | 毛玻璃方块 | `.proto-btn-icon` | 关闭、搜索、设置 |
| link | 品牌色文字链接 | `.proto-btn-link` | 内联操作 |

## 尺寸

| 尺寸 | 高度 | padding-x | 字号 | 图标尺寸 | 圆角 |
|------|------|-----------|------|---------|------|
| sm | 32px | 12px | `var(--text-sm)` | 16px | `var(--radius-sm)` |
| md | 40px | 16px | `var(--text-sm)` | 20px | `var(--radius-md)` |
| lg | 48px | 24px | `var(--text-base)` | 20px | `var(--radius-md)` |

> 移动端最小触控区域 44px，sm 按钮需确保包含 padding 后 ≥44px。

## 通用按钮属性

| 属性 | 值 |
|------|-----|
| 字体 | `var(--font-display)` |
| 字重 | `var(--weight-medium)` |
| 字间距 | `letter-spacing: 1px` |
| 过渡 | `var(--motion-fast)` |
| hover 微浮起 | `transform: translateY(-1px)` |
| 按下缩放 | `transform: scale(0.97)` |

## 状态

### primary 变体（墨青渐变）

| 状态 | 背景 | 文字 | 其他 |
|------|------|------|------|
| 默认 | `linear-gradient(135deg, var(--color-brand-700), var(--color-brand-600))` + `backdrop-filter: blur(8px)` | `var(--color-brand-on)` | 顶部 inset 高光 |
| hover | 渐变提亮至 brand-600→brand-500 | `var(--color-brand-on)` | `translateY(-1px)` + `var(--glass-shadow)` |
| focus | 同默认 | — | `var(--focus-ring)` |
| active | brand-800→brand-700 | `var(--color-brand-on)` | `scale(0.97)` |
| disabled | `opacity: 0.45` | — | `cursor: not-allowed; pointer-events: none` |
| loading | 同默认 opacity:0.7 | hidden | Spinner 替代文字 |

### secondary 变体（强毛玻璃边框）

| 状态 | 背景 | 文字 | 边框 |
|------|------|------|------|
| 默认 | `var(--glass-2)` + `backdrop-filter: var(--glass-blur-sm)` | `var(--color-brand-default)` | `1px solid var(--color-brand-300)` |
| hover | 提高透明度 | `var(--color-brand-hover)` | brand-400 | 
| focus | 同默认 | — | `var(--focus-ring)` |
| active | 加深 | `var(--color-brand-active)` | brand-500 |
| disabled | `opacity: 0.45` | — | — |

### ghost 变体（透明→毛玻璃）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | transparent | `var(--color-brand-default)` |
| hover | `var(--glass-3)` + `backdrop-filter: var(--glass-blur-sm)` | `var(--color-brand-hover)` |
| active | `var(--glass-1)` | `var(--color-brand-active)` |
| disabled | transparent, `opacity: 0.45` | — |

### glass 变体（标准毛玻璃）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | `var(--glass-1)` + `backdrop-filter: var(--glass-blur)` + `var(--glass-border)` | `var(--color-neutral-700)` |
| hover | `var(--glass-2)` | `var(--color-neutral-800)` |
| active | `var(--glass-2)` 加深 | `var(--color-neutral-900)` |
| disabled | `opacity: 0.45` | — |

### destructive 变体（朱砂渐变）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | `linear-gradient(135deg, var(--color-danger-700), var(--color-danger-500))` + blur | white |
| hover | 提亮 danger-500→danger-200 | white |
| active | 加深 danger-700 | white |
| disabled | `opacity: 0.45` | — |

### success 变体（翠玉渐变）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | `linear-gradient(135deg, var(--color-success-700), var(--color-success-500))` + blur | white |
| hover | 提亮 | white |
| active | 加深 | white |
| disabled | `opacity: 0.45` | — |

## Anatomy

```
┌─────────────────────────────────┐
│ [icon?] [label] [icon?]          │  ← backdrop-filter + glass 材质
│ ░░░░░ 顶部 1px inset 高光 ░░░░░ │
└─────────────────────────────────┘

Loading 态：
┌─────────────────────────────────┐
│        [spinner]                 │
└─────────────────────────────────┘
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

- ~~不使用渐变背景填充~~ → **使用**品牌色渐变 + 毛玻璃（P1 原则）
- 不使用 ripple 水波纹动画
- 不使用胶囊形（`radius-pill`）作为默认——仅特殊场景使用
- 不使用纯实色填充（必须有 backdrop-filter 或渐变 + inset 高光）

## a11y 验收点

- [ ] `role="button"`（非 `<button>` 元素时）
- [ ] disabled 时 `aria-disabled="true"`
- [ ] loading 时 `aria-busy="true"` + spinner 有 `aria-label="加载中"`
- [ ] icon-only 按钮必须有 `aria-label`
- [ ] 颜色对比度 ≥4.5:1（文字/背景）

---

## 99. 待确认问题

无

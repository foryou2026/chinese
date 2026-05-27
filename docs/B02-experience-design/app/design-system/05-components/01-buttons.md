# 组件：Button / IconButton

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：触发操作（提交、导航、确认、取消、开始学习、提交答案）
- 禁忌：不用于纯导航链接（用 `<a>` 标签）；不用于切换状态（用 Switch）

## 变体

| 变体 | 说明 | CSS class | 示例语境 |
|------|------|-----------|---------|
| game | **Duolingo 风格 3D 按钮** — 品牌色填充 + 底部阴影 + 胶囊圆角 + 弹簧回弹 | `.btn-game` | 开始学习、提交答案、继续下一课 |
| primary | 品牌渐变 + 毛玻璃高光 | `.btn-primary` | 提交表单、确认操作 |
| secondary | 强毛玻璃 + 品牌色边框 | `.btn-secondary` | 取消、返回、次要操作 |
| ghost | 透明->hover 毛玻璃 | `.btn-ghost` | 工具栏操作、更多选项 |
| glass | 标准毛玻璃面板 | `.btn-glass` | 卡片内操作、筛选 |
| destructive | 危险红 3D 底部阴影 | `.btn-destructive` | 删除、注销 |
| success | 成功绿 3D 底部阴影 | `.btn-success` | 确认完成、提交正确 |
| icon-only | 毛玻璃圆形 | `.btn-icon` | 关闭、搜索、设置 |
| link | 品牌色文字链接 | `.btn-link` | 内联操作 |

> `game` 变体是 app 系统中出现频率最高的按钮，用于所有核心学习交互。它是 Duolingo 标志性的大圆角 3D 按钮。

## 尺寸

| 尺寸 | 高度 | padding-x | 字号 | 图标尺寸 | 圆角 |
|------|------|-----------|------|---------|------|
| sm | 36px | 16px | `var(--text-sm)` | 16px | `var(--radius-pill)` |
| md | 44px | 20px | `var(--text-sm)` | 20px | `var(--radius-pill)` |
| lg | 48px | 28px | `var(--text-base)` | 20px | `var(--radius-pill)` |
| xl | 56px | 32px | `var(--text-md)` | 24px | `var(--radius-pill)` |

> **移动端最小触控高度 48px**。sm 按钮在移动端需确保包含 padding 后触控区域 >=48px。
> **主 CTA 按钮统一使用 `--radius-pill`**（胶囊圆角），这是 Duolingo 风格的核心视觉标识。

## 通用按钮属性

| 属性 | 值 |
|------|-----|
| 字体 | `var(--font-display)` |
| 字重 | `var(--weight-semibold)`（game 变体使用 `var(--weight-bold)`） |
| 字间距 | `letter-spacing: -0.01em` |
| 过渡 | `var(--motion-fast)` + `var(--easing-spring)`（game 变体） |
| min-width | 120px（game/primary/secondary 变体，防止按钮太窄） |

## 状态

### game 变体（Duolingo 风格 3D 按钮）

| 状态 | 背景 | 文字 | box-shadow | transform | 其他 |
|------|------|------|-----------|-----------|------|
| 默认 | `var(--color-brand-default)` 纯色 | `var(--color-brand-on)` 白色 | `0 4px 0 0 var(--color-brand-700)` | none | — |
| hover | `var(--color-brand-hover)` 提亮 | 白色 | `0 4px 0 0 var(--color-brand-700)` | `translateY(-1px)` | 阴影微增 |
| focus | 同默认 | — | `var(--focus-ring), 0 4px 0 0 var(--color-brand-700)` | none | 焦点环叠加底部阴影 |
| active/pressed | `var(--color-brand-active)` 加深 | 白色 | `0 2px 0 0 var(--color-brand-800)` | `translateY(2px)` | 按下位移 + 阴影缩短，弹簧回弹 `var(--easing-spring)` |
| disabled | `var(--color-neutral-300)` | `var(--color-neutral-0)` | `0 4px 0 0 var(--color-neutral-400)` | none | `opacity: 0.65; cursor: not-allowed; pointer-events: none` |
| loading | 同默认 opacity:0.7 | hidden | 同默认 | none | Spinner 替代文字 |

```css
.btn-game {
  background: var(--color-brand-default);
  color: var(--color-brand-on);
  border: none;
  border-radius: var(--radius-pill);
  box-shadow: 0 4px 0 0 var(--color-brand-700);
  font-weight: var(--weight-bold);
  transition: transform 150ms var(--easing-spring),
              box-shadow 150ms var(--easing-spring),
              background 150ms ease;
}
.btn-game:hover {
  background: var(--color-brand-hover);
  transform: translateY(-1px);
}
.btn-game:active {
  background: var(--color-brand-active);
  transform: translateY(2px);
  box-shadow: 0 2px 0 0 var(--color-brand-800);
}
```

### primary 变体（品牌渐变）

| 状态 | 背景 | 文字 | 其他 |
|------|------|------|------|
| 默认 | `linear-gradient(135deg, var(--color-brand-700), var(--color-brand-600))` + `backdrop-filter: blur(8px)` | `var(--color-brand-on)` | 顶部 inset 高光 |
| hover | 渐变提亮至 brand-600->brand-500 | `var(--color-brand-on)` | `translateY(-1px)` + `var(--shadow-sm)` |
| focus | 同默认 | — | `var(--focus-ring)` |
| active | brand-800->brand-700 | `var(--color-brand-on)` | `scale(0.98)` |
| disabled | `opacity: 0.45` | — | `cursor: not-allowed; pointer-events: none` |
| loading | 同默认 opacity:0.7 | hidden | Spinner 替代文字 |

### secondary 变体（强毛玻璃边框）

| 状态 | 背景 | 文字 | 边框 |
|------|------|------|------|
| 默认 | `var(--glass-bg)` + `backdrop-filter: var(--glass-blur-sm)` | `var(--color-brand-default)` | `1px solid var(--color-brand-300)` |
| hover | 提高透明度 | `var(--color-brand-hover)` | brand-400 |
| focus | 同默认 | — | `var(--focus-ring)` |
| active | 加深 | `var(--color-brand-active)` | brand-500 |
| disabled | `opacity: 0.45` | — | — |

### ghost 变体（透明->毛玻璃）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | transparent | `var(--color-brand-default)` |
| hover | `var(--glass-bg)` + `backdrop-filter: var(--glass-blur-sm)` | `var(--color-brand-hover)` |
| active | `var(--glass-bg-card)` | `var(--color-brand-active)` |
| disabled | transparent, `opacity: 0.45` | — |

### glass 变体（标准毛玻璃）

| 状态 | 背景 | 文字 |
|------|------|------|
| 默认 | `var(--glass-bg)` + `backdrop-filter: var(--glass-blur)` + `var(--glass-border)` | `var(--color-neutral-700)` |
| hover | `var(--glass-bg-card)` | `var(--color-neutral-800)` |
| active | `var(--glass-bg-elevated)` 加深 | `var(--color-neutral-900)` |
| disabled | `opacity: 0.45` | — |

### destructive 变体（危险红 3D）

| 状态 | 背景 | 文字 | box-shadow |
|------|------|------|-----------|
| 默认 | `var(--color-danger-500)` | white | `0 4px 0 0 var(--color-danger-700)` |
| hover | `var(--color-danger-200)` 提亮 | white | 同默认 + `translateY(-1px)` |
| active | `var(--color-danger-700)` | white | `0 2px 0 0 var(--color-danger-800)` + `translateY(2px)` |
| disabled | `opacity: 0.45` | — | — |

### success 变体（成功绿 3D）

| 状态 | 背景 | 文字 | box-shadow |
|------|------|------|-----------|
| 默认 | `var(--color-success-500)` | white | `0 4px 0 0 var(--color-success-700)` |
| hover | 提亮 | white | 同默认 + `translateY(-1px)` |
| active | 加深 | white | `0 2px 0 0 var(--color-success-700)` + `translateY(2px)` |
| disabled | `opacity: 0.45` | — | — |

## Anatomy

```
game 变体：
┌─────────────────────────────────┐
│    [icon?] [label] [icon?]       │  <-- 品牌色纯色背景 + 胶囊圆角
│                                  │
├═════════════════════════════════┤  <-- 底部 4px 阴影层（深色）
└─────────────────────────────────┘

primary 变体：
┌─────────────────────────────────┐
│ [icon?] [label] [icon?]          │  <-- backdrop-filter + glass 材质
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
| 按下释放（game 变体） | 按下 `translateY(2px)` + 阴影缩短；释放后弹簧回弹 `var(--easing-spring)` |

## 涟漪/波纹效果（Ant Design 6 风格）

所有可点击按钮在点击时触发一次性涟漪扩散动画，提供清晰的操作确认感：

| 属性 | 值 |
|------|-----|
| 触发 | `click` / `touchstart`（仅触发一次，不重复叠加） |
| 形状 | 从点击坐标向外扩散的圆形波纹 |
| 颜色 | 当前按钮主色 15% 透明度（game/primary: `var(--color-brand-ring)`，glass/ghost: `rgba(0,0,0,0.06)`） |
| 持续时间 | 400ms |
| 缓动 | `var(--easing-out)` |
| 实现 | `::after` 伪元素 + CSS `@keyframes`，由 JS 在 click 时添加 `.ripple-active` class |
| 溢出 | `overflow: hidden` 裁切在按钮边界内 |

```css
@keyframes btn-ripple {
  0%   { transform: translate(-50%, -50%) scale(0); opacity: 0.4; }
  100% { transform: translate(-50%, -50%) scale(4); opacity: 0; }
}
.ripple-active::after {
  content: '';
  position: absolute;
  width: 100%; aspect-ratio: 1;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.15;
  pointer-events: none;
  animation: btn-ripple 400ms var(--easing-out) forwards;
}
```

> game 变体的涟漪与 3D 按压同时触发，涟漪从按压点扩散，按压回弹 150ms 先于涟漪消失 400ms，体感连贯。

## 阴影层级规范

3D 按钮（game/destructive/success）的底部阴影应保持克制，避免与外发光阴影叠加导致视觉割裂：

| 变体 | 底部阴影 | 外发光 | 总计阴影层数 |
|------|---------|--------|------------|
| game | `0 4px 0 0 brand-700` | 无（纯色底部阴影即可） | 1 层 |
| primary | 无底部阴影 | `0 4px 14px -4px brand-ring` | 1 层 |
| destructive/success | `0 4px 0 0 色阶-700` | 无 | 1 层 |
| glass/secondary | 无底部阴影 | `inset 0 1px 0 0 glass-inset` | 1 层 |

> **关键原则**：每个按钮最多 1 层视觉阴影。底部 3D 阴影与外发光二选一，不叠加。hover 时阴影可微增（+1px 底部 + translateY(-1px)），但不新增阴影层。

## 反例

- 不使用纯实色填充（primary/glass 必须有 backdrop-filter 或渐变 + inset 高光）
- game 变体**始终使用胶囊圆角** `--radius-pill`，不降级为 `--radius-md`
- 移动端主 CTA 按钮高度不低于 48px
- 不叠加底部 3D 阴影 + 外发光阴影（视觉割裂）

## a11y 验收点

- [ ] `role="button"`（非 `<button>` 元素时）
- [ ] disabled 时 `aria-disabled="true"`
- [ ] loading 时 `aria-busy="true"` + spinner 有 `aria-label="加载中"`
- [ ] icon-only 按钮必须有 `aria-label`
- [ ] 颜色对比度 >=4.5:1（文字/背景）

---

## 99. 待确认问题

无

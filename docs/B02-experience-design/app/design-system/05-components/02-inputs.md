# 组件：Input / Textarea / Select / Combobox / DatePicker

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：用户文本输入、单值选择、日期选择
- 禁忌：多选用 Checkbox/Tag；开关用 Switch；富文本用专用编辑器

---

## Input

### 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| default | 标准单行输入 | 用户名、邮箱 |
| password | 带显示/隐藏切换 | 密码输入 |
| search | 左侧搜索图标 + 右侧清除按钮 | 全局搜索 |
| with-addon | 前缀/后缀文字或图标 | 手机号前的国家码 |

### 尺寸

| 尺寸 | 高度 | padding-x | 字号 |
|------|------|-----------|------|
| md（唯一） | 44px | 12px | `var(--text-base)` |

> 统一 44px，满足移动端触控目标。

### 材质

| 属性 | Light 模式 | Dark 模式 |
|------|-----------|-----------|
| 背景 | `rgba(255, 251, 240, 0.92)` (暖米白) | `rgba(20, 48, 79, 0.42)` (墨青半透) |
| 边框 | `var(--border-subtle)` = `1px solid var(--color-neutral-200)` | — |
| 圆角 | `var(--radius-md)` (12px) | — |
| 过渡 | `var(--motion-fast)` | — |

### 状态

| 状态 | 边框 | 背景 | 标签色 | 其他 |
|------|------|------|--------|------|
| 默认 | `var(--border-subtle)` | 暖米白半透 | `var(--color-neutral-500)` | — |
| hover | `1px solid var(--color-neutral-300)` | — | — | — |
| focus | `var(--focus-ring)` (`0 0 0 4px var(--color-brand-ring)`) | — | `var(--color-brand-default)` | 标签高亮 |
| active | 同 focus | — | — | — |
| disabled | `1px solid var(--color-neutral-200)` | `var(--color-neutral-50)` | `var(--color-neutral-400)` | `cursor: not-allowed` |
| loading | 同默认 | — | — | 右侧 spinner |
| error | `1px solid var(--color-danger-500)` | — | `var(--color-danger-500)` | `box-shadow: 0 0 0 4px var(--color-danger-50)` |
| readonly | 无边框 | `var(--color-neutral-50)` | `var(--color-neutral-500)` | `cursor: default` |

### Anatomy

```
[Label]  ← var(--font-display), var(--text-sm), letter-spacing: 1px
┌──────────────────────────────┐
│ [prefix?] [input] [suffix?]  │  ← 暖米白半透背景 + 毛玻璃边框
└──────────────────────────────┘
[helper text / error message]
```

- Label 位于输入框上方，间距 `var(--space-2)` (8px)
- Label 使用 `var(--font-display)`，`letter-spacing: 1px`
- Helper text / error 位于输入框下方，字号 `var(--text-xs)`，间距 `var(--space-1)`
- Error message 颜色 `var(--color-danger-500)`

---

## Textarea

继承 Input 所有状态和样式，差异：

| 属性 | 值 |
|------|-----|
| 最小高度 | 88px（2 行） |
| resize | vertical |
| 最大高度 | 200px（超出滚动） |
| 字符计数 | 右下角显示 `当前/最大`，`var(--text-xs)` |

---

## Select

### 变体

| 变体 | 说明 |
|------|------|
| default | 单选下拉 |
| native | 移动端使用原生 select（更好的滚轮体验） |

### 状态

继承 Input 状态，额外：

| 状态 | 表现 |
|------|------|
| 展开 | 下拉面板显示，箭头旋转 180deg |
| 选中 | 选中项左侧 check 图标，`var(--color-brand-default)` |
| 无选项 | 面板内显示"暂无选项" |

### 下拉面板

| 属性 | 值 |
|------|-----|
| 材质 | `.glass-strong` — `background: var(--glass-2); backdrop-filter: var(--glass-blur-lg)` |
| 边框 | `var(--glass-border-strong)` |
| 最大高度 | 240px（可滚动） |
| 圆角 | `var(--radius-lg)` |
| 阴影 | `var(--glass-shadow-lg)` |
| 选项高度 | 40px |
| 选项 hover | `var(--glass-3)` |
| z-index | `var(--z-dropdown)` |

---

## Combobox

继承 Select，额外支持：

| 功能 | 说明 |
|------|------|
| 搜索过滤 | 输入框内可键入，实时过滤选项 |
| 高亮匹配 | 匹配文字加粗或高亮 `var(--color-brand-50)` |
| 创建新项 | 可选，底部显示"创建 XXX" |
| 键盘导航 | 上下键移动高亮，Enter 选中，Esc 关闭 |

---

## DatePicker

### 变体

| 变体 | 说明 |
|------|------|
| single | 单日期 |
| range | 日期范围 |

### 日历面板

| 属性 | 值 |
|------|-----|
| 材质 | `.glass-strong` — 毛玻璃面板 |
| 单元格尺寸 | 36px x 36px |
| 今日标记 | 底部圆点，`var(--color-brand-default)` |
| 选中日 | 圆形背景 `var(--color-brand-default)`，文字 `var(--color-brand-on)` |
| 范围中间 | `var(--color-brand-50)` 背景 |
| 禁用日 | `var(--color-neutral-300)` 文字 |
| 月份切换 | 左右箭头，动画 `var(--motion-base)` |

---

## 行为（键盘+屏幕阅读器）

| 组件 | 键盘 | aria |
|------|------|------|
| Input | Tab 聚焦，Esc 清除（search 变体） | `aria-label` / `aria-describedby`(helper) |
| Textarea | Tab 聚焦，Shift+Enter 换行 | `aria-label` |
| Select | Enter/Space 展开，上下选择，Enter 确认 | `role="listbox"`，`aria-expanded` |
| Combobox | 同 Select + 键入过滤 | `role="combobox"`，`aria-autocomplete` |
| DatePicker | 方向键在日历内移动 | `role="dialog"`，`aria-label` |

---

## 99. 待确认问题

无

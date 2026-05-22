# 组件：Input / Textarea / Select / Combobox / DatePicker

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
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
| 背景 | `var(--glass-bg)` — 毛玻璃白半透 | `var(--glass-bg)` — 毛玻璃暗半透 |
| 模糊 | `backdrop-filter: blur(12px) saturate(1.4)` | 同左 |
| 边框 | `1px solid var(--glass-border)` | 同左 |
| 内层高光 | `inset 0 1px 0 0 var(--glass-inset)` | 同左 |
| 圆角 | `var(--radius-md)` 12px | 同左 |
| 过渡 | `var(--transition-all)` | 同左 |

### 状态

| 状态 | 边框 | 背景 | 其他 |
|------|------|------|------|
| 默认 | `var(--glass-border)` | `var(--glass-bg)` | inset 高光 |
| hover | `var(--color-neutral-300)` | `var(--glass-bg-card)` | — |
| focus | `var(--color-brand-default)` | `var(--glass-bg-card)` | `0 0 0 4px var(--input-focus-glow)` 品牌色发光光晕 |
| error | `var(--color-danger-500)` | 同默认 | `0 0 0 4px rgba(239,68,68,0.15)` |
| disabled | `var(--glass-border)` | `var(--color-neutral-100)` | `opacity: 0.5; cursor: not-allowed` |
| readonly | transparent | `var(--color-neutral-50)` | `cursor: default` |

### Anatomy

```
[Label]  ← var(--font-sans), var(--text-sm), var(--weight-medium)
┌──────────────────────────────┐
│ [prefix?] [input] [suffix?]  │  ← 毛玻璃白半透背景 + 玻璃边框 + inset 高光
└──────────────────────────────┘
[helper text / error message]
```

- Label 位于输入框上方，间距 `var(--space-1)` (4px)
- Helper text / error 位于输入框下方，字号 `var(--text-xs)`
- Error message 颜色 `var(--color-danger-500)`

---

## Textarea

继承 Input 所有材质和状态，差异：

| 属性 | 值 |
|------|-----|
| 最小高度 | 88px（2 行） |
| padding | `var(--space-3)` |
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
| 材质 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` |
| 边框 | `1px solid var(--glass-border)` |
| 内层高光 | `inset 0 1px 0 0 var(--glass-inset)` |
| 最大高度 | 240px（可滚动） |
| 圆角 | `var(--radius-lg)` |
| 阴影 | `0 8px 40px -4px var(--glass-shadow-elevated)` |
| 选项高度 | 40px |
| 选项 hover | `var(--glass-bg-card)` |
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
| 材质 | `var(--glass-bg-elevated)` + `backdrop-filter: var(--glass-blur-lg)` |
| 边框 | `1px solid var(--glass-border)` |
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

<!-- TARGET-PATH: docs/B02-experience-design/design-system/05-components/08-popovers-tooltips.md -->

# 05.08 · 气泡 / 工具提示

> Radix Primitives `Popover` / `Tooltip` 包装,主题层叠加 `glass-panel`。

## 一、Tooltip
| 属性 | 值 |
| ---- | ---- |
| 触发 | hover 600ms 延迟 / focus 立即 |
| 容器 | `--bg-elevated` + `--border-subtle` + `radius-sm` + `shadow-sm` |
| 字号 | `text-caption` |
| 最大宽度 | 240px;超长自动换行 |
| 位置 | 默认 `top`,自动翻转避免溢出 |
| 箭头 | 8px 三角,跟随主体色 |
| 动效 | 透明度 + 4px 位移,`--motion-fast` |

## 二、Popover
| 属性 | 值 |
| ---- | ---- |
| 触发 | click |
| 容器 | `glass-panel`(`--glass-blur-md`) + `radius-md` + `shadow-md` |
| 内边距 | 16px |
| 最大宽度 | 360px |
| 关闭 | 点击外部 / ESC / 内部 close trigger |
| 箭头 | 可选,默认关闭(简化视觉) |

## 三、可访问性
- Tooltip 走 `aria-describedby`,**禁止承载交互**(只读信息)。
- Popover 走 `aria-haspopup` + focus 管理;弹层内 Tab 顺序闭环。

## Anatomy（结构组成）
- Tooltip：纯文字提示，hover/focus 触发，自动避让，箭头 8px。
- Popover：click 触发的交互弹层，`glass-panel` 容器，可承载按钮 / 表单 / 列表；外部点击或 ESC 关闭。

## 反例（禁止形态）
- 把交互内容放进 Tooltip（鼠标移开即消失，无法操作）。
- Popover 内嵌套另一个 Popover（焦点管理失控）。
- Popover 内放完整表单（应改 Modal/Drawer）。
- Tooltip 文案超过 240px 不换行（溢出）。
- 移动端依赖 hover 触发 Tooltip（无 hover 事件）。

## 可访问性（a11y 强化）
- Tooltip：`aria-describedby` 指向 tooltip 内容 id；触发元素必须可 focus（键盘可达）。
- Popover：`aria-haspopup="dialog"` + `aria-expanded`；打开后焦点进入弹层第一个可交互元素，关闭返回触发元素。
- 弹层内 Tab 顺序闭环；ESC 关闭。

## 空态
- 不适用（Tooltip/Popover 不应承载空数据列表；若 Popover 内列表为空，使用紧凑型 `EmptyState`，留白减半）。

## 错误态
- 不适用（错误反馈走 Toast / 内联）。Popover 内异步请求失败时，弹层内插入 1 行 `error.popover.fail` + “重试” 文字按钮，**不关闭弹层**。


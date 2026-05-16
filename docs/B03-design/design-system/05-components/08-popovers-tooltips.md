<!-- TARGET-PATH: docs/B03-design/design-system/05-components/08-popovers-tooltips.md -->

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

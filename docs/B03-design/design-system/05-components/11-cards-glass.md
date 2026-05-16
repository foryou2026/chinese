<!-- TARGET-PATH: docs/B03-design/design-system/05-components/11-cards-glass.md -->

# 05.11 · 卡片 / 玻璃拟态基类

> ui-kit 导出:`GlassCard` / `glass-panel` / `glass-button` / `glass-modal` / `glass-toast` CSS 工具类。
> Token 详见 [01-tokens.md §四 玻璃拟态](../01-tokens.md)。

## 一、`GlassCard`(业务卡片基类)
| 属性 | 值 |
| ---- | ---- |
| 背景 | `var(--glass-bg)`(半透明)+ `backdrop-filter: blur(var(--glass-blur-md))` |
| 边框 | 1px `--border-subtle` |
| 圆角 | `radius-md`(默认)/ `radius-lg`(大卡片) |
| 阴影 | `shadow-sm`(默认)/ `shadow-md`(hover 提升) |
| 内边距 | 16px(紧凑)/ 24px(标准)/ 32px(大尺寸) |

## 二、毛玻璃工具类清单
| 类名 | 模糊强度 | 使用场景 |
| ---- | ---- | ---- |
| `glass-button` | `--glass-blur-sm` | 按钮 / 输入框 / Tab |
| `glass-panel` | `--glass-blur-md` | 弹层 / Popover / Select 弹出 |
| `glass-modal` | `--glass-blur-lg` | Modal / Drawer |
| `glass-toast` | `--glass-blur-md` + `shadow-md` | Toast |

## 三、降级
- 浏览器不支持 `backdrop-filter`:回退为 `--bg-elevated` 实色 + 同边框 + 同阴影,不破坏布局。
- 暗黑模式:`--glass-bg` 自动翻转至深色半透明值(详见 [07-responsive-dark.md](../07-responsive-dark.md))。

## 四、性能
- 同屏 `backdrop-filter` 节点数应 ≤ 12 个(超出可能触发降级);列表场景禁止每行单独毛玻璃。
- 滚动容器禁止套毛玻璃(浏览器渲染昂贵);改为静态背景。

<!-- TARGET-PATH: docs/B02-experience-design/design-system/05-components/11-cards-glass.md -->

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

## Anatomy（结构组成）
- `GlassCard`：毛玻璃背景 + 1px `--border-subtle` + 圆角 + 阴影 + 16/24/32 内边距三档。
- 内部结构：可选 Header（标题 + 操作）→ Body → 可选 Footer（按钮区）。
- 毛玻璃工具类 `glass-*` 仅作 CSS 修饰类，**不**自带语义。

## 反例（禁止形态）
- 在长列表每行单独套 `GlassCard`（同屏 `backdrop-filter` 节点 > 12 触发降级）。
- 滚动容器套毛玻璃（性能差）。
- `GlassCard` 嵌套 `GlassCard`（视觉糊成一团）。
- 直接给 `GlassCard` 加 `cursor: pointer` 而无 `<a>` / `<button>` 子元素（无键盘可达性）。
- 卡片内文字颜色硬编码 `#fff`（应使用 token，否则暗模式不可读）。

## 可访问性（a11y 强化）
- 卡片若可点击，必须是 `<a>` 或 `<button>` 包裹，`focus-visible` 显示 2px `--ring`。
- 卡片标题应有真实 `<hN>` 级别，便于屏幕阅读器跳读。
- 暗模式下 `--glass-bg` 自动翻转，不要在组件内写 `dark:` 分支。

## 空态
- 卡片若用作单条数据展示，无数据时整卡替换为 `EmptyState`（紧凑变体）。

## 错误态
- 加载失败：卡片内容区替换为 `ErrorState` + “重试”，卡片外壳保留。


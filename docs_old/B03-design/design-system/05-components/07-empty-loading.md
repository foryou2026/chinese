<!-- TARGET-PATH: docs/B03-design/design-system/05-components/07-empty-loading.md -->

# 05.07 · 空状态 / 加载 / Spinner

> 上游:[`04-status-colors.md §三.1 / §三.2`](../04-status-colors.md) + [`06-interactions.md`](../06-interactions.md)。
> ui-kit 导出:`EmptyState` + `Skeleton`。

## 一、空状态 `EmptyState`
| 元素 | 规则 |
| ---- | ---- |
| 插画 | 48×48,居中 |
| 主文案 | `text-base` / 500 / `--text-primary`;i18n key `empty.<scene>.title` |
| 辅助文案 | `text-caption` / `--text-secondary`(可选) |
| 主操作 | `primary` 按钮(可选,例:"新建") |
| 留白 | 纵向 `space-6`(24px) |

## 二、加载骨架 `Skeleton`
| 场景 | 形态 |
| ---- | ---- |
| 表格 | 行数 = `pageSize`,每行 4 矩形条按列宽分布,高度 = 表格行高 |
| 卡片 | 圆角矩形(`radius-md`),高度 = 卡片预期高度 |
| 文本块 | 3 条水平矩形,宽度递减 100% / 80% / 60% |

骨架动画:`shimmer`,`--motion-slow` 循环。

## 三、Spinner
- 尺寸:14 / 20 / 32;按钮内 14,模态内 20,全页 32。
- 颜色:跟随父级文字色或 `--brand`(全页 loading)。
- 全页 loading:遮罩 `--bg-overlay` 70% 透明 + 居中 32 Spinner + 文案 `loading.global`。

## 四、禁止
- 禁止使用 GIF / 第三方 Lottie loading(性能 + 风格统一)。
- 禁止"白屏 + Spinner"超过 1s 不出骨架;> 1s 必须切骨架屏。

## Anatomy（结构组成）
- `EmptyState`：48×48 插画 + 主文案 + 辅助文案（可选）+ 主操作（可选），纵向 `space-6` 居中。
- `Skeleton`：按目标形态（表格行 / 卡片 / 文本块）占位，`shimmer` 动效。
- `Spinner`：14 / 20 / 32 三档，颜色跟随父级或 `--brand`。

## 反例（禁止形态）
- 用纯文本 “暂无数据” 代替 `EmptyState`（缺少视觉锚点）。
- 白屏 + Spinner 超过 1s（应切骨架屏）。
- 使用 GIF / Lottie loading（性能差、风格不统一）。
- 在空态描述里写技术错误（应区分“无数据”与“加载失败”两种态）。

## 可访问性（a11y 强化）
- `EmptyState` 容器 `role="status"`；主文案可被屏幕阅读器朗读。
- Spinner 容器 `role="status"` + `aria-label="loading"`；同区域内容设 `aria-busy="true"`。
- `prefers-reduced-motion` 时关闭 shimmer 与 spinner 旋转，仅留静态占位。

## 空态
- 本组件本身即空态；提供 `scene` 维度的文案与插画映射，禁止业务方自实现。

## 错误态
- “加载失败” 是错误态，**不复用** `EmptyState`；提供独立 `ErrorState` 变体（图标 `alert-circle` `--danger` + 错误码 + “重试” 按钮）。


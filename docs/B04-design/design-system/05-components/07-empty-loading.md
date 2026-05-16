<!-- TARGET-PATH: docs/B04-design/design-system/05-components/07-empty-loading.md -->

# 05.07 · 空状态 / 加载 / Spinner

> 上游:[`grules/G2-视觉与交互风格/04-状态与组件.md §三.1 / §三.2`](../../../grules/G2-视觉与交互风格/04-状态与组件.md) + [`05-通用交互.md`](../06-interactions.md)。
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

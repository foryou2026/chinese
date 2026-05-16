<!-- TARGET-PATH: docs/B03-design/design-system/05-components/10-tabs-accordion.md -->

# 05.10 · Tab / 折叠

> ui-kit 导出:`GlassTabs` / `Accordion`(基于 Radix)。

## 一、Tab `GlassTabs`
| 属性 | 值 |
| ---- | ---- |
| 容器 | `glass-panel` 底 + 横向排布 |
| 高度 | 桌面 40px / 移动 44px |
| 选中态 | 文字 `--brand` + 底部 2px `--brand` 下划线 + 1.5x 字重 |
| 未选中 | 文字 `--text-secondary` |
| hover | `--bg-hover` |
| 间距 | tab 之间 24px;首尾 padding 16px |
| 切换动效 | 下划线滑动,`--motion-base` |

### 变体
- `pills`:无下划线,选中态为 `--brand-soft` 底 + `--brand` 字 + `radius-pill`。
- `vertical`:左侧导航形态;选中态为左侧 2px `--brand` 竖线 + `--bg-active` 底。

## 二、折叠 `Accordion`
| 属性 | 值 |
| ---- | ---- |
| 容器 | `<GlassCard>` 包裹 |
| 行高(收起态) | 56px |
| 展开动效 | 高度 0 → auto,`--motion-base` |
| 图标 | 右侧 `chevron-down` 16px,展开时旋转 180° |
| 多开 | 默认允许多 panel 同时展开;可通过 `singleOpen` prop 限单开 |
| 分隔 | panel 间 1px `--border-subtle` |

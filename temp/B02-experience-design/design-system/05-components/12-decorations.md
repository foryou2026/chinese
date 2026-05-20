<!-- TARGET-PATH: docs/B02-experience-design/design-system/05-components/12-decorations.md -->

# 05.12 · 装饰元素

> 非交互装饰组件,纯 CSS / SVG 实现,无 ui-kit 导出(内联使用)。

## 一、分隔线 Divider
| 类型 | 视觉 | 用法 |
| ---- | ---- | ---- |
| 水平分隔 | 1px `--border-subtle` 实线 | 卡片内分组 / 列表分行 |
| 垂直分隔 | 1px × 行高 `--border-subtle` | 顶栏 inline 操作组之间 |
| 带文字分隔 | 中间留 16px 间距插入文字 `text-caption` / `--text-tertiary` | 表单分组标题 / "或者继续使用" |

## 二、品牌光晕 Glow
- 装饰用径向渐变光晕,色 `color-mix(in oklab, var(--brand) 30%, transparent)`;
- 半径 240px;位置:登录页右上角 / 个人中心头像背景。
- 性能:同屏最多 2 处;移动端默认关闭(`@media (max-width: 768px) { display: none }`)。

## 三、底纹 Pattern
- 极淡网格/点阵作为大区块底纹,opacity ≤ 0.04;颜色 `currentColor`。
- 使用场景:空状态背景 / 引导页 / 落地页。

## 四、图标
- 图标库统一使用 [lucide-react](https://lucide.dev),线宽 1.5,默认尺寸 16 / 20 / 24。
- 详情见 [99-extension-icons-imagery.md](../99-extension-icons-imagery.md)(非规范扩展)。

## 五、约束
- 装饰元素**禁止**承载任何交互(无 click / hover 反馈)。
- 装饰元素**不进入** `tabindex`(无障碍隔离)。
- 装饰元素**禁止**使用品牌主色实色,只能用淡化版本(`*-soft` / 光晕)。

## Anatomy（结构组成）
- Divider：`<hr>` 或 `<div role="separator">`。
- Glow：`<div aria-hidden="true">` 配径向渐变。
- Pattern：`<div aria-hidden="true">` 配 SVG/CSS 底纹。
- Icon：`<svg aria-hidden="true">`，仅作视觉补充。

## 反例（禁止形态）
- 给装饰元素绑 onClick / 监听 hover 改变业务状态（违反“装饰不交互”约束）。
- 装饰元素使用品牌主色实色（应仅用 `*-soft` / 光晕淡化版本）。
- 同屏放置 > 2 处 Glow（性能 + 视觉污染）。
- 移动端不关闭 Glow（造成滚动卡顿）。
- 装饰元素带文字而无对应 `aria-label`（屏幕阅读器念出无意义内容）。

## 可访问性（a11y 强化）
- 所有装饰元素 `aria-hidden="true"`，不进入 `tabindex` 序列。
- Divider 若承载语义分组，使用 `<hr>` 或 `role="separator"` 配 `aria-orientation`。
- 与文字组合的装饰，确保对比度仍满足 WCAG AA。

## 空态
- 不适用（装饰无数据态）。

## 错误态
- 不适用（装饰无错误态）。


<!-- TARGET-PATH: docs/B04-design/design-system/05-components/03-tables.md -->

# 05.03 · 表格 Tables

> 上游:[`grules/G2-视觉与交互风格/04-状态与组件.md §三`](../../../grules/G2-视觉与交互风格/04-状态与组件.md)。

## 一、容器与样式
| 属性 | 值 |
| ---- | ---- |
| 容器 | `<GlassCard>` 包裹,圆角 `radius-md` |
| 表头背景 | `transparent`(毛玻璃透出底色);文字 `text-caption` / 600 / `--text-secondary` |
| 行高 | 桌面 48px / 移动 56px |
| 斑马纹 | **禁用**(与毛玻璃叠加易脏) |
| hover 行 | `--bg-hover` |
| 选中行 | `--brand-soft` 底 + 文字 `--text-primary` |
| 边框 | 行间 1px `--border-subtle`;外层 `<GlassCard>` 自带边框 |
| 操作列 | 固定右侧;按钮间距 8px;均用 `ghost` 文字按钮 |
| 排序图标 | `chevrons-up-down` 12px;激活后 `chevron-up/down` + `--brand` |

## 二、空状态(详见 [07-empty-loading.md](07-empty-loading.md))
行内插画(48×48)+ 文字"暂无数据"(`text-secondary`)+ 可选 `New` 主按钮,居中,纵向 `space-6` 留白。

## 三、加载
骨架屏行数 = 当前 `pageSize`;每行 = 表格行高;4 个矩形条占位(按列宽分布)。

## 四、大数据量
**行数 > 100 必须** 启用 [TanStack Virtual](https://tanstack.com/virtual) 虚拟滚动;表头 `sticky`。

## 五、可访问性
- `<th scope="col">` + `aria-sort`,排序状态同步给屏幕阅读器。
- 行选择列 checkbox 必须 `aria-label`。

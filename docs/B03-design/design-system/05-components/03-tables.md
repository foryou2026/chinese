<!-- TARGET-PATH: docs/B03-design/design-system/05-components/03-tables.md -->

# 05.03 · 表格 Tables

> 上游:[`04-status-colors.md §三`](../04-status-colors.md)。

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

## Anatomy（结构组成）
- 容器：`<GlassCard>` → `<table>`。
- 表头：`<thead>` 一行 `<th scope="col">`；含排序图标的列可点击。
- 表体：`<tbody>` 行 `<tr>`，单元 `<td>`；hover 行 `--bg-hover`。
- 操作列：固定右侧，`ghost` 文字按钮组。
- 表尾：分页器（详见 [`06-interactions.md §5`](../06-interactions.md)）。

## 反例（禁止形态）
- 用 `<div>` 网格模拟表格（屏幕阅读器不识别）。
- 启用斑马纹（与毛玻璃叠加产生脏底）。
- 行 hover 时整行变色 + 鼠标指针不改 `cursor: pointer`（误导可点）。
- 跨页选中（容易丢失上下文）。
- 操作列写图标不带 `aria-label`。

## 可访问性（a11y 强化）
- `<th scope="col">` + `aria-sort="ascending|descending|none"` 与排序状态同步。
- 行选择 checkbox 必须 `aria-label`（例：“选择行：{rowKey}”）。
- 行可键盘聚焦（`tabindex=0`）；操作列按钮 Tab 顺序紧随其后。
- 表头 `sticky` 时背景不可透明，避免文字与表体重叠不可读。

## 空态
- 空数据：`<EmptyState>`，48×48 插画 + i18n `empty.{scene}.title` + 可选 `New` 主按钮。
- 已加载完成但筛选无结果：显示 “未找到匹配项” + “清空筛选” 文字按钮。

## 错误态
- 加载错误：表体替换为单元格通栏文案 `error.list.fail` + “重试”文字按钮；表头保留。
- 行级操作错误走 Toast（5xx）或行内 inline（4xx，例：删除冲突）。


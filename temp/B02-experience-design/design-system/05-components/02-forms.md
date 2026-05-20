<!-- TARGET-PATH: docs/B02-experience-design/design-system/05-components/02-forms.md -->

# 05.02 · 表单 Forms

> 上游:[`04-status-colors.md §四`](../04-status-colors.md)。

## 一、布局
| 属性 | 值 |
| ---- | ---- |
| 标签位置 | 桌面 / 移动均**上方** |
| 标签字号 / 字重 | `text-caption` / 500 |
| 字段间距 | `space-4`(16px) |
| 必填标记 | 标签后 4px 处,红色 `*`,色 `--brand` |

## 二、输入框
| 属性 | 值 |
| ---- | ---- |
| 高度 | 36px(默认)/ 32px(紧凑)/ 44px(移动) |
| 背景 | `glass-button` 风格(半透明 + `--glass-blur-sm`) |
| 边框 | `--border-strong` 1px;focus → 2px ring `--ring` |
| 圆角 | `radius-sm` |

## 三、提示文案
| 类型 | 颜色 | 字号 | 位置 |
| ---- | ---- | ---- | ---- |
| 错误提示 | `--danger` | `text-caption` | 字段下方 4px,与标签同列对齐 |
| 字数限制 | `text-tertiary` / 超限 `--danger` | `text-caption` | 字段右下角 |
| 帮助文案 | `text-tertiary` | `text-caption` | 字段下方 4px,**与错误提示互斥** |

## 四、复合控件
- Select / Combobox / DatePicker 弹层一律毛玻璃面板(`glass-panel`)。
- 表单按钮区:右下角,主按钮在右、取消按钮在左(与弹窗一致)。

## 五、校验时机
- `onBlur` 单字段校验 + 提交时全量校验;Schema 来源 [`packages/shared-schemas`](../../../system/packages/shared-schemas/)。
- 错误提示文案 i18n key 与字段同 namespace。

## Anatomy（结构组成）
- 容器：`<form>` / `<fieldset>` 分组。
- 字段单元：`<label>`（必填带 `*`）+ 控件 + 提示/错误 + 帮助文案（与错误互斥）。
- 控件：`<input>` / `<textarea>` / `<select>` / Combobox / DatePicker；统一 `glass-button` 风格。
- 提交区：右下角，主按钮在右，取消在左。

## 反例（禁止形态）
- 标签放控件内部 placeholder 代替 label（聚焦后丢失上下文）。
- 用 `red` 文字提示错误但不绑定 `aria-describedby`。
- 字段错误同时弹 Toast（违反“可恢复 4xx 内联”原则）。
- 必填仅靠红 `*` 而无 `required` 属性。
- 把错误文案做成图标 hover 提示（屏幕阅读器无法读取）。

## 可访问性（a11y 强化）
- `<label for="id">` 一一绑定，或用 `aria-labelledby`。
- 错误文案容器 `id` 通过 `aria-describedby` 绑定到控件，并 `aria-invalid="true"`。
- 必填字段加 `required` 属性，红 `*` 仅作视觉补充。
- 键盘 Tab 顺序必须与视觉顺序一致；提交按钮在最后。
- 错误聚焦：提交校验失败时自动聚焦第一个错误字段。

## 空态
- 空表单态：复合表单（如批量录入）允许 0 行；空时显示 `EmptyState`（详见 [07-empty-loading.md](07-empty-loading.md)）+ “新增一行”按钮。

## 错误态
- 字段级错误：字段下方 4px `--danger` 文案，与帮助文案互斥。
- 表单级错误（5xx / 网络）：表单顶部不嵌横幅，而是右上 Toast；提交按钮恢复可点击。
- 离开保护见 [`06-interactions.md §4`](../06-interactions.md)。


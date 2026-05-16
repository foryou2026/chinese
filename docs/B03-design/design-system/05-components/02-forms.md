<!-- TARGET-PATH: docs/B03-design/design-system/05-components/02-forms.md -->

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

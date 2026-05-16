<!-- TARGET-PATH: docs/B03-design/design-system/05-components/04-modals.md -->

# 05.04 · 弹窗 Modal

> 上游:[`04-status-colors.md §五`](../04-status-colors.md)。
> ui-kit 导出:`GlassModal`。

## 一、尺寸
| 类型 | 宽度 |
| ---- | ---- |
| 默认 | 480px |
| 大弹窗 | 720px |
| 全屏(< 640px) | 宽度 = `100vw - 16px`,高度 = `90vh`,从底部弹起 |

## 二、视觉
| 属性 | 值 |
| ---- | ---- |
| 遮罩层 | `--bg-overlay` |
| 容器 | `glass-modal`(高强度毛玻璃 + `radius-lg`) |
| 标题字号 / 字重 | `text-h3` / 600 |
| 内容区内边距 | 24px |
| 底部按钮对齐 | **右对齐**:取消(`secondary`)在左、确认(`primary`)在右 |

## 三、关闭方式
- 右上角 X 图标按钮 + ESC + 点遮罩。
- **危险弹窗禁用点遮罩关闭**(见 [06-toasts-alerts.md §确认弹窗](06-toasts-alerts.md))。

## 四、动效
- 进入:透明度 0→1 + 缩放 0.96→1,`--motion-slow`。
- 退出:逆向同步。

## 五、可访问性
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby` 指向标题。
- focus trap;关闭后焦点回到触发元素。

## Anatomy（结构组成）
- 遮罩 `--bg-overlay` → 容器 `glass-modal`。
- 容器：标题区（`text-h3` + X 按钮）→ 内容区（24px 内边距）→ 底部按钮区（右对齐：取消左 / 确认右）。
- focus trap 边界：进入聚焦第一个可交互元素，ESC 关闭。

## 反例（禁止形态）
- 用 Modal 承载长表单或可独立成页的复杂流程（应改成抽屉或独立页）。
- 多个 Modal 堆叠（应改为分步向导或拆流程）。
- 关闭按钮放底部（违反约定，关闭应在右上角 X）。
- 危险弹窗允许点遮罩关闭（应禁用）。
- 把成功提示做成 Modal（应用 Toast）。

## 可访问性（a11y 强化）
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby="<title-id>"`。
- focus trap：Tab/Shift+Tab 在 Modal 内闭环；关闭后焦点回到触发元素。
- ESC 关闭支持；`prefers-reduced-motion` 时关闭进出缩放动效。

## 空态
- Modal 内的列表若空，使用与 [07-empty-loading.md](07-empty-loading.md) 一致的 `EmptyState`，缩小留白至 `space-4`。

## 错误态
- Modal 内操作错误：内联在表单字段，不弹 Toast 遮挡 Modal；5xx 时关闭 Modal 后再 Toast。
- 加载失败：Modal 内容区替换为错误占位 + “重试”，标题与按钮区保留。


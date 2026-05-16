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

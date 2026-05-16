<!-- TARGET-PATH: docs/B03-design/design-system/05-components/06-toasts-alerts.md -->

# 05.06 · Toast / 确认弹窗

> 上游:[`04-status-colors.md §七 / §八`](../04-status-colors.md)。
> ui-kit 导出:`GlassToast`(全局单例)+ `Confirm`(危险确认)。

## 一、Toast
| 属性 | 值 |
| ---- | ---- |
| 位置 | **顶部居中**,距离顶栏底部 16px |
| 容器 | `glass-toast`(毛玻璃 + `radius-md` + `shadow-md`) |
| 进入动效 | 自顶向下 16px → 0,`--motion-base` |
| 同时上限 | 3 条,超出时最旧的提前消失 |
| 自动消失 | 成功 3s / 错误 5s / 警告 4s |

### 类型映射
| 类型 | 图标(左侧 16px) | 图标色 | 文字色 |
| ---- | ---- | ---- | ---- |
| 成功 | `check-circle` | `--success` | `--text-primary` |
| 错误 | `x-circle` | `--danger` | `--text-primary` |
| 警告 | `alert-triangle` | `--warning` | `--text-primary` |
| 信息 | `info` | `--text-secondary` | `--text-primary` |

关闭:右侧 X 图标按钮(鼠标悬停时显示)。

## 二、确认弹窗(危险操作)
| 属性 | 值 |
| ---- | ---- |
| 触发 | 删除 / 重置 / 不可撤销操作 |
| 容器 | `GlassModal`(默认 480px) |
| 标题 | "确认删除 / 确认重置 / 确认 XX"(i18n key `confirm.<op>.title`) |
| 内容 | "确定要 XX「{name}」吗?此操作不可撤销。"(i18n + 插值) |
| 标题左侧图标 | `alert-triangle` 20px `--danger` |
| 取消按钮 | `secondary` |
| 确认按钮 | **`danger`** |
| 关闭 | X + ESC(**禁用点遮罩**) |
| 二次确认(高危) | 需输入对象名称匹配后才能点击确认按钮;适用于"删除用户 / 删除课程"等 |

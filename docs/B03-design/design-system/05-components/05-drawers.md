<!-- TARGET-PATH: docs/B03-design/design-system/05-components/05-drawers.md -->

# 05.05 · 抽屉 Drawer

> 上游:[`04-status-colors.md §六`](../04-status-colors.md)。
> ui-kit 导出:`GlassDrawer`。

| 属性 | 值 |
| ---- | ---- |
| 默认宽度 | 桌面 480px / 移动 100% |
| 滑出方向 | **右侧** |
| 容器 | `glass-modal` 风格 |
| 遮罩层 | `--bg-overlay` |
| 关闭方式 | 右上角 X + ESC + 点遮罩 |
| 顶部 | 标题(`text-h3`)+ X 按钮,下方 1px `--border-subtle` |
| 底部 | 操作区固定底部:取消左、主按钮右;含 `safe-area-inset-bottom` |

## 移动端导航 Drawer
- 同样遵循以上规范;触发元素为 [03-navigation.md](../03-navigation.md) 顶栏的汉堡按钮。
- 滑出方向移动端可改为**左侧**(更符合用户习惯),但本项目默认仍走右侧以保持一致。

## Anatomy（结构组成）
- 遮罩 `--bg-overlay` → 容器 `glass-modal` 风格的 Drawer。
- 顶部：标题（`text-h3`）+ X 按钮，下方 1px `--border-subtle`。
- 中部：内容区，纵向滚动。
- 底部：操作区固定，安全区 `env(safe-area-inset-bottom)`，取消左 / 主按钮右。

## 反例（禁止形态）
- 用 Drawer 装单字段确认（应用 Modal 或 Toast 确认）。
- 同时打开多个 Drawer（应排队或合并）。
- 移动端 Drawer 不留 X 按钮（手势不通用，无法回退）。
- Drawer 高度跟随内容（应固定 100vh 避免抖动）。

## 可访问性（a11y 强化）
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby`。
- focus trap 同 Modal；关闭焦点回触发元素。
- 移动端务必能 ESC 关闭（外接键盘场景）。

## 空态
- Drawer 内列表空时，使用 `EmptyState`（与 [07-empty-loading.md](07-empty-loading.md) 一致），纵向 `space-4` 留白。

## 错误态
- Drawer 内表单错误：内联反馈；网络/服务异常显示顶部内嵌错误条（不与 Toast 叠加遮挡）。
- 加载失败：内容区替换错误占位 + “重试”按钮。


<!-- TARGET-PATH: docs/B04-design/design-system/05-components/05-drawers.md -->

# 05.05 · 抽屉 Drawer

> 上游:[`grules/G2-视觉与交互风格/04-状态与组件.md §六`](../../../grules/G2-视觉与交互风格/04-状态与组件.md)。
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

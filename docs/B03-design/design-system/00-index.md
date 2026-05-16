<!-- TARGET-PATH: docs/B03-design/design-system/00-index.md -->

# B04 · 设计系统（索引）

> **阶段**：B04-S 设计系统  
> **角色**：UX / 设计架构师  
> **feature**：全局  
> **上游依赖**：`B02-ux/01-direction.md`、`B02-ux/05-moodboard.md`、`B02-ux/06-experience-principles.md`、`_input/visual-input.md`  
> **冻结状态**：已冻结 · 2026-04-28  
> **下游影响**：`system/packages/ui-kit/`、所有 C04 H 原型、所有 C03 N 4 态文案承载组件、所有 D02 L 错误反馈位置  
> **关联**：本目录即设计系统当前唯一真相

---

## 0. 摘要

- 把 B03 定下的"感觉"转成可工程化的 token / 组件 / 交互规则。
- 唯一品牌色 = 红；全局毛玻璃；无侧边栏；全屏宽度；暗模式真黑。
- 所有数值（颜色、间距、动效曲线）的唯一来源 = `01-tokens.md`；代码不可硬编码。
- 设计原型代码骨架在 `B03-design/prototype-style/`，被 C04 第一次原型时填充。

---

## 1. 文件清单

| 序号 | 文件 | 职责 |
|------|------|------|
| _input | [`_input/visual-input.md`](./_input/visual-input.md) | PM 模拟视觉输入回写 |
| 00 | 00-index.md（本文件）| 索引 + 边界约定 |
| 01 | [01-tokens.md](./01-tokens.md) | 颜色 / 字体 / 间距 / 圆角 / 阴影 / 毛玻璃 / 动效全部 token |
| 02 | [02-layout.md](./02-layout.md) | 顶栏、远景层、内容区 .page、空状态、加载策略 |
| 03 | [03-navigation.md](./03-navigation.md) | 应用端 / 管理端菜单 + 头像下拉 + 角色守卫与菜单源 |
| 04 | [04-status-components.md](./04-status-components.md) | 状态色映射 + 按钮 / 表格 / 表单 / Modal / Drawer / Toast / 确认弹窗 + 组件库目录约定 |
| 05 | [05-interactions.md](./05-interactions.md) | 防重复提交 / 搜索 / 列表刷新 / 表单离开保护 / 分页 / 键盘 / 复制下载 / 错误反馈 / 动效 |
| 06 | [06-responsive-dark.md](./06-responsive-dark.md) | 6 断点 / 移动端细则 / 暗黑模式切换 / 毛玻璃降级 / 主题色自定义 |
| 07 | [07-icons-imagery.md](./07-icons-imagery.md) | 图标 / 插画 / 图片 / 头像 / 字符占位 |
| 99 | [99-open-questions.md](./99-open-questions.md) | 待 PM 拍板项（含图形 Logo 待定）|

---

## 2. 边界

- B04 **只**定义"长什么样 / 怎么响应"；不写业务规则、不定义 PRD 字段、不写接口。
- 凡数值（hex / px / ms / cubic-bezier）必须存在于 [01-tokens.md](./01-tokens.md)；本目录其他文件可援引但不可"另行定义"。
- 与 B03 关系：B03 给"感觉关键词"，B04 给"具体值与规则"。一句 B04 规则必须援引 B03 至少一个关键词作为依据。
- 本目录是设计系统的唯一真相。任何变更均需在 `A00-meta/changelog.md` 同步记录。

---

## 3. 工程落地约定

| 物 | 位置 |
|---|------|
| `tokens.css` + `tokens.ts` | `system/packages/ui-kit/src/tokens/` |
| 毛玻璃组件 | `system/packages/ui-kit/src/components/` （`GlassNav` / `GlassCard` / `GlassButton` / `GlassModal` / `GlassDrawer` / `GlassTabs` / `GlassToast` / `StatusTag` / `Skeleton` / `PageHeader` / `PageContent` / `EmptyState` / `Confirm`）|
| Tailwind 4 主题 | `system/packages/ui-kit/src/tokens/theme.css` 内 `@theme` 块 |
| 菜单数据源 | `system/packages/shared-config/src/menus.ts` |
| Storybook | `system/packages/ui-kit/.storybook/`（亮 / 暗双主题快照）|
| 视觉对比度 CI | `axe-core` 自动跑关键页面 |

---

## 4. 评审约定

- 任何 C 阶段 PR 都必须援引本目录至少 1 节作为依据；
- 任何"加新颜色 / 加新尺寸 / 加新组件"必须先开 B04 变更单（更新 token + Storybook 故事），后改业务代码；
- 同步更新 `docs/A00-meta/changelog.md`。

---

## 99. 待确认问题
- 图形版 Logo 形态（v1 暂用文字 + 色块）。详见 [99-open-questions.md](./99-open-questions.md)。

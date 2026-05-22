# admin 系统体验与设计系统 — 独立声明

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin
> **系统**：admin
> **模块**：全局
> **功能**：全局
> **冻结状态**：未冻结

---

## 独立声明

admin 系统与 app 系统采用**完全独立的设计系统**。

- admin 走 Feishu/Notion 风格的极简专业后台 UX + 克制毛玻璃（Minimal Ink + Frost）
- app 走 Duolingo 风格的游戏化学习 UX

两套系统不共享设计 Token、不共享原型样式包、不共享组件规范。

## 核心差异

| 维度 | app（用户学习系统） | admin（管理后台） |
|------|------------------|-----------------|
| 设计语言 | 游戏化闯关 + 高饱和毛玻璃 | 极简专业 + 克制毛玻璃 |
| 背景 | 渐变 mesh gradient + 高模糊毛玻璃 | 浅灰渐变底色 + 低饱和 Frost |
| 按钮风格 | 品牌渐变 + 弹跳动效 | 亮色纯黑按钮/暗色纯白按钮 |
| 导航 | 移动端 BottomBar / 桌面端 TopBar | SideBar(可折叠) + TopBar |
| 称呼 | "你" | "您" |
| emoji | 仅成功态允许 | 禁止 |
| 表格密度 | 标准 | 可选 compact |
| Breadcrumb | 不使用 | 使用 |
| 暗黑模式 | 默认 auto | 默认 light |
| 游戏化元素 | 有（XP/streak/徽章） | 无 |

## 文件路径

- 体验定调：`docs/B02-experience-design/admin/01-direction.md` ~ `06-experience-principles.md`
- 设计系统：`docs/B02-experience-design/admin/design-system/`
- 原型样式包：`docs/B02-experience-design/admin/prototype-style/`

---

## 99. 待确认问题

无

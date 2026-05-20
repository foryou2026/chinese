# admin 系统体验与设计系统 — 共享引用

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin
> **系统**：admin
> **模块**：全局
> **功能**：全局
> **上游依赖**：docs/B02-experience-design/app/
> **冻结状态**：未冻结

---

## 共享声明

admin 系统与 app 系统共用同一套设计风格和设计系统。

所有体验定调、Token、组件规范、原型样式包均以 `docs/B02-experience-design/app/` 为唯一源。

admin 不复制、不重复定义任何设计规范。

## 差异点

| 维度 | app | admin |
|------|-----|-------|
| 导航 | 移动端 BottomBar / 桌面端 TopBar | SideBar(可折叠) + TopBar |
| 称呼 | "你" | "您" |
| emoji | 仅成功态允许 | 禁止 |
| 表格密度 | 标准(48px行高) | 可选 compact(40px行高) |
| Breadcrumb | 不使用 | 使用 |
| 暗黑模式 | 默认 auto | 默认 light |
| 游戏化元素 | 有（XP/streak/徽章） | 无 |

## 引用路径

- 体验定调：`docs/B02-experience-design/app/01-direction.md` ~ `06-experience-principles.md`
- 设计系统：`docs/B02-experience-design/app/design-system/`
- 原型样式包：`docs/B02-experience-design/app/prototype-style/`

---

## 99. 待确认问题

无

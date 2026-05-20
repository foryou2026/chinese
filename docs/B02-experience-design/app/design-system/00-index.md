# 设计系统 · 索引

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app（admin 引用本目录）
> **冻结状态**：未冻结

---

| 序号 | 文件 | 职责 |
|------|------|------|
| 01 | tokens | 颜色/字体/间距/圆角/阴影/动效/毛玻璃 CSS 变量 |
| 02 | layout | 栅格、断点、容器（流体全宽） |
| 03 | navigation | TopBar/BottomBar/SideBar/Breadcrumb |
| 04 | status-colors | 4 状态色（翠玉/鎏金/朱砂/青花）+ 焦点环 + 禁用态 |
| 05 | components/ | 各组件规范（6 态+异常态） |
| 06 | interactions | 焦点/键盘/滚动/手势 |
| 07 | responsive-dark | 断点行为 + 暗黑映射 |

## 组件库底座

shadcn/ui + Tailwind CSS v4

## 三轴正交主题

| 轴 | 取值 | DOM 标记 |
|----|------|---------|
| 模式 | light / dark / auto | `<html data-mode="...">` |
| 主题色 | ink / cinnabar / jade / gold / graphite | `<html data-accent="...">` |
| 密度 | default / compact / elder | `<html data-density="...">` |

## 同源约束

`prototype-style/tokens.css` 与本目录 `01-tokens.md` 中的 CSS 变量逐字一致。

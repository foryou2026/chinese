# 设计系统 · 索引（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：无
> **冻结状态**：未冻结

---

| 序号 | 文件 | 职责 |
|------|------|------|
| 01 | tokens | 颜色/字体/间距/圆角/阴影/动效/毛玻璃 CSS 变量（Minimal Ink + Frost） |
| 02 | layout | 断点、容器、SideBar+TopBar 页面结构 |
| 03 | navigation | TopBar/SideBar/Breadcrumb/移动端抽屉导航 |
| 04 | status-colors | 4 状态色（翡翠/琥珀/红/蓝）+ 焦点环 + 禁用态 |
| 05 | components/ | 各组件规范（6 态+异常态） |
| 06 | interactions | 焦点/键盘/滚动 |
| 07 | responsive-dark | 断点行为 + 暗黑映射 + 密度切换 |

## 设计风格

**飞书/Notion 式专业管理后台 + 克制毛玻璃**——干净、克制、高效。与 app 端的高饱和极光毛玻璃做明确区分。

| 维度 | admin 管理后台 | app 用户端 |
|------|--------------|-----------|
| 表面语言 | 克制 Frost 毛玻璃（blur ≤ 28px, saturate ≤ 1.5） | 高饱和极光毛玻璃（blur 24px, saturate 1.8） |
| 页面底色 | #F3F4F6 + 微弱径向渐变 / 纯黑 #000000 | 微暖白（跟随 accent）/ 纯黑 #000000 |
| 主按钮 | 纯黑 #18181B / 纯白 #FAFAFA | 品牌色渐变 + 毛玻璃 |
| 卡片 | `--glass-bg-card` rgba(255,255,255,0.78) + blur | 毛玻璃 `.glass` |
| 圆角 | 较小（6/8/12/16px） | 较大（8/12/16/24/32px） |
| 信息密度 | 紧凑（表格行 40px，正文 14px） | 舒适（表格行 48px，正文 16px） |
| 主题色切换 | 无（固定中性灰调色板） | Google 四色 accent 切换（红/黄/蓝/绿） |
| 动效 | 简洁、即时、无弹簧 | 弹簧感 cubic-bezier |

## 组件库底座

shadcn/ui + Tailwind CSS v4

## 二轴正交主题

| 轴 | 取值 | DOM 标记 |
|----|------|---------|
| 模式 | light / dark | `<html data-mode="...">` |
| 密度 | default / compact | `<html data-density="...">` |

> admin 不支持 accent 切换——管理后台使用固定的中性灰调色板，主按钮黑白配色，链接/焦点色固定为 blue-500。

## 同源约束

admin 的 token 系统与 app 完全独立，不共享 CSS 变量文件。两套系统在各自的子应用内互不干扰。

---

## 99. 待确认问题

无

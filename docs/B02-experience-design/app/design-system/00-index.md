# 设计系统 · 索引

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **冻结状态**：未冻结

---

## 设计语言

**Duolingo 风格游戏化 + 毛玻璃增强**

核心理念：以关卡路径、XP 经验值、连续学习天数（Streak）、成就徽章等游戏化机制驱动用户学习动力，同时保留毛玻璃（Frosted Glass）作为唯一表面材质语言，赋予界面通透感与高级感。大圆角胶囊按钮搭配弹簧回弹动效，营造活泼愉悦的操作手感。

| 序号 | 文件 | 职责 |
|------|------|------|
| 01 | tokens | 颜色/字体/间距/圆角/阴影/动效/毛玻璃/游戏化专属 CSS 变量 |
| 02 | layout | 栅格、断点、容器（移动优先全宽）、Quest Path 布局 |
| 03 | navigation | TopBar(桌面)/BottomBar(移动) 双导航 |
| 04 | status-colors | 4 状态色（翡翠/琥珀/红/蓝）+ 焦点环 + 禁用态 |
| 05 | components/ | 各组件规范（6 态+异常态+游戏化变体） |
| 06 | interactions | 焦点/键盘/滚动/手势/弹簧动效/庆祝动画 |
| 07 | responsive-dark | 断点行为 + 暗黑映射 + 密度/主题切换 |

## 组件库底座

shadcn/ui + Tailwind CSS v4

## 三轴正交主题

| 轴 | 取值 | DOM 标记 |
|----|------|---------|
| 模式 | light / dark / auto | `<html data-mode="...">` |
| 主题色 | indigo / rose / emerald / amber / violet | `<html data-accent="...">` |
| 密度 | default / compact / elder | `<html data-density="...">` |

## 游戏化设计支柱

| 支柱 | 说明 |
|------|------|
| 关卡路径（Quest Path） | Duolingo/HelloChinese 式蜿蜒节点路径，每个节点代表一课或一组练习 |
| 经验值（XP） | 完成练习获取 XP，XP 驱动等级提升，琥珀色主视觉 |
| 连续天数（Streak） | 连续学习天数计数器，橙色火焰图标，断链有视觉惩罚 |
| 成就徽章（Achievements） | 里程碑解锁徽章，星星/奖杯/皇冠等图标 |
| 进度驱动 UI | 各处可见进度条、等级指示器、完成率 |
| 3D 按钮 | Duolingo 标志性底部阴影按钮，胶囊圆角 + 按下位移 |

## 同源约束

`prototype-style/tokens.css` 与本目录 `01-tokens.md` 中的 CSS 变量逐字一致。

# 组件：Tabs / Accordion / Stepper

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Tabs

### 用途与禁忌

- 用途：同一页面内切换不同视图/分类
- 禁忌：不用于导航跳转（用 Navigation）；不用于分步流程（用 Stepper）

### 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| underline | 底部 2px 指示线 | 页面级 Tab 切换 |
| pill | 胶囊背景色 | 筛选项切换、小型分类 |
| segment | 分段控制器（SegmentedControl） | 列表/卡片视图切换 |

### 尺寸

| 尺寸 | 高度 | 字号 | padding-x |
|------|------|------|-----------|
| sm | 36px | var(--text-sm) | 12px |
| md | 44px | var(--text-base) | 16px |

### 状态（underline 变体）

| 状态 | 文字 | 底线 | 背景 |
|------|------|------|------|
| 默认 | var(--color-text-secondary) | 无 | transparent |
| hover | var(--color-text-primary) | 无 | var(--color-neutral-50) |
| focus | — | — | 焦点环 |
| active（当前） | var(--color-primary-500) | 2px var(--color-primary-500) | transparent |
| disabled | var(--color-neutral-400) | 无 | transparent |

### 状态（pill 变体）

| 状态 | 文字 | 背景 |
|------|------|------|
| 默认 | var(--color-text-secondary) | transparent |
| hover | var(--color-text-primary) | var(--color-neutral-100) |
| active（当前） | white | var(--color-primary-500) |
| disabled | var(--color-neutral-400) | transparent |

### 行为

| 交互 | 行为 |
|------|------|
| 左右方向键 | 切换 Tab 焦点 |
| Enter/Space | 激活 Tab |
| 底线动画 | 滑动跟随，var(--motion-normal) var(--ease-default) |
| 移动端 | 可横向滚动，overflow-x: auto |
| 懒加载 | Tab 内容首次激活时加载 |

---

## Accordion

### 用途与禁忌

- 用途：折叠/展开内容区域，节省垂直空间
- 禁忌：不用于导航菜单（用 SideBar）

### 变体

| 变体 | 说明 |
|------|------|
| single | 同时仅展开一项 |
| multiple | 可同时展开多项 |

### 状态

| 状态 | 标题区背景 | 箭头 | 内容 |
|------|-----------|------|------|
| 默认（折叠） | transparent | 右箭头 → | 隐藏 |
| hover | var(--color-neutral-50) | — | — |
| focus | 焦点环 | — | — |
| active（展开） | transparent | 下箭头 ↓ | 显示 |
| disabled | transparent | var(--color-neutral-300) | — |

| 属性 | 值 |
|------|-----|
| 标题高度 | 48px |
| 标题 padding | 0 16px |
| 内容 padding | 16px |
| 分隔线 | 1px var(--color-border) |
| 展开动画 | height auto，var(--motion-normal) var(--ease-default) |
| 箭头旋转 | var(--motion-fast) |

---

## Stepper

### 用途与禁忌

- 用途：多步骤流程导航（注册、引导）
- 禁忌：不用于 >5 步流程（考虑拆分或简化）

### 变体

| 变体 | 说明 | 适用 |
|------|------|------|
| horizontal | 水平步骤条 | 桌面端 |
| vertical | 垂直步骤条 | 移动端 / 步骤多时 |
| minimal | 仅显示 "步骤 2/4" | 移动端空间受限 |

### 步骤状态

| 状态 | 圆圈 | 连接线 | 标签 |
|------|------|--------|------|
| 待完成 | 1px var(--color-border)，数字灰色 | var(--color-neutral-200) | var(--color-text-secondary) |
| 当前 | var(--color-primary-500) 填充，白色数字 | 左侧 var(--color-primary-500) | var(--color-text-primary), var(--font-semibold) |
| 已完成 | var(--color-primary-500) 填充，白色 check | var(--color-primary-500) | var(--color-text-primary) |
| 错误 | var(--color-error) 填充，白色 X | var(--color-error) | var(--color-error) |

| 属性 | 值 |
|------|-----|
| 圆圈直径 | 32px |
| 连接线高度 | 2px |
| 标签字号 | var(--text-sm) |

### a11y

- role="list" + role="listitem"
- 当前步骤 aria-current="step"
- 已完成步骤可点击回退

---

## 99. 待确认问题

无

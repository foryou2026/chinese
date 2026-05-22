# 组件：Tabs / Accordion / Stepper（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Tabs

### 变体

| 变体 | 说明 | 适用 |
|------|------|------|
| underline | 下划线指示器 | 页面级 tab 切换 |
| pill | 胶囊背景高亮 | 段内切换、筛选 |

### underline 样式

| 属性 | 值 |
|------|-----|
| tab 高度 | 40px |
| 字号 | `var(--text-sm)` |
| 默认文字 | `var(--text-secondary)` |
| 选中文字 | `var(--text-primary)` + `var(--weight-medium)` |
| 指示器 | 2px `var(--btn-primary-bg)` 底边，transition 200ms |
| hover | 文字 `var(--text-primary)` |
| 底边框 | 1px solid `var(--border-color)` |

### pill 样式

| 属性 | 值 |
|------|-----|
| 容器背景 | `var(--surface-primary)` |
| 容器圆角 | `var(--radius-md)` |
| pill 圆角 | `var(--radius-sm)` |
| 选中背景 | `var(--surface-page)` + `var(--shadow-sm)` |
| 选中文字 | `var(--text-primary)` + `var(--weight-medium)` |

---

## Accordion

| 属性 | 值 |
|------|-----|
| 头部高度 | 48px |
| 头部 padding | `0 var(--space-4)` |
| 字号 | `var(--text-sm)` |
| 字重 | `var(--weight-medium)` |
| 箭头 | 右侧 chevron，旋转 180° 表示展开 |
| 分隔线 | 1px solid `var(--border-color)` |
| 内容 padding | `var(--space-4)` |
| 展开动效 | height auto，200ms ease-out |

### 模式

- 默认：多个可同时展开
- exclusive：同时只展开一个

---

## Stepper

| 属性 | 值 |
|------|-----|
| 步骤圆点 | 28px |
| 连接线 | 2px 高 |
| 完成态 | `var(--color-success-500)` 背景 + ✓ |
| 当前态 | `var(--btn-primary-bg)` 背景 + 步骤号 |
| 待定态 | `var(--surface-hover)` 背景 + 灰色步骤号 |
| 步骤标签 | `var(--text-xs)` |

---

## 反例

- 不使用品牌色渐变指示器
- 不使用弹跳动效切换

## a11y 验收点

- [ ] Tabs: `role="tablist"` / `role="tab"` / `role="tabpanel"` + `aria-selected`
- [ ] Accordion: 触发器 `aria-expanded` + `aria-controls`
- [ ] 键盘：左右箭头切换 tab，Enter/Space 展开折叠面板

---

## 99. 待确认问题

无

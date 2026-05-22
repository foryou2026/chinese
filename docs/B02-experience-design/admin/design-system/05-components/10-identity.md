# 组件：Avatar / Badge / Tag（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## Avatar

### 尺寸

| 尺寸 | 宽高 | 字号 | 适用 |
|------|------|------|------|
| xs | 24px | 10px | 表格行内 |
| sm | 32px | 12px | 列表、评论 |
| md | 40px | 14px | 卡片、导航 |
| lg | 64px | 22px | 个人中心 |

### 材质

| 属性 | 值 |
|------|-----|
| 圆角 | `var(--radius-pill)` 圆形 |
| 占位背景 | `var(--color-neutral-200)` |
| 占位文字 | `var(--text-primary)` 首字母 |
| 图片 | `object-fit: cover` |

### 状态指示器

- 右下角小圆点
- 在线：`var(--color-success-500)` 绿
- 离线：`var(--color-neutral-300)` 灰
- 尺寸：Avatar 宽高的 25%

---

## Badge

| 变体 | 背景 | 文字 | 适用 |
|------|------|------|------|
| neutral | `var(--color-neutral-100)` | `var(--text-secondary)` | 默认 |
| success | `var(--color-success-50)` | `var(--color-success-700)` | 已通过、已上线 |
| warning | `var(--color-warning-50)` | `var(--color-warning-700)` | 待审核、警告 |
| danger | `var(--color-danger-50)` | `var(--color-danger-700)` | 已拒绝、异常 |
| info | `var(--color-info-50)` | `var(--color-info-700)` | 进行中、信息 |

| 属性 | 值 |
|------|-----|
| 高度 | 20px |
| padding-x | `var(--space-2)` |
| 字号 | `var(--text-xs)` |
| 字重 | `var(--weight-medium)` |
| 圆角 | `var(--radius-pill)` |

### 数字徽标

- 在图标/头像右上角
- 红色圆形：`var(--color-danger-500)` 背景 + 白字
- 最小 18px 圆形；> 99 显示 "99+"

---

## Tag

| 属性 | 值 |
|------|-----|
| 高度 | 24px |
| padding-x | `var(--space-2)` |
| 字号 | `var(--text-xs)` |
| 圆角 | `var(--radius-sm)` |
| 背景 | `var(--surface-primary)` |
| 边框 | 1px solid `var(--border-color)` |
| 可删除 | 右侧 × 按钮 |
| 可选中 | 选中态边框 `var(--btn-primary-bg)` |

---

## 反例

- Badge 不使用品牌色渐变
- Avatar 不使用毛玻璃边框

## a11y 验收点

- [ ] Avatar 有 `alt` 文本
- [ ] 数字徽标 `aria-label="n 条未读"`
- [ ] Tag 删除按钮 `aria-label="移除 xxx"`

---

## 99. 待确认问题

无

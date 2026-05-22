# 组件：Table（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：展示结构化数据列表，支持排序、筛选、分页
- 禁忌：卡片式内容列表不使用 table；移动端优先使用列表视图

---

## 结构

```
┌─ thead ───────────────────────────────────┐
│  [checkbox] [列标题 ↕] [列标题] ... [操作] │  ← 表头行
├─ tbody ───────────────────────────────────┤
│  [checkbox] [数据]    [数据]  ... [操作]   │  ← 数据行
│  [checkbox] [数据]    [数据]  ... [操作]   │
├─ tfoot ───────────────────────────────────┤
│  已选 n 项  [批量操作]     [分页器]        │  ← 底栏
└───────────────────────────────────────────┘
```

## 尺寸

| 密度 | 行高 | padding-y | 字号 |
|------|------|-----------|------|
| default | 48px | 12px | `var(--text-sm)` |
| compact | 40px | 8px | `var(--text-sm)` |

## 材质

| 属性 | 值 |
|------|-----|
| 背景 | `var(--surface-primary)` |
| 边框 | 1px solid `var(--border-color)` |
| 圆角 | `var(--radius-lg)` |
| 表头背景 | `var(--surface-hover)` |
| 表头字重 | `var(--weight-medium)` |
| 行 hover | `var(--surface-hover)` |
| 选中行 | `var(--color-accent-50)` |
| 斑马纹 | 可选，`var(--surface-primary)` 交替 `var(--surface-page)` |

## 排序

| 状态 | 图标 |
|------|------|
| 未排序 | ↕ 灰色 `var(--text-muted)` |
| 升序 | ↑ `var(--text-primary)` |
| 降序 | ↓ `var(--text-primary)` |

## 空态

- 居中展示空图标 + 文案 + 可选操作按钮
- 最小高度 200px

## 反例

- 不使用毛玻璃
- 不使用渐变背景
- 不使用圆角 pill 行

## a11y 验收点

- [ ] `<table>` + `<thead>` / `<tbody>` 语义标签
- [ ] 排序列 `aria-sort="ascending|descending|none"`
- [ ] 全选 checkbox `aria-label="全选"`
- [ ] 分页器键盘可操作

---

## 99. 待确认问题

无

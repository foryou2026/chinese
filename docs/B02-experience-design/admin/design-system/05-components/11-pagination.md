# 组件：Pagination / Breadcrumb（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Pagination

### 结构

```
[上一页]  1  2  3  ...  10  [下一页]   每页 [20 ▾] 条，共 193 条
```

### 样式

| 属性 | 值 |
|------|-----|
| 页码按钮 | 32px x 32px |
| 字号 | `var(--text-sm)` |
| 圆角 | `var(--radius-sm)` |
| 当前页背景 | `var(--btn-primary-bg)` |
| 当前页文字 | `var(--btn-primary-text)` |
| 默认页文字 | `var(--text-secondary)` |
| hover 背景 | `var(--surface-hover)` |
| disabled | `opacity: 0.50` |
| 间距 | `var(--space-1)` |

### 行为

- 总页数 > 7 时，用 `...` 省略
- 始终显示首页、末页、当前页及前后各 1 页
- 上一页/下一页在边界时 disabled

---

## Breadcrumb

### 结构

```
首页  /  用户管理  /  用户详情
```

### 样式

| 属性 | 值 |
|------|-----|
| 字号 | `var(--text-sm)` |
| 分隔符 | `/` 或 `>` |
| 链接色 | `var(--text-secondary)` |
| 链接 hover | `var(--text-primary)` |
| 当前页 | `var(--text-primary)` + `var(--weight-medium)` |
| 间距 | `var(--space-1)` |

### 行为

- 最后一项为当前页，不可点击
- 超过 4 级时折叠为 `首页 / ... / 父级 / 当前页`

---

## 反例

- Pagination 不使用品牌色渐变当前页
- Breadcrumb 不使用图标分隔符

## a11y 验收点

- [ ] Pagination: `<nav aria-label="分页">` 包裹
- [ ] 当前页 `aria-current="page"`
- [ ] Breadcrumb: `<nav aria-label="面包屑">` + `<ol>` 语义
- [ ] 键盘：Tab 聚焦各页码

---

## 99. 待确认问题

无

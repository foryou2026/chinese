# 组件：Table

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：展示结构化列表数据（admin 为主，app 少量使用如学习记录/排行榜）
- 禁忌：不用于展示非结构化内容（用 Card List）；移动端优先用卡片列表替代

## 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| default | 标准表格 | admin 用户列表、课程管理 |
| compact | 紧凑行高 40px | admin 日志列表 |
| striped | 斑马纹交替背景 | 长列表提升可读性 |

## 尺寸

| 属性 | default | compact |
|------|---------|---------|
| 行高 | 48px | 40px |
| 表头高度 | 44px | 40px |
| 单元格 padding | 12px 16px | 8px 12px |
| 字号 | var(--text-sm) | var(--text-sm) |

## 状态

| 状态 | 表现 |
|------|------|
| 默认 | 白色背景，底部 1px 分隔线 |
| hover（行） | var(--color-neutral-50) 背景 |
| focus（行） | 焦点环围绕整行 |
| active（行选中） | var(--color-primary-50) 背景 + 左侧 3px var(--color-primary-500) 指示器 |
| disabled（行） | opacity 0.5，pointer-events: none |
| loading | Skeleton 行（3-5 行占位） |
| empty | 空态组件居中（见 09-loading.md Empty） |
| error | Alert Banner 替代表格内容 |

## 表头

| 属性 | 值 |
|------|-----|
| 背景 | var(--color-neutral-50) |
| 字重 | var(--font-medium) |
| 颜色 | var(--color-text-secondary) |
| position | sticky top: 0（表头固定） |

## 排序

| 状态 | 图标 |
|------|------|
| 未排序 | 上下双箭头，var(--color-neutral-300) |
| 升序 | 上箭头，var(--color-primary-500) |
| 降序 | 下箭头，var(--color-primary-500) |

## 筛选

- 表头列筛选图标（漏斗），点击弹出 Popover
- 激活筛选时图标变为 var(--color-primary-500)
- 筛选器内支持 Input / Select / DatePicker

## 分页

见 11-pagination.md。表格底部嵌入分页组件。

## 响应式

| 断点 | 策略 |
|------|------|
| ≥lg | 标准表格 |
| md | 隐藏次要列，横向滚动 |
| <md | 卡片列表替代（每行数据一张卡片） |

## 行为

| 交互 | 行为 |
|------|------|
| 列排序 | 点击表头切换 无→升→降→无 |
| 行选择 | Checkbox 列（可选），Shift+Click 范围选 |
| 键盘 | Tab 移动焦点到行，Enter 展开/操作 |
| 拖拽排序 | 可选功能，左侧拖拽手柄 |

## a11y

- [ ] `role="table"` / `role="grid"`
- [ ] 表头 `scope="col"`
- [ ] 排序列 `aria-sort="ascending/descending/none"`
- [ ] 选中行 `aria-selected="true"`
- [ ] 空态提供描述文字

---

## 99. 待确认问题

无

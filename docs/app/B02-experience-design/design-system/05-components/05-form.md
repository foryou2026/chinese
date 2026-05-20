# 组件：Form

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md, 02-inputs.md, 03-selection.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：收集用户输入并提交（注册、设置、搜索条件）
- 禁忌：不用于纯展示信息（用 Description List）

## 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| standard | 垂直布局，标签在上 | 注册、个人设置 |
| inline | 水平布局，标签在左 | admin 筛选条件栏 |
| step | 分步表单，配合 Stepper | 引导式注册 |

## 布局

### standard

```
[Label]          ← var(--text-sm), var(--font-medium), var(--color-text-primary)
[Input]          ← 全宽
[helper/error]   ← var(--text-xs)
                 ← 字段间距 var(--space-4)
[Label]
[Input]
[helper/error]

[Submit Button]  ← 右对齐或全宽（移动端全宽）
```

### inline（admin）

```
[Label    ] [Input          ] [Label    ] [Input          ]
                                                    [查询] [重置]
```

- 标签宽度固定 80-120px
- 每行 2-3 个字段（桌面）

## 校验策略

| 时机 | 行为 |
|------|------|
| 实时（输入中） | 仅格式校验（如邮箱格式），400ms 防抖 |
| 失焦（blur） | 完整字段校验，立即显示错误 |
| 提交 | 全表单校验，滚动到第一个错误字段 |

## 错误显示

| 属性 | 值 |
|------|-----|
| 位置 | 字段下方，紧贴输入框 |
| 字号 | var(--text-xs) |
| 颜色 | var(--color-error) |
| 图标 | 可选，error 图标 16px |
| 输入框边框 | 2px var(--color-error) |
| 标签颜色 | var(--color-error) |

### 全局错误（非字段级）

- 表单顶部 Alert 组件（error 变体）
- 显示服务器返回的错误信息

## 状态

| 状态 | 表现 |
|------|------|
| 默认 | 所有字段可编辑 |
| hover | 各字段独立 hover |
| focus | 当前字段高亮 |
| active | 同 focus |
| disabled | 全表单灰化，提交按钮 disabled |
| loading（提交中） | 提交按钮 loading，所有字段 readonly |
| error（校验失败） | 错误字段标红 + 下方错误消息 |
| readonly | 所有字段 readonly 态 |

## 必填标记

- Label 后追加红色 `*`（var(--color-error)）
- 可选字段不加标记（默认理解为必填）
- 如果大多数字段可选，改为可选字段标注"（选填）"

## 行为

| 交互 | 行为 |
|------|------|
| Tab | 按字段顺序移动焦点 |
| Enter | 单行 Input 中触发提交；Textarea 中换行 |
| Esc | 关闭打开的下拉/日期面板 |
| 提交成功 | Toast 提示 + 根据场景重置或跳转 |
| 提交失败 | 滚动到第一个错误字段 + 聚焦 |

## a11y

- [ ] 每个 Input 必须关联 `<label>` 或 `aria-label`
- [ ] 错误消息通过 `aria-describedby` 关联到字段
- [ ] 必填字段 `aria-required="true"`
- [ ] 提交中 `aria-busy="true"` 在 form 元素上

---

## 99. 待确认问题

无

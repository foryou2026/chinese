# 状态色

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：01-tokens.md
> **冻结状态**：未冻结

---

## 4 状态色

| 状态 | 色值 | 浅色背景 | 用途 |
|------|------|---------|------|
| success | #10b981 | #d1fae5 | 操作成功、正确答案、在线状态 |
| warning | #f59e0b | #fef3c7 | 警告提示、即将过期、弱网 |
| error | #ef4444 | #fee2e2 | 操作失败、错误答案、表单校验错误 |
| info | #3b82f6 | #dbeafe | 信息提示、帮助说明、新功能标记 |

### 暗色模式映射

| 状态 | 文字/图标色 | 背景色 |
|------|-----------|--------|
| success | #34d399 | rgba(16,185,129,0.15) |
| warning | #fbbf24 | rgba(245,158,11,0.15) |
| error | #f87171 | rgba(239,68,68,0.15) |
| info | #60a5fa | rgba(59,130,246,0.15) |

> 暗色模式下状态色提亮一级（400 级），背景用主色 15% 透明度。

---

## 焦点环

| 属性 | 值 |
|------|-----|
| 样式 | 2px solid var(--color-ring) |
| 偏移 | outline-offset: 2px |
| 颜色 | var(--color-primary-500)（light）/ var(--color-primary-400)（dark） |
| 可见条件 | 仅键盘导航时显示（:focus-visible） |
| 禁止 | :focus 不显示焦点环（鼠标/触控不需要） |

```css
:focus-visible {
  outline: 2px solid var(--color-ring);
  outline-offset: 2px;
}
:focus:not(:focus-visible) {
  outline: none;
}
```

---

## 禁用态

| 属性 | 值 |
|------|-----|
| 文字颜色 | var(--color-neutral-400) |
| 背景 | var(--color-neutral-100)（light）/ var(--color-neutral-800)（dark） |
| 边框 | var(--color-neutral-200)（light）/ var(--color-neutral-700)（dark） |
| 光标 | cursor: not-allowed |
| 透明度 | 不使用 opacity（会影响对比度），用具体色值 |
| 交互 | pointer-events: none |

---

## 99. 待确认问题

无

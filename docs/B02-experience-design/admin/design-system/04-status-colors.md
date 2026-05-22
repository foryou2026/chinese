# 状态色（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：01-tokens.md
> **冻结状态**：未冻结

---

## 4 状态色（与 app 端一致）

| 状态 | 色名 | 文字/图标色 | 浅色背景 | 用途 |
|------|------|-----------|---------|------|
| success | 翡翠 emerald | #10B981 | #ECFDF5 | 操作成功、审核通过、在线状态 |
| warning | 琥珀 amber | #F59E0B | #FFFBEB | 警告提示、待审核、数据异常 |
| danger | 红 red | #EF4444 | #FEF2F2 | 操作失败、删除确认、封禁状态 |
| info | 蓝 blue | #3B82F6 | #EFF6FF | 信息提示、帮助说明、数据统计 |

### 完整色阶

```css
:root {
  --color-success-50:  #ECFDF5;  --color-success-100: #D1FAE5;
  --color-success-200: #A7F3D0;  --color-success-500: #10B981;
  --color-success-700: #047857;

  --color-warning-50:  #FFFBEB;  --color-warning-100: #FEF3C7;
  --color-warning-200: #FDE68A;  --color-warning-500: #F59E0B;
  --color-warning-700: #B45309;

  --color-danger-50:  #FEF2F2;  --color-danger-100: #FEE2E2;
  --color-danger-200: #FECACA;  --color-danger-500: #EF4444;
  --color-danger-700: #B91C1C;

  --color-info-50:  #EFF6FF;  --color-info-100: #DBEAFE;
  --color-info-200: #BFDBFE;  --color-info-500: #3B82F6;
  --color-info-700: #1D4ED8;
}
```

### 暗色模式映射

| 状态 | 文字色（提亮） | 背景色（半透明） |
|------|-------------|---------------|
| success | #34D399 | rgba(16, 185, 129, 0.12) |
| warning | #FBBF24 | rgba(245, 158, 11, 0.12) |
| danger | #FCA5A5 | rgba(239, 68, 68, 0.12) |
| info | #93C5FD | rgba(59, 130, 246, 0.12) |

> 暗色模式下文字提亮至 -300/-200 级别，背景用 12% 透明度。

---

## 焦点环

| 属性 | 值 |
|------|-----|
| 样式 | `box-shadow: var(--focus-ring)` = `0 0 0 3px rgba(59, 130, 246, 0.30)` |
| 颜色 | 固定 blue-500（admin 不随 accent 切换） |
| 宽度 | 3px（比 app 的 4px 更紧凑） |
| 可见条件 | 仅 `:focus-visible`（键盘导航） |
| 对比度 | >= 3:1 |

```css
:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: inherit;
}
```

---

## 禁用态

| 属性 | 值 |
|------|-----|
| 透明度 | `opacity: 0.50`（按钮）；输入框用具体色值不用 opacity |
| 光标 | `cursor: not-allowed` |
| 交互 | `pointer-events: none` |
| 输入框背景 | `var(--color-neutral-50)` |
| 输入框边框 | `var(--color-neutral-200)` |
| 输入框文字 | `var(--text-muted)` = `var(--color-neutral-400)` |

---

## 99. 待确认问题

无

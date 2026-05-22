# 状态色

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：01-tokens.md
> **冻结状态**：未冻结

---

## 4 状态色（现代清晰，与 accent 解耦）

| 状态 | 色名 | 文字/图标色 | 浅色背景 | 用途 |
|------|------|-----------|---------|------|
| success | 翡翠 emerald | #10B981 | #ECFDF5 | 操作成功、正确答案、在线状态、关卡完成 |
| warning | 琥珀 amber | #F59E0B | #FFFBEB | 警告提示、即将过期、弱网、Streak 即将断链 |
| danger | 红 red | #EF4444 | #FEF2F2 | 操作失败、错误答案、表单校验错误、生命值耗尽 |
| info | 蓝 blue | #3B82F6 | #EFF6FF | 信息提示、帮助说明、新功能标记、学习小贴士 |

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

## 游戏化专属色（与 accent 解耦）

| 色名 | 色值 | 用途 |
|------|------|------|
| XP 琥珀金 | `--color-xp: #F59E0B` | 经验值数字、XP 进度条填充、XP 飞出动画 |
| Streak 火焰橙 | `--color-streak: #F97316` | 连续天数图标、火焰动画、Streak 冻结警告 |
| 锁定冷灰 | `--color-locked: #94A3B8` | 未解锁关卡节点、锁定内容遮罩 |

> 这三个颜色在 light/dark 模式下保持不变，仅透明度微调。

---

## 焦点环

| 属性 | 值 |
|------|-----|
| 样式 | `box-shadow: 0 0 0 4px var(--color-brand-ring)` |
| 颜色 | 随 accent 自动切换（indigo: rgba(99,102,241,.30), rose: rgba(244,63,94,.30), ...） |
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
| 透明度 | `opacity: 0.45`（按钮）；输入框用具体色值不用 opacity |
| 光标 | `cursor: not-allowed` |
| 交互 | `pointer-events: none` |
| 输入框背景 | `var(--color-neutral-100)` |
| 输入框边框 | `var(--color-neutral-200)` |
| 输入框文字 | `var(--color-neutral-400)` |

---

## 99. 待确认问题

无

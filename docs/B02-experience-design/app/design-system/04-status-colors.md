# 状态色

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：01-tokens.md
> **冻结状态**：未冻结

---

## 4 状态色（中国传统色名，与 accent 解耦）

| 状态 | 色名 | 文字/图标色 | 浅色背景 | 用途 |
|------|------|-----------|---------|------|
| success | 翠玉 jade | #4A6F5A | #E5EFE9 | 操作成功、正确答案、在线状态 |
| warning | 鎏金 gold | #B8923A | #F4ECD8 | 警告提示、即将过期、弱网 |
| danger | 朱砂 cinnabar | #B14545 | #F5E0DC | 操作失败、错误答案、表单校验错误 |
| info | 青花 ink | #2E5C8A | #E8EFF5 | 信息提示、帮助说明、新功能标记 |

### 完整色阶

```css
:root {
  --color-success-50:  #E5EFE9;  --color-success-100: #C9DCD2;
  --color-success-200: #97BAA7;  --color-success-500: #4A6F5A;
  --color-success-700: #2F5640;

  --color-warning-50:  #F4ECD8;  --color-warning-100: #E8D5A8;
  --color-warning-200: #D4B870;  --color-warning-500: #B8923A;
  --color-warning-700: #8C6E2A;

  --color-danger-50:  #F5E0DC;  --color-danger-100: #EAC0B8;
  --color-danger-200: #D89488;  --color-danger-500: #B14545;
  --color-danger-700: #8A2F2F;

  --color-info-50:  #E8EFF5;  --color-info-100: #CFDDE8;
  --color-info-500: #2E5C8A;  --color-info-700: #1B3A5C;
}
```

### 暗色模式映射

| 状态 | 文字色（提亮） | 背景色（半透明） |
|------|-------------|---------------|
| success | #C9DCD2 | rgba(74, 111, 90, 0.18) |
| warning | #E8D5A8 | rgba(184, 146, 58, 0.18) |
| danger | #EAC0B8 | rgba(177, 69, 69, 0.18) |
| info | #CFDDE8 | rgba(46, 92, 138, 0.18) |

> 暗色模式下文字用 -700 级（在暗色 token 中已映射为浅色），背景用 18% 透明度半透。

---

## 焦点环

| 属性 | 值 |
|------|-----|
| 样式 | `box-shadow: 0 0 0 4px var(--color-brand-ring)` |
| 颜色 | 随 accent 自动切换（ink: rgba(46,92,138,.18), cinnabar: rgba(177,69,69,.20), ...） |
| 可见条件 | 仅 `:focus-visible`（键盘导航） |
| 对比度 | ≥ 3:1 |

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
| 输入框背景 | `var(--color-neutral-50)` |
| 输入框边框 | `var(--color-neutral-200)` |
| 输入框文字 | `var(--color-neutral-400)` |

---

## 99. 待确认问题

无

# 交互规范

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：01-tokens.md, 04-status-colors.md
> **冻结状态**：未冻结

---

## 焦点管理

| 规则 | 说明 |
|------|------|
| 焦点环 | 仅 `:focus-visible` 显示（键盘导航），鼠标/触控不显示 |
| 样式 | `box-shadow: var(--focus-ring)` = `0 0 0 4px var(--color-brand-ring)` |
| outline | `outline: none`（用 box-shadow 代替，不影响布局） |
| border-radius | `border-radius: inherit`（焦点环跟随元素圆角） |
| Tab 顺序 | 跟随 DOM 顺序，不使用 tabindex >0 |
| 焦点陷阱 | Modal / Drawer 内焦点循环，不外泄 |
| 焦点恢复 | 弹层关闭后焦点回到触发元素 |
| Skip Link | 页面首元素为"跳到主内容"链接，默认隐藏，Tab 聚焦时显示 |

```css
:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
  border-radius: inherit;
}
```

---

## 键盘导航

| 按键 | 全局行为 |
|------|---------|
| Tab | 前进焦点 |
| Shift+Tab | 后退焦点 |
| Enter | 激活按钮/链接 |
| Space | 激活按钮、切换 Checkbox/Switch |
| Esc | 关闭浮层（Modal/Drawer/Dropdown/Popover） |
| 方向键 | Tab 组件内切换、菜单内移动、日历内移动 |
| Home/End | 列表/菜单首末项 |

### 组件级键盘

| 组件 | 详细键盘规范 |
|------|-------------|
| Tabs | 左右切换，Enter/Space 激活 |
| Dropdown | 上下移动，Enter 选中，首字母快速定位 |
| Select | 上下选择，Enter 确认，键入搜索（Combobox） |
| Accordion | Enter/Space 展开/折叠 |
| Stepper | 不通过键盘切步骤，仅在按钮上操作 |
| Quest 节点 | Tab 移动焦点至节点，Enter 进入关卡 |

---

## 滚动行为

| 场景 | 行为 |
|------|------|
| 主内容 | 原生平滑滚动 `scroll-behavior: smooth` |
| 锚点跳转 | 平滑滚动到目标位置，偏移 TopBar 高度（56px） |
| 弹层打开 | body `overflow: hidden`，防止背景滚动 |
| 弹层关闭 | 恢复 body 滚动位置 |
| 移动端弹性滚动 | `-webkit-overflow-scrolling: touch` |
| 无限滚动 | 距底部 200px 触发加载，loading 指示器 |

### 自定义滚动条（桌面端）

```css
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--color-neutral-300);
  border-radius: var(--radius-pill);
}
::-webkit-scrollbar-thumb:hover {
  background: var(--color-neutral-400);
}
```

---

## 手势（app 移动端）

| 手势 | 行为 |
|------|------|
| 下拉刷新 | 主列表页支持，触发全量刷新 |
| 左滑行 | 可选，露出操作按钮（删除/归档） |
| 下拉 Bottom Drawer | 关闭 |
| 长按 | 可选，触发上下文菜单（Dropdown） |
| 双指缩放 | 禁止（viewport meta `user-scalable=no`） |
| 横滑 Quest Path | 可选，在横向关卡路径上左右滑动查看更多节点 |

> 所有手势操作必须有等价的按钮操作（a11y 要求）。

---

## 触控反馈

| 元素 | 反馈 |
|------|------|
| 普通按钮 | `active: scale(0.98)` + 色值加深，`var(--motion-fast)` |
| 3D 游戏按钮 | `active: translateY(2px)` + `box-shadow` 从 `0 4px 0 0` 缩至 `0 2px 0 0`，`var(--motion-fast)` |
| 列表项 | `active: background var(--color-neutral-100)` |
| 卡片（.glass-card） | `active: scale(0.98)`，`var(--motion-fast)` |
| 图标按钮 | `active: background var(--glass-bg)` |
| Quest 节点 | `active: scale(0.92)` + 弹簧回弹 `var(--easing-spring)` |

```css
@media (hover: none) {
  .interactive:active {
    transform: scale(0.98);
    transition: transform var(--motion-fast);
  }
}
```

---

## 弹簧回弹动效（游戏化核心）

Duolingo 风格的弹簧过冲效果，用于关键交互元素：

```css
/* 弹簧缓动函数 */
--easing-spring: cubic-bezier(.34, 1.56, .64, 1);
```

### 按钮弹簧按压

```css
.btn-game {
  transition: transform 150ms var(--easing-spring),
              box-shadow 150ms var(--easing-spring);
}
.btn-game:active {
  transform: translateY(2px);
  box-shadow: 0 2px 0 0 var(--color-brand-700); /* 从 4px 降至 2px */
}
.btn-game:not(:active) {
  /* 释放后弹簧回弹至原位 */
  transform: translateY(0);
  box-shadow: var(--shadow-btn);
}
```

### Quest 节点弹簧点击

```css
.quest-node:active {
  transform: scale(0.88);
}
.quest-node {
  transition: transform 300ms var(--easing-spring);
}
/* 释放后过冲回弹至 scale(1)，由 cubic-bezier 过冲特性自然实现 */
```

---

## 庆祝动画（正确答案/关卡完成）

### 星星爆发（Star Burst）

| 属性 | 值 |
|------|-----|
| 触发 | 答对题目 |
| 粒子数量 | 6-12 个星星/光点 |
| 粒子颜色 | `var(--color-xp)` 金色 + `var(--color-brand-default)` 品牌色混合 |
| 爆发原点 | 答案按钮中心 |
| 运动轨迹 | 从中心向四周径向扩散，带轻微重力下坠 |
| 持续时间 | 600ms |
| 缓动 | `var(--easing-out)` |
| 粒子消失 | 扩散至终点时 `opacity: 0` + `scale(0)` |

### 完成动画（Level Complete）

| 属性 | 值 |
|------|-----|
| 触发 | 关卡完成 |
| 效果 | 中心大 check 图标 `scale(0 -> 1.2 -> 1)` 弹簧出现 + 环绕金色粒子喷发 |
| 背景 | 全屏半透 `var(--color-success-500)` 15% 闪烁 |
| 持续时间 | 800ms |
| 声音 | 可选，胜利提示音 |

### 五彩纸屑（Confetti）

| 属性 | 值 |
|------|-----|
| 触发 | 成就解锁、等级提升 |
| 粒子数量 | 30-50 个矩形/圆形碎片 |
| 颜色 | Google 四色主题对应色族随机混合 |
| 运动 | 从顶部下落，带旋转和横向随机摆动 |
| 持续时间 | 1200ms |
| 重力模拟 | 加速下落 + 空气阻力减速 |

---

## 错误反馈动画

### 抖动（Shake）

| 属性 | 值 |
|------|-----|
| 触发 | 答错题目、表单校验失败 |
| 目标 | 错误的答案选项/输入框 |
| 幅度 | 左右 +-6px |
| 次数 | 3 次往返 |
| 持续时间 | 400ms |
| 配色 | 同时边框变为 `var(--color-danger-500)` |

```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 50%, 90% { transform: translateX(-6px); }
  30%, 70% { transform: translateX(6px); }
}
.shake {
  animation: shake 400ms var(--easing-out);
}
```

### 错误闪红

| 属性 | 值 |
|------|-----|
| 触发 | 答错题目（与 Shake 同时） |
| 效果 | 背景闪烁 `var(--color-danger-50)` -> transparent |
| 持续时间 | 300ms |

---

## XP 飞出动画（Float Up）

| 属性 | 值 |
|------|-----|
| 触发 | 获得 XP 时 |
| 内容 | "+10 XP" 文字 |
| 字体 | `var(--font-display)`，`var(--weight-extrabold)` |
| 颜色 | `var(--color-xp)` 金色 |
| 起点 | 触发元素正上方 |
| 运动 | 向上飘移 40px + `opacity: 1 -> 0` |
| 持续时间 | 800ms |
| 缓动 | `var(--easing-out)` |
| scale | 从 `scale(0.5)` -> `scale(1.2)` -> `scale(1)` 弹簧进入，然后淡出上飘 |

```css
@keyframes xp-float {
  0%   { transform: translateY(0) scale(0.5); opacity: 0; }
  20%  { transform: translateY(-5px) scale(1.2); opacity: 1; }
  40%  { transform: translateY(-10px) scale(1); opacity: 1; }
  100% { transform: translateY(-40px) scale(1); opacity: 0; }
}
.xp-float {
  animation: xp-float 800ms var(--easing-out) forwards;
}
```

---

## 动效令牌

| 令牌 | 值 | 场景 |
|------|-----|------|
| `--motion-fast` | `150ms cubic-bezier(.16,1,.3,1)` | 按钮按下、焦点、微交互 |
| `--motion-base` | `250ms cubic-bezier(.16,1,.3,1)` | 弹出/收起、Tab 切换、导航栏显隐 |
| `--motion-slow` | `350ms cubic-bezier(.16,1,.3,1)` | Modal/Drawer 进入、页面过渡 |
| `--easing-out` | `cubic-bezier(.16,1,.3,1)` | 弹出类（弹簧感） |
| `--easing-in-out` | `cubic-bezier(.4,0,.2,1)` | 持续类 |
| `--easing-spring` | `cubic-bezier(.34,1.56,.64,1)` | 游戏化弹簧过冲（按钮回弹、节点点击、XP 弹出） |

## hover 微浮起（桌面端通用）

```css
.glass-hoverable:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
  transition: all var(--motion-fast);
}
```

---

## 拖拽

| 场景 | 实现 |
|------|------|
| 文件上传 | dropzone 拖拽（见 12-file-upload.md） |
| 拖拽指示 | 元素半透明(opacity 0.7) + `box-shadow: var(--shadow-lg)` |

---

## 减弱动效

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

> 在 `prefers-reduced-motion: reduce` 下，所有庆祝动画（星星/纸屑/XP飞出）改为静态显示结果（如直接显示 "+10 XP" 1秒后淡出），不播放粒子动画。

---

## 99. 待确认问题

无

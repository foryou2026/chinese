# 交互规范

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
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
| Table | Tab 到行，Enter 展开/操作，方向键移动 |
| Accordion | Enter/Space 展开/折叠 |
| Stepper | 不通过键盘切步骤，仅在按钮上操作 |

---

## 滚动行为

| 场景 | 行为 |
|------|------|
| 主内容 | 原生平滑滚动 `scroll-behavior: smooth` |
| 锚点跳转 | 平滑滚动到目标位置，偏移 TopBar 高度（56px） |
| 弹层打开 | body `overflow: hidden`，防止背景滚动 |
| 弹层关闭 | 恢复 body 滚动位置 |
| 移动端弹性滚动 | `-webkit-overflow-scrolling: touch` |
| 表格水平滚动 | 自定义滚动条样式（6px，圆角） |
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

> 所有手势操作必须有等价的按钮操作（a11y 要求）。

---

## 触控反馈

| 元素 | 反馈 |
|------|------|
| 按钮 | `active: scale(0.98)` + 色值加深，`var(--motion-fast)` |
| 列表项 | `active: background var(--color-neutral-100)` |
| 卡片（.glass） | `active: scale(0.98)`，`var(--motion-fast)` |
| 图标按钮 | `active: background var(--glass-3)` |

```css
@media (hover: none) {
  .interactive:active {
    transform: scale(0.98);
    transition: transform var(--motion-fast);
  }
}
```

---

## 动效令牌

| 令牌 | 值 | 场景 |
|------|-----|------|
| `--motion-fast` | `120ms cubic-bezier(.16,1,.3,1)` | 按钮按下、焦点、微交互 |
| `--motion-base` | `200ms cubic-bezier(.16,1,.3,1)` | 弹出/收起、Tab 切换、导航栏显隐 |
| `--motion-slow` | `320ms cubic-bezier(.16,1,.3,1)` | Modal/Drawer 进入、页面过渡 |
| `--easing-out` | `cubic-bezier(.16,1,.3,1)` | 弹出类（弹簧感） |
| `--easing-in-out` | `cubic-bezier(.4,0,.2,1)` | 持续类 |

## hover 微浮起（桌面端通用）

```css
.glass-hoverable:hover {
  transform: translateY(-1px);
  box-shadow: var(--glass-shadow-lg);
  transition: all var(--motion-fast);
}
```

---

## 拖拽

| 场景 | 实现 |
|------|------|
| 文件上传 | dropzone 拖拽（见 12-file-upload.md） |
| 列表排序 | 可选功能，左侧拖拽手柄（6 点图标） |
| 拖拽指示 | 元素半透明(opacity 0.7) + `box-shadow: var(--glass-shadow-lg)` |
| 放置指示 | 目标位置 2px `var(--color-brand-500)` 水平线 |

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

---

## 99. 待确认问题

无

# 交互规范（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：01-tokens.md, 04-status-colors.md
> **冻结状态**：未冻结

---

## 焦点管理

| 规则 | 说明 |
|------|------|
| 焦点环 | 仅 `:focus-visible` 显示（键盘导航），鼠标/触控不显示 |
| 样式 | `box-shadow: var(--focus-ring)` = `0 0 0 3px rgba(59, 130, 246, 0.30)` |
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
| 方向键 | Tab 组件内切换、菜单内移动 |
| Home/End | 列表/菜单首末项 |

### 组件级键盘

| 组件 | 详细键盘规范 |
|------|-------------|
| Tabs | 左右切换，Enter/Space 激活 |
| Dropdown | 上下移动，Enter 选中，首字母快速定位 |
| Select | 上下选择，Enter 确认，键入搜索（Combobox） |
| Table | Tab 到行，Enter 展开/操作，方向键移动 |
| Accordion | Enter/Space 展开/折叠 |
| SideBar 菜单 | 上下移动，Enter 展开子菜单/导航 |

---

## 滚动行为

| 场景 | 行为 |
|------|------|
| 主内容 | 原生平滑滚动 `scroll-behavior: smooth` |
| 锚点跳转 | 平滑滚动到目标位置，偏移 TopBar 高度（48px） |
| 弹层打开 | body `overflow: hidden`，防止背景滚动 |
| 弹层关闭 | 恢复 body 滚动位置 |
| 表格水平滚动 | 自定义滚动条样式（6px，圆角） |
| 分页加载 | 切换页码后滚动到表格顶部 |

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

## hover 状态

> admin 不使用微浮起（translateY）和弹簧动画。所有 hover 反馈为简单的背景色变化。

| 元素 | hover 效果 |
|------|-----------|
| 按钮 | 背景色加深/提亮一档 |
| 表格行 | 背景色 `var(--color-neutral-50)` |
| 菜单项 | 背景色 `var(--color-neutral-100)` |
| 链接 | 下划线 |
| 卡片 | 无变化（admin 卡片不可点击，仅作为内容容器） |
| 图标按钮 | 背景色 `var(--color-neutral-100)` |

```css
/* admin 不使用浮起动效 */
/* 禁止: transform: translateY(-1px); */
/* 禁止: box-shadow 变化; */
/* 使用: background-color 变化，过渡 var(--motion-fast) */
```

---

## 触控反馈

| 元素 | 反馈 |
|------|------|
| 按钮 | `active: background-color` 加深，`var(--motion-fast)` |
| 列表项/表格行 | `active: background var(--color-neutral-100)` |
| 图标按钮 | `active: background var(--color-neutral-200)` |

> admin 不使用 `scale(0.98)` 缩放效果。反馈仅通过颜色变化实现——干净、即时、无装饰。

---

## 动效令牌

| 令牌 | 值 | 场景 |
|------|-----|------|
| `--motion-fast` | `100ms ease` | hover、焦点、按钮按下 |
| `--motion-base` | `200ms ease-out` | 弹出/收起、Tab 切换、侧栏展开 |
| `--motion-slow` | `200ms ease-out` | Modal/Drawer 进入（admin 不需要更慢的动效） |

> admin 不使用弹簧缓动函数 `cubic-bezier(.16,1,.3,1)`。所有过渡使用标准 `ease` / `ease-out`。
> admin 不使用 `--motion-slow: 350ms` 的慢动效——200ms 足以完成所有过渡。

---

## 拖拽

| 场景 | 实现 |
|------|------|
| 文件上传 | dropzone 拖拽（见 05-components/12-file-upload.md） |
| 列表排序 | 可选功能，左侧拖拽手柄（6 点图标） |
| 拖拽指示 | 元素半透明 `opacity: 0.7` + `var(--shadow-md)` |
| 放置指示 | 目标位置 2px `var(--color-accent)` 水平线 |

---

## 无庆祝/装饰动效

admin 管理后台**禁止**以下动效：

- 弹簧/回弹（spring/bounce）动画
- 纸屑/星星/庆祝效果
- 微浮起（translateY）hover
- 呼吸/脉冲光环
- 极光渐变动画
- 任何装饰性动画

> 管理后台的一切动效服务于状态反馈——hover 变色、展开/折叠、弹层进出，仅此而已。

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

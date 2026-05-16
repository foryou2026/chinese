<!-- TARGET-PATH: docs/B03-design/design-system/_input/visual-input.md -->

# 视觉输入（B03-S01）

> 阶段：B04-S 设计系统 · 用户输入  
> 确认 by PM · 2026-04-28

---

## 1. 想要的视觉感受

- **黑白红 + 全局毛玻璃**：唯一品牌色 = 红（小红书红 `#FF2442` 亮 / `#FF3B5C` 暗）；其他视觉差异只用透明度 + 中性灰实现。
- **现代 + 克制 + 质感 + 趣味 + 沉浸**（见 B03 体验定调）。
- 暗模式 day-1 上线，**真黑**（`#0A0A0B`），不是纯 `#000`。
- 全局**无侧边栏**；只有顶部导航。
- 全屏宽度，**不**在中间居中固定列宽。

## 2. 关键参照

- 小红书：红色 + 毛玻璃 + 卡片质感；
- Stitch（Google Labs 设计工具）：毛玻璃 + 远景光晕 + 微噪；
- Notion：内容简洁、键盘党友好；
- Vercel Dashboard：暗模式真黑；
- Apple Music：卡片 hover 微抬。

## 3. 字体

- 拉丁：Inter / Be Vietnam Pro / Noto Sans Thai Looped；
- 中文：Noto Sans SC（UI）+ Noto Serif SC（汉字教学卡片 / 释义）；
- 等宽：JetBrains Mono；
- 自托管（详见 `B01-architecture/07-i18n-responsive.md`）。

## 4. 必有的图标 / 插画 / 图片风格

- 图标：lucide-react（线条风格、18px 标准、2px stroke）；
- 插画：线条风格 + 单色 `--text-tertiary` + 红色辅助高光；
- 图片：圆角 `radius-md`；暗模式叠 1px `--border-subtle` 防边缘融化；
- 头像：圆形 `radius-pill`；首字符兜底色块（红底白字）。

## 5. 必有的动效

- hover / focus = 120ms；
- 主交互 = 200ms；
- 弹窗 = 320ms ease-out + 透明度；
- 拖拽 / 列表插入 = Framer Motion spring；
- 全部尊重 `prefers-reduced-motion: reduce`。

## 6. 主题色自定义

- 用户可在「设置 → 显示 → 主题色」改 `--brand`，覆盖一整套 brand token；
- 黑白中性色不变；
- 不做节日皮肤（圣诞 / 春节等本期不上）。

## 7. 必须遵守 / 必须避开

| ✅ 必须 | ❌ 不允许 |
|--------|---------|
| 毛玻璃面板（顶栏 / 卡片 / 弹窗 / Drawer / Toast / Tab / 按钮）| `bg-white` / `bg-zinc-900` 实色卡片 |
| 顶栏 sticky + 滚动后阴影渐变 | 任何侧边栏（v1 全禁）|
| 内容区全屏宽度 | 中心固定列宽（`max-w-7xl mx-auto` 在普通页禁用）|
| 错误用品牌红 = `--danger` | 引入蓝 / 紫 / 橙 当第二品牌色 |
| 暗模式真黑 `#0A0A0B` | 纯 `#000` 配纯红 |
| lucide 线条图标 | 拟物 3D 图标 / mascot |

## 8. PM 签字
任何视觉变更先动 B04（本目录）+ B03（体验定调），后改代码。

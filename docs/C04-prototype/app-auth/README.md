<!-- TARGET-PATH: docs/C04-prototype/app-auth/README.md -->

# `app-auth` · HTML 原型

> **阶段**：C04-H · **feature**：`app-auth`  
> **状态**：**占位 / 暂缓**（与 [`C04-prototype/_global-style/README.md`](../_global-style/README.md) 保持一致）  
> **冻结状态**：未启动 · 2026-05-16

---

## 1. 为什么暂缓

- 项目尚处 D 阶段反向回写补完期；
- 视觉规范 [B04-design](../../B04-design/design-system/00-index.md) 已经够支持 v1 上线，不再依赖 HTML 原型；
- prototype-style 规范文档本身（批次 2）也是占位状态。

## 2. 真正需要 HTML 原型时的产出物

按 [`prompt/A-framework/A00-04-文档目录规划.md`](../../../prompt/A-framework/A00-04-文档目录规划.md) §C04 要求，本目录最终应交付：

- `index.html` — 9 个 page-id 的导航首页；
- `pages/<page-id>.html` — 每页 1 个 HTML（共 9）；
- `assets/css/` — token 变量复刻 B04-design `01-tokens.md`；
- `assets/js/state.js` — 状态机切换 demo；
- 全部基于 [`C03-pages/app-auth/*.md`](../../C03-pages/app-auth/) 既有 DOM 骨架直译。

## 3. 触发条件

任一发生时启动 C04：

1. 需要给非技术干系人演示交互细节；
2. 设计稿（Figma）需要"可点击高保真"评审版本；
3. 视觉规范出现重大变更，希望先在原型上验证。

## 4. 输入

- [`_input/prototype-direction.md`](./_input/prototype-direction.md)

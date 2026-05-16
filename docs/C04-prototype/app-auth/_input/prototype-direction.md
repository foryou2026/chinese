<!-- TARGET-PATH: docs/C04-prototype/app-auth/_input/prototype-direction.md -->

# H01 · 原型方向(app-auth)

> **冻结状态**:v1.0 · 2026-05-16

## 目的
- 反向回写期补登:把 [`C03-pages/app-auth/`](../../../C03-pages/app-auth/) 既有 DOM 骨架直译为可双击打开的 HTML;
- 演示 [`B04-design/design-system`](../../../B04-design/design-system/) 设计 token + 毛玻璃 + 红色品牌色在登录/账号场景的真实效果。

## 范围
- 全部 page-id 一次性出齐(见 index.html);
- 每个 P0 页面 4 状态齐(default/loading/empty/error);
- 权限页加 forbidden 态。

## 不在此期内的能力(由 vendor proto.* / 后续 H 阶段补)
- 真实接口请求(全部 mock-data.js);
- 主题色拾色器 UI(仅亮/暗切换);
- 多语言切换 UI(仅顶栏占位)。

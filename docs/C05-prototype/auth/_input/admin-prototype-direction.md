<!-- TARGET-PATH: docs/C05-prototype/auth/_input/admin-prototype-direction.md -->

# H01 · 原型方向(auth)

> **冻结状态**:v1.0 · 2026-05-16

## 目的
- 把 [`C04-pages/auth/admin/`](../../../C04-pages/auth/admin/) 既有 DOM 骨架直译为可双击打开的 HTML;
- 演示 [`B03-design/design-system`](../../../B03-design/design-system/) 设计 token + 毛玻璃 + 红色品牌色在登录/账号场景的真实效果。

## 范围
- 全部 page-id 一次性出齐(见 index.html);
- 每个 page-id 只出 1 个默认态 HTML，平铺在 `<surface>/` 根下;
- 空 / 加载 / 错 / 无权限态由 [`docs/C06-prd/auth/`](../../../C06-prd/auth/) 文字描述，不出图。

## 不在此期内的能力（由后续 D 阶段补）
- 真实接口请求(示例数据直接写在 HTML 静态片段);
- 主题色拾色器 UI(仅亮/暗切换);
- 多语言切换 UI(仅顶栏占位)。

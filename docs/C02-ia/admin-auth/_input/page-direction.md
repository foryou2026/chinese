<!-- TARGET-PATH: docs/C02-ia/admin-auth/_input/page-direction.md -->

# I01 · 页面方向 · `admin-auth`

- surface = `admin` · 路径前缀 `/admin/auth/*` 与 `/admin/me`
- 4 页极简:不需要侧边栏 / 不需要复杂导航;登录/忘密/重置共用居中卡片布局,`/admin/me` 复用 admin 全局 layout (左侧导航 + 右上头像)
- 与 app 端**强制视觉差异**:深色 admin 主题 (B04 设计 token 中的 admin 暗色)、表单字段更紧凑、按钮更方正
- 错误展示:沿用 B04-05 的 4xx 内联 / 5xx Toast 约定
- 顶栏头像下拉仅 2 项:"账号与安全" → `/admin/me` · "退出登录" → 调 `/admin/v1/auth/session-revoke`

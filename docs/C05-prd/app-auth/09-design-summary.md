<!-- TARGET-PATH: docs/C05-prd/app-auth/09-design-summary.md -->

# 09 · 设计要点

视觉规范全文见 [`B04-design/design-system/`](../../B04-design/design-system/00-index.md)；本节仅汇总本 feature 用到的关键点：

- **卡片化**：`<GlassCard>` 是所有 auth + me 页的核心容器；
- **居中布局**：auth 页全屏居中；me 页 `.page` 标准宽度，左对齐；
- **品牌色 (--brand `#FF2442`)**：仅用于：主按钮、登录页强调标题底色（可选 hairline）、强度条最高态、强提醒（错误用 `--error` 不同色）；
- **暗黑模式自动**：跟随 OS prefers-color-scheme；显式切换写 cookie；
- **字段错误**：内联红字，**不**用红框（避免色盲），但 `outline: 2px solid --error` 在 focus 态出现；
- **Loading**：按钮 inline spinner 替代文字；不在卡片外加 mask；
- **i18n key 前缀**：`auth.*`、`me.*`、`common.error.*`；
- **表单可纯键盘完成**：Tab 顺序 = 视觉顺序；Enter 触发主按钮；
- **避免布局抖动**：错误内联展开使用 `min-height` 占位，校验红字出现时不挤压下方按钮。

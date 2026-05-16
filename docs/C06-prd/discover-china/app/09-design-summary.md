<!-- TARGET-PATH: docs/C06-prd/discover-china/app/09-design-summary.md -->

# 09 · 设计摘要 · discover-china / **app**

## 9.1 视觉调性

| 维度 | 选择 |
|------|------|
| 主色 | 沿用 B03;阅读态偏暖白(护眼) |
| 暗色模式 | 必须;阅读场景高频 |
| 字号基线 | 中文 17px(略大,阅读型);拼音 13px;翻译 15px |
| 信息密度 | 低;一屏一句聚焦 |

## 9.2 关键组件(↑ [B03 05-components](../../../B03-design/design-system/05-components/))

| 组件 | 来源 |
|------|------|
| `Card`(类目卡 / 文章卡) | [B03 05-04-card.md](../../../B03-design/design-system/05-components/11-cards-glass.md) |
| `List`(文章列表) | [B03 05-08-table.md](../../../B03-design/design-system/05-components/03-tables.md) 列表形态 |
| `AudioPlayer`(句级) | [B03 05-12-audio-player.md](../../../B03-design/design-system/05-components/00-index.md) |
| `Input`(搜索) | [B03 05-07-form.md](../../../B03-design/design-system/05-components/02-forms.md) |

## 9.3 交互模式

- **行点击播放**:整行(汉字 + 拼音 + 翻译)为点击热区,**避免** 仅小图标
- **三层显示开关**:右上角 toolbar,3 个独立 toggle
- **句子高亮**:当前播放句子背景色提亮
- **手势**:上下滚动正常;左右滑切换文章(列表内顺序);**禁用** 双指缩放(避免与系统冲突)

## 9.4 响应式

与 course/app 同:移动优先;PC ≥ 1024px 居中容器。

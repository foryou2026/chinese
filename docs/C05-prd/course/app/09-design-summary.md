<!-- TARGET-PATH: docs/C05-prd/course/app/09-design-summary.md -->

# 09 · 设计摘要 · course / **app**

> 项目设计系统真相在 [`B04-design/design-system/`](../../../B04-design/design-system/);本文件只摘要 app 端关键 UI 决策。

## 9.1 视觉调性

| 维度 | app 端选择 |
|------|----------|
| 主色 | 沿用 B04 主色 token;学习态强调专注 |
| 暗色模式 | 必须支持(夜间学习场景) |
| 字号基线 | 中文 16px+;汉字优先级最高;拼音 12-14px;翻译同字号 |
| 信息密度 | 中低密度;卡片式;单屏一个主任务 |

## 9.2 关键组件(↑ [B04 05-components](../../../B04-design/design-system/05-components/))

| app 端高频组件 | 来源 |
|---------------|------|
| `Card` | [B04 05-04-card.md](../../../B04-design/design-system/05-components/04-card.md) |
| `Button` | [B04 05-02-button.md](../../../B04-design/design-system/05-components/02-button.md) |
| `Tabs` | [B04 05-09-tabs.md](../../../B04-design/design-system/05-components/09-tabs.md) |
| `AudioPlayer` | [B04 05-12-audio-player.md](../../../B04-design/design-system/05-components/12-audio-player.md)(节内 KP 音频) |

## 9.3 交互模式

- **左下角"回到学习"**悬浮按钮:任何 app 页面均可一键回到当前游标节
- **滑动手势**:节内 KP 卡片左右滑动;答题不滑(避免误触)
- **触觉反馈**:答对(轻)/ 答错(中);设置可关

## 9.4 响应式

- 移动优先;PC 浏览器 ≥ 1024 px 时居中 480 px 宽容器(模拟手机);
- 平板 768-1023 px:同移动栈式布局,左右内边距增大。

## 9.5 国际化字符

| 语种 | 注意点 |
|------|------|
| `vi` | 越南语带声调字符宽度 +10%,需为按钮文本预留 |
| `th` | 泰语行高 +20%,无空格分词 |
| `id` | 印尼语单词最长,按钮文字截断需用 ellipsis |

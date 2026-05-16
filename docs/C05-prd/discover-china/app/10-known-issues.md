<!-- TARGET-PATH: docs/C05-prd/discover-china/app/10-known-issues.md -->

# 10 · 已知问题 · discover-china / **app**

| ID | 一句话 | 影响 | 计划 |
|----|-------|------|------|
| KI-app-disc-001 | iOS 后台播放 TTS 中断 | [P-003](06-page-specs/P-app-discover-china-003.md) | Round 9 用 Media Session API |
| KI-app-disc-002 | 弱网下首屏文章列表加载慢 | [P-002](06-page-specs/P-app-discover-china-002.md) | 加首屏 SSR / 静态预渲染评估 |
| KI-app-disc-003 | 5 语切换时正文翻译行有 100ms 闪烁 | [P-003](06-page-specs/P-app-discover-china-003.md) | 翻译数据预加载 |
| KI-app-disc-004 | 类目图标在低分辨率屏失真 | [P-001](06-page-specs/P-app-discover-china-001.md) | 改 SVG |

## 已澄清不修

| ID | 一句话 | 原因 |
|----|-------|------|
| KI-app-disc-005 | 不支持整文连续播放 | 体验设计:句级播放确保用户跟读 |
| KI-app-disc-006 | 不进 SRS / 错题本 | 本 feature 浏览型,无答题模型 |

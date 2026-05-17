<!-- TARGET-PATH: docs/C06-prd/discover-china/app/07-business-rules.md -->

# 07 · 业务规则 · discover-china / **app**

| R-ID | 规则 |
|------|------|
| R-001 | 仅 `published = true` 文章可见 |
| R-002 | 分类树最多 3 层 |
| R-003 | 文章 cursor 分页;limit ≤ 50 |
| R-004 | TTS 按 lang 缓存 30 天;命中不计费 |
| R-005 | 搜索 q 必须 ≥ 2 字符;< 2 拒收 |
| R-028 | UI 语种切换实时;不重启播放 |

## 失败降级

| TTS 失败 | 显示文本 + 重试按钮;不阻断阅读 |

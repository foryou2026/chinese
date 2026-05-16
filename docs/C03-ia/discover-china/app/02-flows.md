<!-- TARGET-PATH: docs/C03-ia/discover-china/app/02-flows.md -->

# 02 · 关键流程 · discover-china / **app**

## F-app-disc-1 · 浏览到播放

```
P-app-discover-china-001(分类首页) → 选分类 → P-002(文章列表,cursor 翻页)
                                  → 选文章 → P-003(文章详情 + 句子) → 点句子 → TTS 播放
```

OP:`GET /categories` · `GET /articles?category=...&cursor=` · `GET /articles/:slug` · `GET /sentences/:id/tts`。

## F-app-disc-2 · 搜索

```
P-001 顶部搜索框 → q → GET /search?q= → 结果列表 → 命中文章 → P-003
```

## F-app-disc-3 · 离线降级

```
TTS 失败(网络/上游) → 仅显示文本 + 重试按钮 + toast "音频暂不可用"
```

> 已废弃 `/me/progress`(原 R-006/007),不在本流程中。

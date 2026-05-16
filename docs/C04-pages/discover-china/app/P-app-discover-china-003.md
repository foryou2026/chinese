<!-- TARGET-PATH: docs/C04-pages/discover-china/app/P-app-discover-china-003.md -->

# `P-app-discover-china-003` · 文章逐句详情 + TTS

> **R 覆盖**:R-003..006
> **冻结状态**:已冻结 · 2026-05-16

## 1. 布局
- 顶部面包屑 + 标题区(文章名中 + 本地 + 拼音);
- 工具栏:`全文朗读 / 暂停` · `跳到上次阅读` · `上一篇 / 下一篇`;
- 句子卡片纵向流(每句 1 卡);
- 右下浮动:`返回类目` Anchor。

## 2. DOM 骨架
```
Breadcrumb
ArticleHeader { pinyin, h1 中文, h3 本地语, meta }
PlayerBar (sticky) { 播放/暂停 · 当前句号 · 全文按钮 }
SentenceList {
  SentenceCard ×N (id=s-{句子顺序号}, data-block="Sentence") {
    PlayButton (data-op="OP-tts-play", aria-label="朗读")
    pinyin (text-caption)
    chinese (text-body-lg)
    local (text-body, 中文用户隐藏)
    SeqBadge {句子顺序号}
  }
}
EndCard { 上一篇 / 下一篇 / 返回类目 }
```

## 3. 数据
- → `{ article, sentences: [{ 句子顺序号, content_i18n, pinyin, audio_url? }] }`;
- → `{ audio_url }`(详 D02);
- 操作(登录用户)/ `localStorage`(访客)。

## 4. 状态
| 态 | 触发 | 表现 |
|---|------|------|
| idle | 默认 | 句子卡片列表 |
| loading | 首屏 | 3 卡片 skeleton |
| empty | sentences.length=0(异常) | 空态"内容缺失,请联系管理员" |
| article-gone | 404 | 空态"该文章已下架或不存在" + 返回类目 |
| tts-loading | 单句加载音频 | 按钮 spinner |
| tts-playing | 播放中 | 按钮 pause 图标 |
| tts-error | 失败 | Toast + 按钮回 idle |
| fulltext-playing | 全文朗读中 | PlayerBar 高亮当前句卡片(滚动到可视区) |
| fulltext-paused | 暂停 | 当前句保持高亮 |

## 5. 交互
- **单句播放**:按钮点 → loading → 播放;再点 → 暂停;
- **全文朗读**:从"当前可视/上次阅读"句开始 → onended → 自动下一句;
- **进度同步**:滚动到句子或点击句子卡片 → debounce 1s 更新远端 / 本地进度;
- **进入页**:fetch 进度 → 滚动到对应句子;
- **上一篇 / 下一篇**:同类目内 seq 顺序;

## 6. 错误码
- TTS 5xx → `tts-error` Toast,后台 retry;
- 文章 404 → article-gone;
- 401 应用端访客访问 04-12 → 跳 login + redirect 当前 url。

## 7. 移动端
- PlayerBar 改 sticky 底部 + 大图标;
- 句子卡片字号 +1pt;
- 全文朗读时屏幕常亮 + 锁滚动跟随。

## 8. 无障碍
- 当前句 `aria-current="true"`;
- 播放按钮 `aria-pressed`;
- 朗读时高亮符合 `prefers-reduced-motion`。

## 9. 性能 / 埋点
- 音频通过 audio 标签 + service worker 缓存;
- `china.article_open` / `china.sentence_tts_play` / `china.fulltext_play`。

## 10. 多语言
- 中文用户:仅显示拼音 + 中文,本地语行隐藏;
- 非中文用户:三层全显示;
- TTS 永远播放中文(不做多语 TTS)。

<!-- TARGET-PATH: docs/C06-prd/discover-china/app/01-overview.md -->

# 01 · 总览 · discover-china / **app**

> 跨端真相在 [`../_shared/`](../_shared/);本文件聚焦 app 端独有视角。

## 1.1 app 端定位

`discover-china` app 端是知语应用首批上线的 **内容浏览型一级 Tab**,以 **12 个固定中国文化类目** 为入口,为东南亚学习者提供 **"拼音 + 中文 + 本地语言"三层对照** 的文章 + **逐句 TTS** 体验。来源:〔历史素材〕。

## 1.2 12 个固定类目

| 编码 | 类目 | 说明 |
|------|------|------|
| 01 | 中国历史 | 朝代更替、历史事件、传奇人物 |
| 02 | 中国美食 | 八大菜系、地方小吃、饮食文化 |
| 03 | 名胜风光 | 自然奇观、历史遗迹、城市地标 |
| 04 | 传统节日 | 传统节日、节气、民间习俗 |
| 05 | 艺术非遗 | 书法、国画、剪纸、陶瓷、刺绣 |
| 06 | 音乐戏曲 | 民族乐器、京剧、民歌 |
| 07 | 文学经典 | 古典名著、诗词歌赋、寓言 |
| 08 | 成语典故 | 成语故事、歇后语、谚语 |
| 09 | 哲学思想 | 儒释道、诸子百家 |
| 10 | 当代中国 | 科技、城市生活、流行文化 |
| 11 | 趣味汉字 | 汉字演变、数字密码、网络用语 |
| 12 | 神话传说 | 创世神话、神仙体系、民间传说 |

> 类目数量固定为 12,**不可** 新增 / 删除;名称 5 语录入(`zh/en/vi/th/id`),由 admin 端 [P-admin-discover-china-001](../../../discover-china/admin/06-page-specs/P-admin-discover-china-001.md) 维护。

## 1.3 app 端 3 大页

| 页面 | 入口 |
|------|------|
| 分类首页 + 搜索 | [P-app-discover-china-001](06-page-specs/P-app-discover-china-001.md) |
| 分类下文章列表 | [P-app-discover-china-002](06-page-specs/P-app-discover-china-002.md) |
| 文章详情 + 句子 TTS | [P-app-discover-china-003](06-page-specs/P-app-discover-china-003.md) |

## 1.4 内容模型(app 端可见)

- **文章**:`(article_code 12 位, title_pinyin, title 5 语 ≤ 40, sentences[])`
- **句子**:`(sentence_code 4 位 0001 起, 中文 ≤ 400 字, pinyin, 5 语翻译, audio_url(MP3 CDN))`

## 1.5 性能基线

| 接口 | 目标 |
|------|------|
| `GET /api/app/v1/discover/categories`(12 类目 静态) | 强缓存 24h |
| `GET /api/app/v1/discover/articles?cat=NN` | P95 ≤ 250 ms |
| `GET /api/app/v1/discover/article/{code}` | P95 ≤ 300 ms;含全部句子 |
| 句子音频 | CDN 强缓存,单句 ≤ 200 KB |

## 1.6 与 course 的隔离

- `discover-china` **不进** SRS / 错题本;
- 学员阅读进度 **不计** 入 course 个人统计(仅本 feature 内"上次读到")。

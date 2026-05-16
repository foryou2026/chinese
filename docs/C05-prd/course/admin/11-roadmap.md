<!-- TARGET-PATH: docs/C05-prd/course/admin/11-roadmap.md -->

> **本文件为 surface=`admin` 视角的 PRD 章节(Round 2 从 PRD.md 第 11 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

## 11. 与其它 feature 的边界

- 与 [`discover-china`](../../C05-prd/discover-china/PRD.md) 共享:5 语 locale、媒资库技术栈、Admin 角色与 LWW 模式;不共享:类目编码 / 文章结构 / TTS 缓存键命名;
- 与未来 `payments`(订阅)feature:`users.subscription` 字段对接,本期 BR-P03 视订阅状态拦截;支付流走 mock 适配(docker-policy)。

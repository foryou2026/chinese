<!-- TARGET-PATH: docs/C05-prd/discover-china/admin/02-glossary.md -->

> **本文件为 surface=`admin` 视角的 PRD 章节(Round 2 从 PRD.md 第 2 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

## 2. 术语表

| 术语 | 说明 |
|------|------|
| 类目(Category)| 12 个固定文化主题,编码 `01..12` |
| 文章(Article)| 类目下的文本,12 位编码 `{类目 2}{自增 10}` |
| 句子(Sentence)| 文章内可单独编辑 / 朗读的最小单元,带 4 位 seq_no |
| 5 语 | 简体中文 / 英 / 越南 / 泰 / 印尼 |
| TTS | 中文文本转语音,全局缓存,键 `{article_code}-{seq_no}` |
| super_admin | 管理端唯一角色 |

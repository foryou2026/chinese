<!-- TARGET-PATH: docs/C06-prd/discover-china/_shared/glossary.md -->

# discover-china feature · 共享术语表

> **跨 surface 共享术语表(Round 2 从 PRD.md 第 2 章迁出)。** app/admin 双端均引用本文件。

## 2. 术语表

| 术语 | 说明 |
|------|------|
| 类目(Category)| 12 个固定文化主题,编码 `01..12` |
| 文章(Article)| 类目下的文本,12 位编码 `{类目 2}{自增 10}` |
| 句子(Sentence)| 文章内可单独编辑 / 朗读的最小单元,带 4 位 句子顺序号 |
| 5 语 | 简体中文 / 英 / 越南 / 泰 / 印尼 |
| TTS | 中文文本转语音,全局缓存,键 `{文章编码}-{句子顺序号}` |
| admin | 管理端唯一角色 |

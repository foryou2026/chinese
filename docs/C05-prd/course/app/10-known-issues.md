<!-- TARGET-PATH: docs/C05-prd/course/app/10-known-issues.md -->

> **本文件为 surface=`app` 视角的 PRD 章节(Round 2 从 PRD.md 第 10 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

## 10. 国际化与端策略

- 应用端 5 语 UI 切换,文案 key 前缀 `course.*`;
- 应用端学员**端**:Web App + 微信 H5 + 后期 RN(同套页面);
- 管理端:Web 桌面优先;
- 数据层 5 语字段统一 `*_i18n: { zh, en, vi, th, id }`;
- 缺失语言渲染回退 `zh`,前端浅色提示。

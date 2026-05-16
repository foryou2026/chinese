<!-- TARGET-PATH: docs/C05-prd/discover-china/admin/08-roles-permissions.md -->

> **本文件为 surface=`admin` 视角的 PRD 章节(Round 2 从 PRD.md 第 8 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

## 8. 角色权限

| 操作 | 访客 | 应用用户 | super_admin |
|------|:--:|:--:|:--:|
| 浏览 01-03 类目 | ✓ | ✓ | ✓ |
| 浏览 04-12 类目 | × | ✓ | ✓ |
| 阅读 / TTS | ✓(01-03) / ✓(04-12 登录后) | ✓ | ✓ |
| 进度同步(远端) | × | ✓ | ✓ |
| 进入 `/admin/china*` | × | × | ✓ |
| 文章 / 句子 CRUD | × | × | ✓ |
| 全局搜索 | × | × | ✓ |

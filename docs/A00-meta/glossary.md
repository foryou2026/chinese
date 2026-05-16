<!-- TARGET-PATH: docs/A00-meta/glossary.md -->

# A00 · 项目术语表（global）

> 全项目共享术语。C 阶段 feature 局部术语放各 feature 的 `docs/C06-prd/<feature>/02-glossary.md`；
> 跨 feature 共享的术语沉淀到本文件 + `docs/C06-prd/_glossary.md`（二者同义，前者偏框架/工程，后者偏产品）。

| 术语 | 英文 / 缩写 | 释义 |
|------|------------|------|
| 知语 | Zhiyu | 项目正式名；面向东南亚（越南 / 泰国 / 印尼）用户的中文学习软件 |
| 应用端 | app surface | 面向 C 端（学习者）的前端 + 后端，端口 fe=3100 / be=8100 |
| 管理后台 | admin surface | 面向内容运营、客服、AI 训练师的前端 + 后端，端口 fe=4100 / be=9100 |
| 发现中国 | discover-china | feature ID；首页"文化频道"，按类目浏览中国主题文章、句子级 TTS |
| 课程 | course | feature ID；主线学习地图（主题 → 阶段 → 章 → 节）、知识点 KP、SRS 复习、考试 |
| 知识点 | KP（Knowledge Point）| 课程内最小可教学单元（汉字、词、语法点等） |
| SRS | Spaced Repetition System | 间隔重复复习系统，错题与已学 KP 进入复习池 |
| 节末小测 | section quiz | 一节学习结束后的过关测验 |
| 类目 | category | 「发现中国」的一级 / 二级目录（如「饮食」「节日」） |
| 句子级 TTS | sentence TTS | 文章中以句子为最小单位的语音合成与朗读控制 |
| jsonb 多语言 | i18n jsonb | 业务文案以 `{zh,en,vi,th,id}` 五语 jsonb 存储 |
| RPC | Postgres RPC | Postgres 中以 SQL 函数封装的复杂业务事务，前后端通过 `supabase.rpc()` 调用 |
| Adapter | Adapter Layer | 第三方 / AI 服务的统一接入层，缺 Key 自动 fallback 到 mock |
| 全栈 TS | full-stack TypeScript | 前端 / 后端 / 共享包 / 脚本 / Edge Functions 全部 `.ts`，禁止 `.js` / `.mjs` / JSDoc |
| Docker-only | Docker-only dev | 唯一 dev 环境运行在 Docker 容器内，禁止裸机；自动化测试也在容器内 |
| 反爬虫纯 CSR | CSR / SPA only | 前端禁止 SSR/SSG/数据预注入；HTML 仅空壳 |

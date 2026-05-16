<!-- TARGET-PATH: docs/C03-ia/discover-china/_shared/flows-shared.md -->

# 02 · Flow 一览

| Flow-ID | 名称 | 类型 | 上游 page | 下游 page | 来源 |
|---------|------|------|----------|----------|------|
| FL-discover-china-01 | 访客 12 类目浏览 → 公开类目下钻 | 主 | — | P-app-001 → P-app-002 → P-app-003 | C01 main ① |
| FL-discover-china-02 | 全文朗读 | 主 | P-app-003 | P-app-003 | C01 main ② |
| FL-discover-china-03 | 进度记忆同步 | 主 | P-app-003 | P-app-003 | C01 main ③ |
| FL-discover-china-04 | 管理员新建文章 | 主 | P-admin-002 | P-admin-003 | C01 main ④ |
| FL-discover-china-05 | 句子编辑 / 插入 / 重排 | 主 | P-admin-003 | P-admin-003 | C01 main ⑤ |
| FL-discover-china-06 | 管理端三级搜索 | 主 | P-admin-001..003 | P-admin-004 | C01 main ⑥ |
| FL-discover-china-07 | 04-12 类目登录引导 | 异 | P-app-001 | `/auth/login` | C01 exc E1 |
| FL-discover-china-08 | TTS 失败 + 后台重试 | 异 | P-app-003 | P-app-003 | C01 exc E2 |
| FL-discover-china-09 | 阅读中文章被下架 | 异 | P-app-003 | P-app-002 | C01 exc E3 |
| FL-discover-china-10 | 管理端后写覆盖 + 提示 | 异 | P-admin-003 | P-admin-003 | C01 exc E4 |
| FL-discover-china-11 | 未保存离开拦截 | 异 | P-admin-003 | * | C01 exc E5 |
| FL-discover-china-12 | 类目删除尝试拒绝 | 异 | P-admin-001 | P-admin-001 | C01 exc E6 |
| FL-discover-china-13 | 5 语未齐发布拦截 | 异 | P-admin-003 | P-admin-003 | C01 exc E7 |

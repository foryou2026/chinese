# 权限矩阵

## P2. 权限矩阵

| 资源/操作 | ROLE-ADMIN | 数据范围 | 所属功能 |
|-----------|-----------|---------|---------|
| 翻译总览仪表盘 | 允许 | 全局 | i18n/translation-hub |
| 语言列表查看 | 允许 | 全局 | i18n/translation-hub |
| 语言启用/停用 | 允许 | 全局 | i18n/translation-hub |
| 语言排序 | 允许 | 全局 | i18n/translation-hub |
| UI 文案列表查看 | 允许 | 全局 | i18n/translation-hub |
| UI 文案翻译编辑 | 允许 | 全局 | i18n/translation-hub |
| UI 文案 AI 翻译触发 | 允许 | 全局 | i18n/translation-hub |
| UI 文案发布 | 允许 | 全局 | i18n/translation-hub |
| 数据表列表查看 | 允许 | 全局 | i18n/translation-hub |
| 表级翻译配置 | 允许 | 全局 | i18n/translation-hub |
| 字段级翻译配置 | 允许 | 全局 | i18n/translation-hub |
| 内容翻译查看/编辑 | 允许 | 全局 | i18n/translation-hub |
| 内容 AI 翻译触发 | 允许 | 全局 | i18n/translation-hub |
| 翻译任务查看/取消 | 允许 | 全局 | i18n/translation-hub |
| 配音开关配置 | 允许 | 全局 | i18n/translation-hub |
| 配音接口配置 | 允许 | 全局 | i18n/translation-hub |
| 配音触发/管理 | 允许 | 全局 | i18n/translation-hub |

### P2.2 授权校验机制
- 前端：路由守卫拦截未登录用户
- 后端：Hono 中间件校验 JWT，验证 `app_metadata.role = 'admin'`
- 行级/字段级：无 RLS（管理员操作全局数据）

## P3. 本轮权限变更摘要
| 变更类型 | 对象 | 说明 | 来源功能 |
|---------|------|------|---------|
| 新增矩阵 | i18n 管理相关 17 项操作 | 全部新增 | i18n/translation-hub |

# 接口规范 · translation-hub · 总览

> **系统**：admin
> **关联 R-ID**：R-i18n-001~062
> **不做**：表结构(D01)、页面/原型(C02/C03)
> **特殊说明**：所有接口需 Bearer JWT + role=admin 鉴权。翻译任务与配音任务均为异步执行，通过轮询或 WebSocket 获取进度。
> **接口详情**：01-languages.md ~ 06-translation-api.md

---

## 1. 路由表

### 1.1 page-id → URL 映射

| page-id | 页面名称 | URL | 鉴权 | 可见角色 |
|---------|---------|-----|------|---------|
| P-admin-i18n-001 | 翻译总览仪表盘 | /i18n | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-002 | 语言管理页 | /i18n/languages | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-003 | 文案翻译列表页 | /i18n/ui-copy | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-004 | 数据表列表页 | /i18n/content | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-005 | 表字段列表页 | /i18n/content/:tableName | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-006 | 字段翻译详情页 | /i18n/content/:tableName/:fieldName | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-007 | 翻译任务列表页 | /i18n/tasks | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-008 | 配音管理页 | /i18n/audio | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-009 | 翻译接口配置页 | /i18n/translation-api | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-010 | 配音任务列表页 | /i18n/audio/tasks | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-011 | 配音接口配置页 | /i18n/audio/settings | JWT+admin | ROLE-ADMIN |

---

## 2. 接口清单

| API-ID | 方法 | 路径 | 职责(≤10字) | 角色 | R-ID | 详情 |
|--------|------|------|------------|------|------|------|
| API-i18n-dashboard | GET | /api/v1/admin/i18n/dashboard | 翻译总览数据 | JWT+admin | R-i18n-040 | 01 |
| API-i18n-languages-list | GET | /api/v1/admin/i18n/languages | 语言列表 | JWT+admin | R-i18n-001 | 01 |
| API-i18n-languages-update | PATCH | /api/v1/admin/i18n/languages/:id | 更新语言配置 | JWT+admin | R-i18n-002 | 01 |
| API-i18n-languages-reorder | PUT | /api/v1/admin/i18n/languages/order | 排序语言 | JWT+admin | R-i18n-003 | 01 |
| API-i18n-ui-sync | POST | /api/v1/admin/i18n/ui/sync | 同步文案 | JWT+admin | R-i18n-010 | 02 |
| API-i18n-ui-list | GET | /api/v1/admin/i18n/ui/entries | 文案列表 | JWT+admin | R-i18n-011,012,013 | 02 |
| API-i18n-ui-update | PATCH | /api/v1/admin/i18n/ui/translations/:id | 更新文案翻译 | JWT+admin | R-i18n-014 | 02 |
| API-i18n-ui-translate | POST | /api/v1/admin/i18n/ui/translate | 触发文案 AI 翻译 | JWT+admin | R-i18n-015 | 02 |
| API-i18n-ui-publish | POST | /api/v1/admin/i18n/ui/publish | 发布文案翻译 | JWT+admin | R-i18n-016 | 02 |
| API-i18n-tables-list | GET | /api/v1/admin/i18n/content/tables | 数据表列表 | JWT+admin | R-i18n-020 | 03 |
| API-i18n-table-config | PATCH | /api/v1/admin/i18n/content/tables/:tableName | 表级翻译配置 | JWT+admin | R-i18n-021 | 03 |
| API-i18n-fields-list | GET | /api/v1/admin/i18n/content/tables/:tableName/fields | 字段列表 | JWT+admin | R-i18n-022 | 03 |
| API-i18n-field-config | PATCH | /api/v1/admin/i18n/content/tables/:tableName/fields/:fieldName | 字段级翻译配置 | JWT+admin | R-i18n-023 | 03 |
| API-i18n-field-translations | GET | /api/v1/admin/i18n/content/tables/:tableName/fields/:fieldName/translations | 字段翻译列表 | JWT+admin | R-i18n-024,025 | 03 |
| API-i18n-content-update | PATCH | /api/v1/admin/i18n/content/translations/:id | 更新内容翻译 | JWT+admin | R-i18n-026 | 03 |
| API-i18n-content-translate | POST | /api/v1/admin/i18n/content/translate | 触发内容 AI 翻译 | JWT+admin | R-i18n-027 | 03 |
| API-i18n-tasks-list | GET | /api/v1/admin/i18n/tasks | 翻译任务列表 | JWT+admin | R-i18n-030 | 04 |
| API-i18n-task-detail | GET | /api/v1/admin/i18n/tasks/:id | 翻译任务详情 | JWT+admin | R-i18n-031 | 04 |
| API-i18n-task-cancel | POST | /api/v1/admin/i18n/tasks/:id/cancel | 取消翻译任务 | JWT+admin | R-i18n-032 | 04 |
| API-i18n-translation-config-get | GET | /api/v1/admin/i18n/translation-api/config | 翻译接口配置 | JWT+admin | R-i18n-045 | 06 |
| API-i18n-translation-config-save | PUT | /api/v1/admin/i18n/translation-api/config | 保存翻译接口配置 | JWT+admin | R-i18n-045 | 06 |
| API-i18n-translation-test | POST | /api/v1/admin/i18n/translation-api/test | 翻译接口测试 | JWT+admin | R-i18n-046 | 06 |
| API-i18n-audio-switch | PATCH | /api/v1/admin/i18n/audio/switch | 配音模块开关 | JWT+admin | R-i18n-050 | 05 |
| API-i18n-audio-tables-list | GET | /api/v1/admin/i18n/audio/tables | 配音数据表列表 | JWT+admin | R-i18n-051 | 05 |
| API-i18n-audio-table-config | PATCH | /api/v1/admin/i18n/audio/tables/:tableName | 表级配音配置 | JWT+admin | R-i18n-051 | 05 |
| API-i18n-audio-field-config | PATCH | /api/v1/admin/i18n/audio/tables/:tableName/fields/:fieldName | 字段级配音配置 | JWT+admin | R-i18n-052 | 05 |
| API-i18n-audio-generate | POST | /api/v1/admin/i18n/audio/generate | 触发配音生成 | JWT+admin | R-i18n-053 | 05 |
| API-i18n-audio-files-list | GET | /api/v1/admin/i18n/audio/files | 配音文件列表 | JWT+admin | R-i18n-053 | 05 |
| API-i18n-audio-upload | POST | /api/v1/admin/i18n/audio/files/:id/upload | 手动上传配音 | JWT+admin | R-i18n-055 | 05 |
| API-i18n-voice-list | GET | /api/v1/admin/i18n/audio/voices | 音色列表 | JWT+admin | R-i18n-054 | 05 |
| API-i18n-voice-upsert | PUT | /api/v1/admin/i18n/audio/voices/:locale | 配置语言音色 | JWT+admin | R-i18n-054 | 05 |
| API-i18n-voice-delete | DELETE | /api/v1/admin/i18n/audio/voices/:locale | 删除语言音色 | JWT+admin | R-i18n-054 | 05 |
| API-i18n-voice-test | POST | /api/v1/admin/i18n/audio/voices/test | 音色试听测试 | JWT+admin | R-i18n-054 | 05 |
| API-i18n-audio-tasks-list | GET | /api/v1/admin/i18n/audio/tasks | 配音任务列表 | JWT+admin | R-i18n-056 | 05 |
| API-i18n-audio-task-detail | GET | /api/v1/admin/i18n/audio/tasks/:id | 配音任务详情 | JWT+admin | R-i18n-057 | 05 |
| API-i18n-audio-task-cancel | POST | /api/v1/admin/i18n/audio/tasks/:id/cancel | 取消配音任务 | JWT+admin | R-i18n-058 | 05 |
| API-i18n-audio-config-get | GET | /api/v1/admin/i18n/audio/api/config | 配音接口配置 | JWT+admin | R-i18n-060 | 05 |
| API-i18n-audio-config-save | PUT | /api/v1/admin/i18n/audio/api/config | 保存配音接口配置 | JWT+admin | R-i18n-060 | 05 |
| API-i18n-audio-config-test | POST | /api/v1/admin/i18n/audio/api/test | 配音接口测试 | JWT+admin | R-i18n-062 | 05 |

---

## 3. App 端读取接口（公开/用户鉴权）

> app 端无需管理权限，仅读取已发布的翻译内容。

| API-ID | 方法 | 路径 | 职责 | 鉴权 |
|--------|------|------|------|------|
| API-app-i18n-languages | GET | /api/v1/app/i18n/languages | 获取已启用语言列表 | 公开 |
| API-app-i18n-content | GET | /api/v1/app/i18n/content/:tableName/:recordId | 获取记录翻译 | 公开 |

---

## 4. 错误码汇总

| code | HTTP | 含义 | 文案 | 触发接口 |
|------|------|------|------|---------|
| 40001 | 400 | 参数校验失败 | 请检查输入内容 | 所有 |
| 40010 | 400 | 系统默认语言不可停用 | 中文为系统默认语言，不可停用 | languages-update |
| 40011 | 400 | 字段类型不支持翻译 | 该字段类型不支持翻译配置 | field-config |
| 40012 | 400 | 配音前置条件不满足 | 字段未启用翻译或表未启用配音 | audio-field-config, audio-generate |
| 40101 | 401 | 认证失败 | 请重新登录 | 所有 |
| 40301 | 403 | 权限不足 | 无权访问 | 所有 |
| 40401 | 404 | 资源不存在 | 未找到指定资源 | 所有带 :id 参数的接口 |
| 42201 | 422 | 翻译接口配置无效 | 翻译接口连接测试失败 | translation-config-save, translation-test |
| 42202 | 422 | 配音接口配置无效 | 配音接口连接测试失败 | audio-config-save, audio-config-test |
| 50001 | 500 | 内部错误 | 服务异常，请稍后重试 | 所有 |
| 50201 | 502 | AI 翻译接口异常 | 翻译服务暂时不可用 | ui-translate, content-translate |
| 50202 | 502 | TTS 接口异常 | 配音服务暂时不可用 | audio-generate |

---

## 5. 并发与幂等

| API-ID | 并发场景 | 策略 | 失败处理 |
|--------|---------|------|---------|
| API-i18n-ui-sync | 多人同时同步 | 分布式锁，仅一人执行 | 后续请求返回"同步进行中" |
| API-i18n-ui-translate | 重复触发 | 检查是否有进行中的同范围任务 | 返回已有任务信息 |
| API-i18n-content-translate | 同上 | 同上 | 同上 |
| API-i18n-ui-publish | 多人同时发布 | 分布式锁 | 后续请求返回"发布进行中" |
| API-i18n-audio-generate | 重复触发 | 检查是否有进行中的同范围配音任务 | 返回已有任务信息 |

---

## 6. 增量融合报告

### 6.1 本轮新增
新增 40 个 admin 接口 + 2 个 app 读取接口。

---

## 7. 自检报告

**R-ID 覆盖**

| R-ID 范围 | 承接 API-ID |
|-----------|------------|
| R-i18n-001~003 | languages-list, languages-update, languages-reorder |
| R-i18n-010~016 | ui-sync, ui-list, ui-update, ui-translate, ui-publish |
| R-i18n-020~028 | tables-list, table-config, fields-list, field-config, field-translations, content-update, content-translate |
| R-i18n-030~032 | tasks-list, task-detail, task-cancel |
| R-i18n-040 | dashboard |
| R-i18n-045~046 | translation-config-get, translation-config-save, translation-test |
| R-i18n-050~055 | audio-switch, audio-tables-list, audio-table-config, audio-field-config, audio-generate, audio-files-list, voice-list, voice-upsert, voice-delete, voice-test, audio-upload |
| R-i18n-056~058 | audio-tasks-list, audio-task-detail, audio-task-cancel |
| R-i18n-060~062 | audio-config-get, audio-config-save, audio-config-test |

- [x] 每条 R-ID 均有接口承接

---

## 99. 待确认问题

无

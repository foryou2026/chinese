# 接口规范 · translation-hub · 总览

> **系统**：admin
> **关联 R-ID**：R-i18n-001~067
> **不做**：表结构(D01)、页面/原型(C02/C03)
> **特殊说明**：所有接口需 Bearer JWT + role=admin 鉴权。翻译任务与配音任务均为异步执行，通过轮询或 WebSocket 获取进度。
> **接口详情**：01-languages.md ~ 08-tts-providers.md

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
| P-admin-i18n-008 | 配音管理 · 数据表列表 | /i18n/dubbing | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-009 | 翻译接口 · 供应商列表 | /i18n/translation-api | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-010 | 配音任务列表页 | /i18n/dubbing/tasks | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-011 | 配音接口 · 供应商列表 | /i18n/tts-api | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-012 | 翻译接口 · 供应商详情 | /i18n/translation-api/:providerId | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-013 | 配音总览仪表盘 | /i18n/dubbing/overview | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-014 | 配音管理 · 字段列表 | /i18n/dubbing/:tableName | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-015 | 配音管理 · 配音详情 | /i18n/dubbing/:tableName/:fieldName | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-016 | 音色管理页 | /i18n/voices | JWT+admin | ROLE-ADMIN |
| P-admin-i18n-017 | 配音接口 · 供应商详情 | /i18n/tts-api/:providerId | JWT+admin | ROLE-ADMIN |

---

## 2. 接口清单

| API-ID | 方法 | 路径 | 职责(≤10字) | 角色 | R-ID | 详情文件 |
|--------|------|------|------------|------|------|---------|
| API-i18n-dashboard | GET | /api/v1/admin/i18n/dashboard | 翻译总览数据 | JWT+admin | R-i18n-040 | 01 |
| API-i18n-dubbing-dashboard | GET | /api/v1/admin/i18n/dubbing/dashboard | 配音总览数据 | JWT+admin | R-i18n-063 | 01 |
| API-i18n-languages-list | GET | /api/v1/admin/i18n/languages | 语言列表 | JWT+admin | R-i18n-001 | 01 |
| API-i18n-languages-update | PATCH | /api/v1/admin/i18n/languages/:id | 更新语言配置 | JWT+admin | R-i18n-002 | 01 |
| API-i18n-languages-reorder | PUT | /api/v1/admin/i18n/languages/order | 排序语言 | JWT+admin | R-i18n-003 | 01 |
| API-i18n-ui-sync | POST | /api/v1/admin/i18n/ui/sync | 同步文案 | JWT+admin | R-i18n-010 | 02 |
| API-i18n-ui-list | GET | /api/v1/admin/i18n/ui/entries | 文案列表 | JWT+admin | R-i18n-011~013 | 02 |
| API-i18n-ui-update | PATCH | /api/v1/admin/i18n/ui/translations/:id | 更新文案翻译 | JWT+admin | R-i18n-014 | 02 |
| API-i18n-ui-translate | POST | /api/v1/admin/i18n/ui/translate | 触发文案 AI 翻译 | JWT+admin | R-i18n-015,017 | 02 |
| API-i18n-ui-publish | POST | /api/v1/admin/i18n/ui/publish | 发布文案翻译 | JWT+admin | R-i18n-016 | 02 |
| API-i18n-tables-list | GET | /api/v1/admin/i18n/content/tables | 数据表列表 | JWT+admin | R-i18n-020 | 03 |
| API-i18n-table-config | PATCH | /api/v1/admin/i18n/content/tables/:tableName | 表级翻译配置 | JWT+admin | R-i18n-021 | 03 |
| API-i18n-fields-list | GET | /api/v1/admin/i18n/content/tables/:tableName/fields | 字段列表 | JWT+admin | R-i18n-022 | 03 |
| API-i18n-field-config | PATCH | /api/v1/admin/i18n/content/tables/:tableName/fields/:fieldName | 字段级翻译配置 | JWT+admin | R-i18n-023,029 | 03 |
| API-i18n-field-translations | GET | /api/v1/admin/i18n/content/tables/:tableName/fields/:fieldName/translations | 字段翻译列表 | JWT+admin | R-i18n-024,025 | 03 |
| API-i18n-content-update | PATCH | /api/v1/admin/i18n/content/translations/:id | 更新内容翻译 | JWT+admin | R-i18n-026 | 03 |
| API-i18n-content-translate | POST | /api/v1/admin/i18n/content/translate | 触发内容 AI 翻译 | JWT+admin | R-i18n-027 | 03 |
| API-i18n-tasks-list | GET | /api/v1/admin/i18n/tasks | 翻译任务列表 | JWT+admin | R-i18n-030 | 04 |
| API-i18n-task-detail | GET | /api/v1/admin/i18n/tasks/:id | 翻译任务详情 | JWT+admin | R-i18n-031 | 04 |
| API-i18n-task-cancel | POST | /api/v1/admin/i18n/tasks/:id/cancel | 取消翻译任务 | JWT+admin | R-i18n-032 | 04 |
| API-i18n-trans-providers-list | GET | /api/v1/admin/i18n/translation-api/providers | 翻译供应商列表 | JWT+admin | R-i18n-045 | 06 |
| API-i18n-trans-provider-create | POST | /api/v1/admin/i18n/translation-api/providers | 新增翻译供应商 | JWT+admin | R-i18n-045 | 06 |
| API-i18n-trans-provider-get | GET | /api/v1/admin/i18n/translation-api/providers/:id | 翻译供应商详情 | JWT+admin | R-i18n-046 | 06 |
| API-i18n-trans-provider-update | PUT | /api/v1/admin/i18n/translation-api/providers/:id | 更新翻译供应商 | JWT+admin | R-i18n-046 | 06 |
| API-i18n-trans-provider-delete | DELETE | /api/v1/admin/i18n/translation-api/providers/:id | 删除翻译供应商 | JWT+admin | R-i18n-045 | 06 |
| API-i18n-trans-models-list | GET | /api/v1/admin/i18n/translation-api/providers/:id/models | 翻译模型列表 | JWT+admin | R-i18n-046 | 06 |
| API-i18n-trans-model-create | POST | /api/v1/admin/i18n/translation-api/providers/:id/models | 新增翻译模型 | JWT+admin | R-i18n-046 | 06 |
| API-i18n-trans-model-update | PUT | /api/v1/admin/i18n/translation-api/models/:modelId | 更新翻译模型 | JWT+admin | R-i18n-046 | 06 |
| API-i18n-trans-model-delete | DELETE | /api/v1/admin/i18n/translation-api/models/:modelId | 删除翻译模型 | JWT+admin | R-i18n-046 | 06 |
| API-i18n-trans-test | POST | /api/v1/admin/i18n/translation-api/test | 翻译接口测试 | JWT+admin | R-i18n-047 | 06 |
| API-i18n-all-models-list | GET | /api/v1/admin/i18n/translation-api/all-models | 全局翻译模型列表 | JWT+admin | R-i18n-017 | 06 |
| API-i18n-dubbing-switch | PATCH | /api/v1/admin/i18n/dubbing/switch | 配音模块开关 | JWT+admin | R-i18n-050 | 05 |
| API-i18n-dubbing-tables-list | GET | /api/v1/admin/i18n/dubbing/tables | 配音数据表列表 | JWT+admin | R-i18n-051 | 05 |
| API-i18n-dubbing-table-config | PATCH | /api/v1/admin/i18n/dubbing/tables/:tableName | 表级配音配置 | JWT+admin | R-i18n-051 | 05 |
| API-i18n-dubbing-fields-list | GET | /api/v1/admin/i18n/dubbing/tables/:tableName/fields | 配音字段列表 | JWT+admin | R-i18n-052 | 05 |
| API-i18n-dubbing-field-config | PATCH | /api/v1/admin/i18n/dubbing/tables/:tableName/fields/:fieldName | 字段级配音配置 | JWT+admin | R-i18n-053 | 05 |
| API-i18n-dubbing-field-files | GET | /api/v1/admin/i18n/dubbing/tables/:tableName/fields/:fieldName/files | 字段配音文件列表 | JWT+admin | R-i18n-054 | 05 |
| API-i18n-dubbing-generate | POST | /api/v1/admin/i18n/dubbing/generate | 触发配音生成 | JWT+admin | R-i18n-055 | 05 |
| API-i18n-dubbing-upload | POST | /api/v1/admin/i18n/dubbing/files/:id/upload | 手动上传配音 | JWT+admin | R-i18n-054 | 05 |
| API-i18n-voice-list | GET | /api/v1/admin/i18n/voices | 音色列表 | JWT+admin | R-i18n-056 | 07 |
| API-i18n-voice-create | POST | /api/v1/admin/i18n/voices | 新增音色 | JWT+admin | R-i18n-057 | 07 |
| API-i18n-voice-update | PUT | /api/v1/admin/i18n/voices/:id | 更新音色 | JWT+admin | R-i18n-057 | 07 |
| API-i18n-voice-delete | DELETE | /api/v1/admin/i18n/voices/:id | 删除音色 | JWT+admin | R-i18n-057 | 07 |
| API-i18n-voice-test | POST | /api/v1/admin/i18n/voices/test | 音色试听测试 | JWT+admin | R-i18n-058 | 07 |
| API-i18n-dubbing-tasks-list | GET | /api/v1/admin/i18n/dubbing/tasks | 配音任务列表 | JWT+admin | R-i18n-060 | 05 |
| API-i18n-dubbing-task-detail | GET | /api/v1/admin/i18n/dubbing/tasks/:id | 配音任务详情 | JWT+admin | R-i18n-061 | 05 |
| API-i18n-dubbing-task-cancel | POST | /api/v1/admin/i18n/dubbing/tasks/:id/cancel | 取消配音任务 | JWT+admin | R-i18n-062 | 05 |
| API-i18n-tts-providers-list | GET | /api/v1/admin/i18n/tts-api/providers | TTS 供应商列表 | JWT+admin | R-i18n-065 | 08 |
| API-i18n-tts-provider-create | POST | /api/v1/admin/i18n/tts-api/providers | 新增 TTS 供应商 | JWT+admin | R-i18n-065 | 08 |
| API-i18n-tts-provider-get | GET | /api/v1/admin/i18n/tts-api/providers/:id | TTS 供应商详情 | JWT+admin | R-i18n-066 | 08 |
| API-i18n-tts-provider-update | PUT | /api/v1/admin/i18n/tts-api/providers/:id | 更新 TTS 供应商 | JWT+admin | R-i18n-066 | 08 |
| API-i18n-tts-provider-delete | DELETE | /api/v1/admin/i18n/tts-api/providers/:id | 删除 TTS 供应商 | JWT+admin | R-i18n-065 | 08 |
| API-i18n-tts-models-list | GET | /api/v1/admin/i18n/tts-api/providers/:id/models | TTS 音色模型列表 | JWT+admin | R-i18n-066 | 08 |
| API-i18n-tts-model-create | POST | /api/v1/admin/i18n/tts-api/providers/:id/models | 新增 TTS 音色模型 | JWT+admin | R-i18n-066 | 08 |
| API-i18n-tts-model-update | PUT | /api/v1/admin/i18n/tts-api/models/:modelId | 更新 TTS 音色模型 | JWT+admin | R-i18n-066 | 08 |
| API-i18n-tts-model-delete | DELETE | /api/v1/admin/i18n/tts-api/models/:modelId | 删除 TTS 音色模型 | JWT+admin | R-i18n-066 | 08 |
| API-i18n-tts-test | POST | /api/v1/admin/i18n/tts-api/test | TTS 接口测试 | JWT+admin | R-i18n-067 | 08 |
| API-i18n-all-tts-models-list | GET | /api/v1/admin/i18n/tts-api/all-models | 全局音色模型列表 | JWT+admin | R-i18n-055 | 08 |

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
| 40010 | 400 | 受保护语言不可停用 | 该语言为受保护语言（系统默认/枢纽语言），不可停用 | languages-update |
| 40011 | 400 | 字段类型不支持翻译 | 该字段类型不支持翻译配置 | field-config |
| 40012 | 400 | 配音前置条件不满足 | 字段未启用翻译或表未启用配音 | dubbing-field-config, dubbing-generate |
| 40013 | 400 | 翻译模型未配置 | 请先配置翻译接口和模型 | ui-translate, content-translate |
| 40014 | 400 | 音色模型未配置 | 请先配置配音接口和音色模型 | dubbing-generate |
| 40015 | 400 | 供应商有关联数据 | 该供应商有模型正在被使用，无法删除 | provider-delete |
| 40101 | 401 | 认证失败 | 请重新登录 | 所有 |
| 40301 | 403 | 权限不足 | 无权访问 | 所有 |
| 40401 | 404 | 资源不存在 | 未找到指定资源 | 所有带 :id 参数的接口 |
| 42201 | 422 | 翻译接口配置无效 | 翻译接口连接测试失败 | trans-test |
| 42202 | 422 | 配音接口配置无效 | 配音接口连接测试失败 | tts-test |
| 50001 | 500 | 内部错误 | 服务异常，请稍后重试 | 所有 |
| 50201 | 502 | AI 翻译接口异常 | 翻译服务暂时不可用 | ui-translate, content-translate |
| 50202 | 502 | TTS 接口异常 | 配音服务暂时不可用 | dubbing-generate |

---

## 5. 并发与幂等

| API-ID | 并发场景 | 策略 | 失败处理 |
|--------|---------|------|---------|
| API-i18n-ui-sync | 多人同时同步 | 分布式锁，仅一人执行 | 后续请求返回"同步进行中" |
| API-i18n-ui-translate | 重复触发 | 检查是否有进行中的同范围任务 | 返回已有任务信息 |
| API-i18n-content-translate | 同上 | 同上 | 同上 |
| API-i18n-ui-publish | 多人同时发布 | 分布式锁 | 后续请求返回"发布进行中" |
| API-i18n-dubbing-generate | 重复触发 | 检查是否有进行中的同范围配音任务 | 返回已有任务信息 |

---

## 6. 增量融合报告

### 6.1 本轮新增
新增 56 个 admin 接口 + 2 个 app 读取接口。

---

## 7. 自检报告

**R-ID 覆盖**

| R-ID 范围 | 承接 API-ID |
|-----------|------------|
| R-i18n-001~003 | languages-list, languages-update, languages-reorder |
| R-i18n-010~017 | ui-sync, ui-list, ui-update, ui-translate, ui-publish, all-models-list |
| R-i18n-020~029 | tables-list, table-config, fields-list, field-config, field-translations, content-update, content-translate |
| R-i18n-030~032 | tasks-list, task-detail, task-cancel |
| R-i18n-040 | dashboard |
| R-i18n-045~047 | trans-providers-list/create/get/update/delete, trans-models-list/create/update/delete, trans-test |
| R-i18n-050~055 | dubbing-switch, dubbing-tables-list, dubbing-table-config, dubbing-fields-list, dubbing-field-config, dubbing-field-files, dubbing-generate, dubbing-upload |
| R-i18n-056~058 | voice-list, voice-create, voice-update, voice-delete, voice-test |
| R-i18n-060~062 | dubbing-tasks-list, dubbing-task-detail, dubbing-task-cancel |
| R-i18n-063 | dubbing-dashboard |
| R-i18n-065~067 | tts-providers-list/create/get/update/delete, tts-models-list/create/update/delete, tts-test |

- [x] 每条 R-ID 均有接口承接

---

## 99. 待确认问题

无

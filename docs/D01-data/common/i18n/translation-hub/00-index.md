# 数据规范 · translation-hub · 共用总览

> **适用系统**：admin, app
> **关联 R-ID**：R-i18n-001~053
> **不做**：状态机定义(C02)、路由/接口(D02)、页面(C03)
> **特殊说明**：i18n 模块为通用框架级设计，所有表均在 `public` 域下。数据库内容翻译通过独立翻译表实现，不修改业务表 schema。
> **实体清单**：01-i18n-languages ~ 07-i18n-audio-files
> **枚举清单**：enums.md

---

## 1. ER 图

```mermaid
erDiagram
    I18N_LANGUAGES {
        uuid id PK
        text locale_code UK
        boolean is_active
        int sort_order
    }
    I18N_TABLE_CONFIG {
        uuid id PK
        text table_name UK
        boolean translation_enabled
        text default_source_locale
    }
    I18N_FIELD_CONFIG {
        uuid id PK
        text table_name
        text field_name
        boolean needs_translation
        text source_locale
        boolean needs_audio
    }
    I18N_UI_ENTRIES {
        uuid id PK
        text key_path UK
        text source_text_zh
        text namespace
    }
    I18N_UI_TRANSLATIONS {
        uuid id PK
        uuid entry_id FK
        text locale
        text translated_text
        text status
    }
    I18N_CONTENT_TRANSLATIONS {
        uuid id PK
        text table_name
        uuid record_id
        text field_name
        text locale
        text translated_text
        text status
    }
    I18N_AUDIO_CONFIG {
        uuid id PK
        text locale
        text api_type
        text api_endpoint
    }
    I18N_AUDIO_FILES {
        uuid id PK
        text table_name
        uuid record_id
        text field_name
        text locale
        text audio_url
    }
    I18N_TRANSLATION_TASKS {
        uuid id PK
        text task_type
        text scope
        text status
        int total_items
        int completed_items
    }

    I18N_TABLE_CONFIG ||--o{ I18N_FIELD_CONFIG : "1:N (table_name)"
    I18N_FIELD_CONFIG ||--o{ I18N_CONTENT_TRANSLATIONS : "逻辑关联"
    I18N_UI_ENTRIES ||--o{ I18N_UI_TRANSLATIONS : "1:N"
    I18N_LANGUAGES ||--o{ I18N_UI_TRANSLATIONS : "locale"
    I18N_LANGUAGES ||--o{ I18N_CONTENT_TRANSLATIONS : "locale"
    I18N_LANGUAGES ||--o{ I18N_AUDIO_CONFIG : "locale"
    I18N_LANGUAGES ||--o{ I18N_AUDIO_FILES : "locale"
    I18N_CONTENT_TRANSLATIONS ||--o{ I18N_AUDIO_FILES : "逻辑关联"
```

---

## 2. 业务规则与校验

| BR-ID | 来源 R-ID | 涉及实体/字段 | 描述(一句) | 实现层 |
|-------|-----------|---------------|-----------|--------|
| BR-i18n-001 | R-i18n-002 | i18n_languages.locale_code='zh' | 中文不可停用 | Application + DB CHECK |
| BR-i18n-002 | R-i18n-015/027 | — | 翻译链 zh→en→其他 | Service |
| BR-i18n-003 | R-i18n-023 | i18n_field_config | 字段级配置优先于表级 | Service |
| BR-i18n-004 | R-i18n-028 | i18n_content_translations.status | 源文变更自动标记 outdated | Trigger/Service |
| BR-i18n-005 | R-i18n-014/015 | i18n_ui_translations.status | AI→translated, 手动→reviewed | Service |
| BR-i18n-006 | R-i18n-032 | i18n_translation_tasks | 取消后已完成部分保留 | Service |
| BR-i18n-007 | R-i18n-050 | i18n_field_config.needs_audio | 配音独立于翻译 | Application |
| BR-i18n-008 | R-i18n-050 | i18n_field_config.needs_audio | 配音字段级>表级 | Service |

---

## 3. 索引策略

| IDX-ID | 表 | 字段 | 类型 | 唯一 | 支撑查询 |
|--------|-----|------|------|------|---------|
| uniq_languages_locale | i18n_languages | (locale_code) | btree | 是 | 按 locale 查语言 |
| uniq_table_config | i18n_table_config | (table_name) | btree | 是 | 按表名查配置 |
| uniq_field_config | i18n_field_config | (table_name, field_name) | btree | 是 | 按表+字段查配置 |
| uniq_ui_entry_key | i18n_ui_entries | (key_path) | btree | 是 | 按 key 查文案 |
| uniq_ui_trans | i18n_ui_translations | (entry_id, locale) | btree | 是 | 按条目+语言查翻译 |
| idx_ui_trans_status | i18n_ui_translations | (locale, status) | btree | 否 | 按语言+状态统计 |
| uniq_content_trans | i18n_content_translations | (table_name, record_id, field_name, locale) | btree | 是 | 查指定记录字段翻译 |
| idx_content_trans_table | i18n_content_translations | (table_name, field_name, locale, status) | btree | 否 | 按表+字段+语言+状态筛选 |
| uniq_audio_file | i18n_audio_files | (table_name, record_id, field_name, locale) | btree | 是 | 查指定记录字段配音 |
| idx_tasks_status | i18n_translation_tasks | (status, created_at) | btree | 否 | 任务列表筛选 |

---

## 4. 种子数据

| 表 | 用途 | 示例 | 写入时机 |
|-----|------|------|---------|
| i18n_languages | 预置全球主流语言 | 约 50 条，zh/en/vi/th/... | 首次部署 |

---

## 5. 增量融合报告

### 5.1 本轮新增摘要
新建 9 张表：i18n_languages, i18n_table_config, i18n_field_config, i18n_ui_entries, i18n_ui_translations, i18n_content_translations, i18n_translation_tasks, i18n_audio_config, i18n_audio_files。定义 3 个枚举类型。

### 5.2 融合点 / 冲突点 / 已有变更
- 与 auth 模块无数据耦合
- i18n_content_translations 通过 (table_name, record_id) 逻辑关联任意业务表，无物理外键

---

## 6. 自检报告

**完整性 — R-ID 覆盖对照**

| R-ID 范围 | 承接实体/规则 |
|-----------|-------------|
| R-i18n-001~003 语言管理 | i18n_languages |
| R-i18n-010~016 UI 文案 | i18n_ui_entries + i18n_ui_translations |
| R-i18n-020~028 数据库内容 | i18n_table_config + i18n_field_config + i18n_content_translations |
| R-i18n-030~032 翻译任务 | i18n_translation_tasks |
| R-i18n-040 翻译总览 | 聚合查询，无独立表 |
| R-i18n-050~053 配音 | i18n_audio_config + i18n_audio_files |

- [x] 每条 R-ID 均有实体或规则承接
- [x] 外键/逻辑关联明确
- [x] 主键统一 uuid
- [x] 索引覆盖主查询路径

---

## 99. 待确认问题

无

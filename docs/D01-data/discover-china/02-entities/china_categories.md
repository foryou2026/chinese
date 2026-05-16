<!-- TARGET-PATH: docs/D01-data/discover-china/02-entities/china_categories.md -->

# 实体:`zhiyu.china_categories`

> **性质**:系统内置数据字典,12 条固定;迁移种子写入;前端禁止 CRUD;不启用软删。

## 字段

| 字段 | 类型 | 必填 | 默认 | 索引 | 业务含义 |
|------|------|:--:|------|------|---------|
| `id` | uuid | ✅ | `gen_random_uuid()` | PK | — |
| `code` | text | ✅ | — | UNIQUE | 类目编码 01..12 |
| `name_i18n` | jsonb | ✅ | — | — | 5 语类目名 `{zh,en,vi,th,id}` |
| `description_i18n` | jsonb | ✅ | — | — | 5 语类目介绍 |
| `sort_order` | int | ✅ | `code::int` | idx | 排序键 |
| `created_at` | timestamptz | ✅ | `now()` | — | — |
| `updated_at` | timestamptz | ✅ | `now()` | — | 触发器维护 |

## DDL

```sql
create table zhiyu.china_categories (
  id          uuid primary key default gen_random_uuid(),
  code        text not null,
  name_i18n   jsonb not null,
  description_i18n jsonb not null,
  sort_order  int  not null,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),

  constraint uq_china_categories_code unique (code),
  constraint ck_china_categories_code_format
    check (code ~ '^(0[1-9]|1[0-2])$'),
  constraint ck_china_categories_name_i18n_keys
    check (name_i18n ?& array['zh','en','vi','th','id']),
  constraint ck_china_categories_desc_i18n_keys
    check (description_i18n ?& array['zh','en','vi','th','id'])
);

create index idx_china_categories_sort_order
  on zhiyu.china_categories (sort_order);

create trigger tg_china_categories_before_update_set_updated_at
  before update on zhiyu.china_categories
  for each row execute function zhiyu.set_updated_at();
```

## RLS

| 操作 | 角色 | 策略 |
|------|------|------|
| select | `anon` + `authenticated` | 全部放行(公开字典) |
| insert / update / delete | `service_role` | 仅 service-role |

策略:`china_categories_select_public`、`china_categories_write_service`。

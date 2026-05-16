<!-- TARGET-PATH: docs/D01-data/discover-china/02-entities/china_articles.md -->

# 实体:`zhiyu.china_articles`

> **性质**:管理端 CRUD 内容表;软删 30 天;状态机 `draft / published`。

## 字段

| 字段 | 类型 | 必填 | 默认 | 索引 | 业务含义 |
|------|------|:--:|------|------|---------|
| `id` | uuid | ✅ | `gen_random_uuid()` | PK | — |
| `code` | text | ✅ | `fn_gen_article_code()` | UNIQUE WHERE deleted_at IS NULL | 12 位文章编码 |
| `category_id` | uuid | ✅ | — | idx | FK → categories.id, RESTRICT |
| `title_pinyin` | text | ✅ | — | — | 拼音标题 1–200 |
| `title_i18n` | jsonb | ✅ | — | — | 5 语标题,每语 1–40 |
| `status` | text | ✅ | `'draft'` | idx | `draft \| published` |
| `published_at` | timestamptz | ❌ | null | idx | `published` 时必有,`draft` 时必空 |
| `created_by` | uuid | ❌ | — | idx | FK → auth.users.id, SET NULL |
| `updated_by` | uuid | ❌ | — | — | 同上 |
| `created_at` | timestamptz | ✅ | `now()` | — | — |
| `updated_at` | timestamptz | ✅ | `now()` | — | 触发器 |
| `deleted_at` | timestamptz | ❌ | null | idx | 软删 |

## DDL

```sql
create table zhiyu.china_articles (
  id           uuid primary key default gen_random_uuid(),
  code         text not null,
  category_id  uuid not null,
  title_pinyin text not null,
  title_i18n   jsonb not null,
  status       text not null default 'draft',
  published_at timestamptz,
  created_by   uuid,
  updated_by   uuid,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  deleted_at   timestamptz,

  constraint fk_china_articles_category_id
    foreign key (category_id) references zhiyu.china_categories(id) on delete restrict,
  constraint fk_china_articles_created_by
    foreign key (created_by) references auth.users(id) on delete set null,
  constraint fk_china_articles_updated_by
    foreign key (updated_by) references auth.users(id) on delete set null,

  constraint ck_china_articles_code_format
    check (code ~ '^[A-Z0-9]{12}$'),
  constraint ck_china_articles_status
    check (status in ('draft','published')),
  constraint ck_china_articles_title_pinyin_len
    check (char_length(title_pinyin) between 1 and 200),
  constraint ck_china_articles_title_i18n_keys
    check (title_i18n ?& array['zh','en','vi','th','id']),
  constraint ck_china_articles_published_at_consistency
    check (
      (status = 'published' and published_at is not null) or
      (status = 'draft'     and published_at is null)
    )
);

create unique index uq_china_articles_code
  on zhiyu.china_articles (code) where deleted_at is null;
create index idx_china_articles_category_id  on zhiyu.china_articles (category_id) where deleted_at is null;
create index idx_china_articles_status       on zhiyu.china_articles (status)      where deleted_at is null;
create index idx_china_articles_published_at on zhiyu.china_articles (published_at desc) where status = 'published' and deleted_at is null;
create index idx_china_articles_created_by   on zhiyu.china_articles (created_by);
create index idx_china_articles_deleted_at   on zhiyu.china_articles (deleted_at);

create trigger tg_china_articles_before_update_set_updated_at
  before update on zhiyu.china_articles
  for each row execute function zhiyu.set_updated_at();
```

## RLS

| 操作 | 角色 | 策略 |
|------|------|------|
| select | `anon` + `authenticated` | 仅 `status='published' AND deleted_at IS NULL` |
| select | `service_role` | 全量 |
| insert / update / delete | `service_role` | 全量(管理端走 service-role) |

策略:`china_articles_select_published`、`china_articles_write_service`。

## 状态机详见 [`../03-business-rules.md §1`](../03-business-rules.md)

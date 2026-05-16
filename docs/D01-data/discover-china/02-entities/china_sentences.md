<!-- TARGET-PATH: docs/D01-data/discover-china/02-entities/china_sentences.md -->

# 实体:`zhiyu.china_sentences`

> **性质**:文章 1..N 条句子;按性能 5 语内容拆为独立列;中文 TTS 异步生成。

## 字段

| 字段 | 类型 | 必填 | 默认 | 索引 | 业务含义 |
|------|------|:--:|------|------|---------|
| `id` | uuid | ✅ | `gen_random_uuid()` | PK | — |
| `article_id` | uuid | ✅ | — | idx | FK → articles.id, CASCADE |
| `seq_no` | int | ✅ | `fn_next_sentence_seq()` | UNIQUE (article_id, seq_no) | 1..9999;UI 4 位补零 |
| `pinyin` | text | ✅ | — | — | 1–600 |
| `content_zh` | text | ✅ | — | — | 1–400 |
| `content_en` | text | ✅ | — | — | 1–400 |
| `content_vi` | text | ✅ | — | — | 1–400 |
| `content_th` | text | ✅ | — | — | 1–400 |
| `content_id` | text | ✅ | — | — | 1–400 (id = 印尼语 BCP-47 代码,非主键) |
| `audio_url_zh` | text | ❌ | null | — | Storage URL,`audio_status='ready'` 时必有 |
| `audio_status` | text | ✅ | `'pending'` | idx | `pending \| processing \| ready \| failed` |
| `audio_provider` | text | ❌ | — | — | TTS 厂商 `azure / aliyun / mock` |
| `audio_voice` | text | ❌ | — | — | 音色 ID |
| `audio_duration_ms` | int | ❌ | — | — | 时长,前端进度条用 |
| `audio_generated_at` | timestamptz | ❌ | — | — | TTS 完成时间 |
| `audio_error` | text | ❌ | — | — | 最近一次失败原因 |
| `created_at / updated_at / deleted_at` | timestamptz | — | — | idx(deleted_at) | 时间字段 |

## DDL

```sql
create table zhiyu.china_sentences (
  id                 uuid primary key default gen_random_uuid(),
  article_id         uuid not null,
  seq_no             int  not null,
  pinyin             text not null,
  content_zh         text not null,
  content_en         text not null,
  content_vi         text not null,
  content_th         text not null,
  content_id         text not null,
  audio_url_zh       text,
  audio_status       text not null default 'pending',
  audio_provider     text,
  audio_voice        text,
  audio_duration_ms  int,
  audio_generated_at timestamptz,
  audio_error        text,
  created_at         timestamptz not null default now(),
  updated_at         timestamptz not null default now(),
  deleted_at         timestamptz,

  constraint fk_china_sentences_article_id
    foreign key (article_id) references zhiyu.china_articles(id) on delete cascade,

  constraint ck_china_sentences_seq_no_range  check (seq_no between 1 and 9999),
  constraint ck_china_sentences_audio_status
    check (audio_status in ('pending','processing','ready','failed')),
  constraint ck_china_sentences_pinyin_len     check (char_length(pinyin) between 1 and 600),
  constraint ck_china_sentences_content_zh_len check (char_length(content_zh) between 1 and 400),
  constraint ck_china_sentences_content_en_len check (char_length(content_en) between 1 and 400),
  constraint ck_china_sentences_content_vi_len check (char_length(content_vi) between 1 and 400),
  constraint ck_china_sentences_content_th_len check (char_length(content_th) between 1 and 400),
  constraint ck_china_sentences_content_id_len check (char_length(content_id) between 1 and 400),
  constraint ck_china_sentences_audio_url_when_ready
    check (audio_status <> 'ready' or audio_url_zh is not null)
);

create unique index uq_china_sentences_article_seq
  on zhiyu.china_sentences (article_id, seq_no) where deleted_at is null;
create index idx_china_sentences_article_id   on zhiyu.china_sentences (article_id) where deleted_at is null;
create index idx_china_sentences_audio_status on zhiyu.china_sentences (audio_status) where audio_status in ('pending','processing','failed');
create index idx_china_sentences_deleted_at   on zhiyu.china_sentences (deleted_at);

create trigger tg_china_sentences_before_update_set_updated_at
  before update on zhiyu.china_sentences
  for each row execute function zhiyu.set_updated_at();
```

## RLS

| 操作 | 角色 | 策略 |
|------|------|------|
| select | `anon` + `authenticated` | 句子所属文章 `status='published' AND deleted_at IS NULL` |
| select | `service_role` | 全量 |
| insert / update / delete | `service_role` | 全量 |

```sql
create policy china_sentences_select_published on zhiyu.china_sentences
  for select to anon, authenticated
  using (
    deleted_at is null and exists (
      select 1 from zhiyu.china_articles a
      where a.id = china_sentences.article_id
        and a.status = 'published'
        and a.deleted_at is null
    )
  );
```

## TTS 缓存键

- Storage 路径:`china-tts/{article_code}/{seq_no_padded}.mp3`(示例 `china-tts/A7K2P9X3M4QR/0003.mp3`);
- 缓存键由 `(article_code, seq_no)` 决定,不是句子 UUID;
- seq_no 重排会清空 `audio_url_zh` 并重置 `audio_status='pending'`(详 [`../05-calculations.md`](../05-calculations.md));
- 孤儿音频文件由 cron `cron_china_purge_orphan_audio` 每周扫描清理。

<!-- TARGET-PATH: docs/D01-data/discover-china/05-calculations.md -->

# 05 · RPC 函数(编号 / 状态 / 重排)

> 所有 RPC `SECURITY DEFINER`,内部按需调用 `auth.uid()` 校验角色;
> 命名前缀 `fn_`。

## 1. `fn_gen_article_code()` — 12 位文章编码

字符集 `ABCDEFGHJKLMNPQRSTUVWXYZ23456789`(32 字符,去除易混淆 I/O/0/1)。

```sql
create or replace function zhiyu.fn_gen_article_code()
returns text language plpgsql as $$
declare
  alphabet constant text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  v_code text;
  v_attempts int := 0;
begin
  loop
    v_code := '';
    for i in 1..12 loop
      v_code := v_code || substr(alphabet, 1 + floor(random() * 32)::int, 1);
    end loop;
    perform 1 from zhiyu.china_articles where code = v_code;
    if not found then return v_code; end if;
    v_attempts := v_attempts + 1;
    if v_attempts >= 5 then raise exception 'CHINA_ARTICLE_CODE_GEN_FAILED'; end if;
  end loop;
end;
$$;
```

碰撞概率:32^12 ≈ 1.15×10^18,实际不可能;5 次重试为防御性。

## 2. `fn_next_sentence_seq(p_article_id uuid)` — 句子下一号

```sql
create or replace function zhiyu.fn_next_sentence_seq(p_article_id uuid)
returns int language plpgsql as $$
declare v_next int;
begin
  perform 1 from zhiyu.china_articles where id = p_article_id for update;
  select coalesce(max(seq_no), 0) + 1 into v_next
    from zhiyu.china_sentences where article_id = p_article_id;
  if v_next > 9999 then raise exception 'CHINA_SENTENCE_SEQ_OVERFLOW'; end if;
  return v_next;
end;
$$;
```

## 3. `fn_resequence_sentences(p_article_id uuid)` — 重排 + 失效 TTS

```sql
create or replace function zhiyu.fn_resequence_sentences(p_article_id uuid)
returns void language plpgsql as $$
declare v_row record; v_new int := 0;
begin
  perform 1 from zhiyu.china_articles where id = p_article_id for update;

  -- 临时偏移,绕开 (article_id, seq_no) 唯一约束
  update zhiyu.china_sentences
     set seq_no = seq_no + 100000
   where article_id = p_article_id and deleted_at is null;

  for v_row in
    select id from zhiyu.china_sentences
     where article_id = p_article_id and deleted_at is null
     order by seq_no asc
  loop
    v_new := v_new + 1;
    update zhiyu.china_sentences
       set seq_no             = v_new,
           audio_url_zh       = null,
           audio_status       = 'pending',
           audio_provider     = null,
           audio_voice        = null,
           audio_duration_ms  = null,
           audio_generated_at = null,
           audio_error        = null
     where id = v_row.id;
  end loop;
end;
$$;
```

> seq_no 变化 → TTS 缓存键(`{article_code}-{seq_no}`)失效,必须清空音频字段。旧 mp3 暂留 Storage,由周扫描 cron `cron_china_purge_orphan_audio` 清理。

## 4. `fn_publish_article(p_article_id uuid)` / `fn_unpublish_article` — 状态转换

伪代码:

```
fn_publish_article(p_id):
  for update lock china_articles row
  assert role = 'super_admin'
  assert status = 'draft'
  assert title_i18n keys = 5
  count = (select count from china_sentences where article_id=p_id and deleted_at is null)
  assert count >= 1
  for each sentence:
    assert content_<lang> not null for lang in [zh,en,vi,th,id]
  update status='published', published_at=now(), updated_by=auth.uid()
  insert audit_log
  pg_notify('china_article_published', p_id::text)  -- 缓存失效
  return row

fn_unpublish_article(p_id):
  for update
  assert role = 'super_admin'
  assert status = 'published'
  update status='draft', published_at=null, updated_by=auth.uid()
  perform fn_clear_progress_by_article(p_id)  -- 跨域,事务内
  pg_notify('china_article_unpublished', p_id::text)
  return row
```

## 5. `fn_insert_sentence_at` / `fn_delete_sentence` / `fn_reorder_sentences`

- `fn_insert_sentence_at(p_article_id, p_position text, p_after_seq int, p_payload jsonb)`:
  - `position='end'`:`seq_no = fn_next_sentence_seq()`,**不调** `fn_clear_progress_by_article`;
  - `position='start'` 或 `'after'`:先插末尾,然后 `fn_resequence_sentences` 整理顺序,**调用** `fn_clear_progress_by_article`;
- `fn_delete_sentence(p_id)`:软删 → `fn_resequence_sentences` → `fn_clear_progress_by_article`;
- `fn_reorder_sentences(p_article_id, p_ordered_ids uuid[])`:按列表顺序重写 seq_no → 全部 audio 字段清空 → `fn_clear_progress_by_article`。

## 6. cron 任务

| 名称 | 频率 | 动作 |
|------|------|------|
| `cron_china_purge_soft_deleted` | daily 03:00 | 物理删除 30 天前软删的文章 + 句子;CASCADE |
| `cron_china_purge_orphan_audio` | weekly | 扫描 Storage `china-tts/`,比对 DB `audio_url_zh`,删孤儿 |

<!-- TARGET-PATH: docs/D01-data/course/08-seed-data.md -->

# 08 · 种子数据 · course

> 直读 F1:[11-种子数据.md](../../../../function/02-course/ai/F1-AI-数据模型规范/11-种子数据.md)。

## 8.1 执行顺序

```
1. course_tracks      (5 行,固定)
2. course_stages      (25 行)
3. course_media_assets(1 行占位静音音频,hash 去重示例)
4. (可选) course_chapters / lessons / kp / question — 示例数据,e2e 冒烟用
5. course_exams      (1 套示例,e2e 用)
```

## 8.2 主题(`course_tracks`)

| code | name_zh | sort_order |
|------|---------|-----------|
| share | 拼音基础 | 0 |
| ec | 电商客服 | 1 |
| fc | 工厂沟通 | 2 |
| hsk | HSK | 3 |
| dl | 日常生活 | 4 |

```sql
INSERT INTO zhiyu.course_tracks (code, name_zh, name_i18n, sort_order, is_enabled)
VALUES
  ('share','拼音基础','{"zh":"拼音基础","en":"Pinyin Basics","vi":"Phát âm cơ bản","th":"พื้นฐานพินอิน","id":"Dasar Pinyin"}',0,true),
  ('ec','电商客服','{"zh":"电商客服","en":"E-commerce CS","vi":"Chăm sóc TMĐT","th":"บริการอีคอมเมิร์ซ","id":"Layanan E-commerce"}',1,true),
  ('fc','工厂沟通','{"zh":"工厂沟通","en":"Factory Comms","vi":"Giao tiếp nhà máy","th":"การสื่อสารโรงงาน","id":"Komunikasi Pabrik"}',2,true),
  ('hsk','HSK','{"zh":"HSK","en":"HSK","vi":"HSK","th":"HSK","id":"HSK"}',3,true),
  ('dl','日常生活','{"zh":"日常生活","en":"Daily Life","vi":"Đời sống","th":"ชีวิตประจำวัน","id":"Kehidupan Harian"}',4,true)
ON CONFLICT (code) DO NOTHING;
```

## 8.3 阶段(`course_stages`)

| track | stage_no | 数量 | hsk_mapping |
|-------|----------|------|-------------|
| share | 0 | 1 | — |
| ec | 1–6 | 6 | — |
| fc | 1–6 | 6 | — |
| hsk | 1–6 | 6 | HSK1–6 |
| dl | 1–6 | 6 | — |

每阶段 `title_i18n / desc_i18n` 由运营录入,seed 给中文 + 4 语翻译占位(可后续覆盖)。

## 8.4 媒资占位

```sql
INSERT INTO zhiyu.course_media_assets
  (id, kind, url, hash, meta, source, voice_profile)
VALUES
  (gen_random_uuid(),
   'audio',
   'https://cdn.zhiyu.local/seed/silence-1s.mp3',
   '0000000000000000000000000000000000000000000000000000000000000000',
   '{"duration_ms":1000,"bitrate_kbps":128,"format":"mp3"}',
   'tts',
   'xiaoxiao_zh')
ON CONFLICT (hash) DO NOTHING;
```

## 8.5 管理员

- `super` 管理员账号通过 [account 域 seed](../../D01-data/discover-china/08-seed-data.md) 创建一次(`auth.users + auth_admin_profiles`);
- 本域不重复 seed。

## 8.6 序列初值

```sql
-- 35 个 KP sequence(示例,实际由 migration 自动 CREATE)
CREATE SEQUENCE IF NOT EXISTS zhiyu.seq_course_kp_share_p START 1;
-- ... 略 (共 5 主题 × 7 类型 = 35)

-- 5 个 Question sequence
CREATE SEQUENCE IF NOT EXISTS zhiyu.seq_course_q_share START 1;
-- ... 略 (共 5 个)
```

## 8.7 e2e 冒烟示例(可选,生产不上)

- 1 个 chapter `share/0/1`、1 个 lesson `share-0-1-1`「ma 的四声」、12 个 KP、24 道题、1 套节末小测;
- 通过 fixture seed 单独维护:`system/scripts/db/seed-course-smoke.ts`。

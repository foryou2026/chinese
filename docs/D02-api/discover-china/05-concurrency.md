<!-- TARGET-PATH: docs/D02-api/discover-china/05-concurrency.md -->

# 05 · 并发与冲突

> 来源 F2 §四 PM 决策:"以最后保存为准"。
> 详见 [F2-08](../../../../function/01-china/ai/F2-AI-接口规范/08-并发与冲突处理.md)。

## 1. 文章基本信息编辑(A5) — Last Writer Wins

- 后端无版本号、不返 409,按到达顺序覆盖;
- 前端打开编辑页记录 `loaded_updated_at`;保存响应里返回新 `updated_at` + `updated_by`;
- 若 `response.updated_at > loaded_updated_at` 且 `updated_by != self` → 前端 toast 提示「该文章在你编辑期间被 {display_name} 修改过,已覆盖」;
- 不锁文章,符合 PM 决策。

## 2. 句子编辑(A12)

同 A5;`content_zh` 改动时清音频缓存(单事务,无并发问题)。

## 3. 句子重排 / 删除 / 插入(A11 / A13 / A14) — 串行化

- 所有 RPC 在事务内对所属 `china_articles` 行 `FOR UPDATE`;
- 第二个并发请求等待第一个事务提交,不会丢失;
- 极端长事务 → statement_timeout 30s → 504,前端提示稍后重试。

## 4. 用户 TTS 触发(C4) vs 管理员编辑 zh(A12)

- A12 改 content_zh 时 SET `audio_url_zh=null, audio_status='pending'`;
- C4 处于 processing 时,A12 等待 C4 完成(行锁);C4 写 ready 后 A12 立即覆盖回 pending,旧 mp3 残留由 cron `cron_china_purge_orphan_audio` 清理;
- 用户拿到旧 mp3 播放完即丢,无害。

## 5. 发布(A6) vs 删除(A8) 并发

- 同行锁;后到者发现状态不符 → 409 `CHINA_ARTICLE_STATUS_CONFLICT`。

## 6. 限流与防重复

| 场景 | 防护 |
|------|------|
| C4 同 IP 频繁触发 TTS | 20 / min IP 限流 + 行锁 + `Idempotency-Key` 头(可选) |
| A14 批量重排 | service-role 单管理员场景,不额外限流 |
| 通用写接口 | 120 r/min(按用户) |
| A15 全局搜索 | 30 r/min(按用户) |

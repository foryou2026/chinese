<!-- TARGET-PATH: docs/D02-api/discover-china/app/03-endpoints/02-app-tts.md -->

# 应用端 · TTS 触发与朗读(C4 / AUX)

> 详情见 [F2-02](../../../../function/01-china/ai/F2-AI-接口规范/02-应用端-TTS与朗读.md)。

## 设计原则(PM 答 Q10)

- 用户点击触发,后端不预生成、不自动重试;
- 全平台共享永久缓存,首位用户触发后所有用户命中;
- 失败不限次重试由用户再次点击;
- 上游 TTS 在 dev / 未配密钥环境走 mock adapter(`packages/ai-adapters/tts/mock.ts`)。

## OP-C4 · POST `/api/v1/china/sentences/:id/audio`

| 项 | 内容 |
|----|------|
| 权限 | 公开(IP 限流 20/min,缓存命中不计) |
| 入参 | path `id`(uuid);body `{voice?}`;header `Idempotency-Key?` |
| 业务校验 | 句子存在 + 所属文章 published 未删 → 否则 404 |

### 状态机响应

| 当前 `audio_status` | 行为 | HTTP |
|--------------------|------|------|
| `ready` | 直接返回缓存 | 200,`from_cache=true` |
| `pending` | CAS 抢占 → `processing` → 同步调上游 → 上传 Storage → 写 `ready` | 200 |
| `processing`(他人占用) | 同步轮询 ≤ 30s,仍未完成 → 202 | 200 / 202 |
| `failed` | 与 `pending` 同流程 | 200 / 502 |

### 响应

- 200 `data.audio{status,url,duration_ms,provider,voice,generated_at,from_cache}`;
- 202 `{code:20200, data.audio.status:'processing'}` — 前端走 AUX 轮询;
- 502 `CHINA_TTS_UPSTREAM_FAILED`;504 `CHINA_TTS_UPSTREAM_TIMEOUT`(上游超时 15s);
- 429 `CHINA_TTS_RATE_LIMITED`。

### 失败副作用

`audio_status='failed'` + `audio_error=<原因>`;用户点击立即重试,无次数限制。

### 来源需求

C01 R-004,R-006,R-018。

## OP-AUX · GET `/api/v1/china/sentences/:id/audio`

| 项 | 内容 |
|----|------|
| 权限 | 公开(IP 30 / min) |
| 用途 | C4 返回 202 后前端短轮询;不写库 |
| 出参 | `audio.status` ∈ `pending\|processing\|ready\|failed`;`ready` 时附 `url` |

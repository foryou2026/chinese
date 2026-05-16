<!-- TARGET-PATH: docs/D02-api/discover-china/03-endpoints/08-internal.md -->

# 内部接口(I1 / I2)

> 详见 [F2-07](../../../../function/01-china/ai/F2-AI-接口规范/07-AI补充接口.md)。

## OP-I1 · POST `/internal/v1/china/tts/callback`

| 项 | 内容 |
|----|------|
| 权限 | 仅 service-role;nginx 不暴露公网 |
| 用途 | dev / mock 环境异步回调写回 `audio_url_zh` + `audio_status='ready'`(生产真实 TTS 同步返回,不走此接口) |
| body | `{sentence_id, audio_url, duration_ms, provider, voice}` |
| 错误 | 401 / 404 / 409(状态不允许) |

> 与 zhiyu-docker-policy 一致:本地 Docker 验证时,`TTS_PROVIDER=mock` 启用 fake adapter,走 I1。

## OP-I2 · GET `/api/v1/china/health`

| 项 | 内容 |
|----|------|
| 权限 | 公开 |
| 用途 | 容器探活 / 监控 |
| 出参 | `{service:'china', uptime_s, tts_adapter}` |

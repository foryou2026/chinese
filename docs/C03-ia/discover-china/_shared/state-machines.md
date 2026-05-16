<!-- TARGET-PATH: docs/C03-ia/discover-china/_shared/state-machines.md -->

# 03 · 状态机

## SM-discover-china-01 · 文章发布状态


| 状态 | 应用端可见 | 管理端可编辑 |
|------|----------|-------------|
| `draft` | 否 | 是 |
| `published` | 是 | 是 |

## SM-discover-china-02 · 句子 TTS 音频生成

句子级 TTS 音频对象的服务端生成与缓存状态（数据源 `tts_audio.status`）。

```
none ──request_tts──▶ queued ──worker_pick──▶ generating
generating ──synth_ok──▶ ready
generating ──synth_fail──▶ failed ──retry(≤3)──▶ queued
failed ──manual_retry──▶ queued
ready ──content_edit──▶ stale ──auto_invalidate──▶ none
```

- `ready` 命中即直返 CDN URL，不再合成；
- `failed` 终态需管理端主动重试或编辑句子；
- `stale` 仅作过渡，由清理 job 物理删除。

## SM-discover-china-03 · 管理端表单脏检查

文章 / 句子编辑表单的本地脏态（不入库，仅前端 UI 守卫）。

```
clean ──user_edit──▶ dirty
dirty ──save_ok──▶ clean
dirty ──save_fail──▶ dirty (保留输入)
dirty ──discard_confirm──▶ clean
dirty ──navigate_away──▶ confirm_modal ──confirm_stay──▶ dirty
                                    └─confirm_leave──▶ clean (丢弃)
```

- `dirty` 状态下顶部 banner 提示"未保存"，禁用切换语言 Tab；
- 离开页面强制弹确认，符合 R-discover-china-013 规则。

## SM-discover-china-04 · 应用端 TTS 播放器

单条句子播放器的运行态（纯前端，刷新页面即重置）。

```
idle ──tap_play──▶ loading
loading ──audio_ready──▶ playing
loading ──load_fail──▶ error
playing ──tap_pause──▶ paused ──tap_play──▶ playing
playing ──audio_end──▶ ended ──tap_play──▶ loading (重放)
error ──tap_retry──▶ loading
任意态 ──tap_other_sentence──▶ idle (清栈)
```

- 同一时刻仅允许 1 条句子处于 `playing`，切换自动暂停上一条；
- `error` 显示 toast，不阻塞页面其他句子。


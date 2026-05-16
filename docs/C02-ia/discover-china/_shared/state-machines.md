<!-- TARGET-PATH: docs/C02-ia/discover-china/_shared/state-machines.md -->

# 03 · 状态机

## SM-discover-china-01 · 文章发布状态

```mermaid
stateDiagram-v2
  [*] --> draft: 新建(R-009)
  draft --> published: 发布(R-013)
  published --> draft: 下架(R-013)\n→ 清空所有用户该文章进度
  draft --> [*]: 软删 deleted_at
  published --> [*]: 软删 deleted_at(强制先下架?在 C05-07-BR 规约:必须先下架)
```

| 状态 | 应用端可见 | 管理端可编辑 |
|------|----------|-------------|
| `draft` | 否 | 是 |
| `published` | 是 | 是 |

## SM-discover-china-02 · 句子 TTS 音频生成

```mermaid
stateDiagram-v2
  [*] --> none: 未生成
  none --> pending: 用户首次点播放(R-004)
  pending --> ready: AI 返回 + 缓存写
  pending --> failed: 5xx / timeout
  failed --> pending: 后台 retry(不限次)
  ready --> none: seq_no 重排导致缓存键失效(R-012)
```

## SM-discover-china-03 · 管理端表单脏检查

```mermaid
stateDiagram-v2
  [*] --> clean: 加载
  clean --> dirty: 任意字段变更(R-015)
  dirty --> clean: 保存成功
  dirty --> dirty: 离开拦截(留)
  dirty --> clean: 离开拦截(丢弃)
```

## SM-discover-china-04 · 应用端 TTS 播放器

```mermaid
stateDiagram-v2
  [*] --> idle
  idle --> loading: 单句 / 全文(R-004/005)
  loading --> playing: 音频就绪
  playing --> paused: 用户暂停
  paused --> playing: 用户恢复
  playing --> ended: 自然结束
  ended --> loading: 全文模式 + 下一句存在
  ended --> idle: 全文模式 + 无下一句
  loading --> error: TTS 失败(R-004)
  error --> idle: Toast 后归位
```

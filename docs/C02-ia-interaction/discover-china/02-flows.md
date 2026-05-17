<!-- TARGET-PATH: docs/C02-ia-interaction/discover-china/02-flows.md -->

# 业务流程

> **阶段**：C02-IN · **功能**：`discover-china`
> **冻结状态**：已冻结 · 2026-05-16

---

## 一、共享流程（FL-discover-china-NN）

| Flow-ID | 名称 | 类型 | 涉及 P-ID |
|---------|------|------|---------|
| FL-discover-china-01 | 访客 12 类目浏览 → 公开类目下钻 | 主 | P-app-discover-china-001 → 002 → 003 |
| FL-discover-china-02 | 全文朗读 | 主 | P-app-discover-china-003 |
| FL-discover-china-03 | 进度记忆同步 | 主 | P-app-discover-china-003 |
| FL-discover-china-04 | 管理员新建文章 | 主 | P-admin-discover-china-002 → 003 |
| FL-discover-china-05 | 句子编辑 / 插入 / 重排 | 主 | P-admin-discover-china-003 |
| FL-discover-china-06 | 管理端三级搜索 | 主 | P-admin-discover-china-001~003 → 004 |
| FL-discover-china-07 | 04-12 类目登录引导 | 异常 | P-app-discover-china-001 → `/auth/login` |
| FL-discover-china-08 | TTS 失败 + 后台重试 | 异常 | P-app-discover-china-003 |
| FL-discover-china-09 | 阅读中文章被下架 | 异常 | P-app-discover-china-003 → 002 |
| FL-discover-china-10 | 管理端后写覆盖 + 提示 | 异常 | P-admin-discover-china-003 |
| FL-discover-china-11 | 未保存离开拦截 | 异常 | P-admin-discover-china-003 → * |
| FL-discover-china-12 | 类目删除尝试拒绝 | 异常 | P-admin-discover-china-001 |
| FL-discover-china-13 | 5 语未齐发布拦截 | 异常 | P-admin-discover-china-003 |

---

## 二、app 端流程（F-app-disc-N）

### F-app-disc-1 · 浏览到播放

```
P-app-discover-china-001（分类首页）→ 选分类
    → P-app-discover-china-002（文章列表，cursor 翻页）
    → 选文章 → P-app-discover-china-003（文章详情 + 句子）
    → 点句子 → TTS 播放
```

涉及 endpoint：`GET /categories` · `GET /articles?category=...&cursor=` · `GET /articles/:slug` · `GET /sentences/:id/tts`。

### F-app-disc-2 · 搜索

```
P-app-discover-china-001 顶部搜索框 → q → GET /search?q= → 结果列表 → 命中文章 → P-003
```

### F-app-disc-3 · 离线降级

```
TTS 失败（网络 / 上游）→ 仅显示文本 + 重试按钮 + toast "音频暂不可用"
```

---

## 三、admin 端流程（F-admin-disc-N）

### F-admin-disc-1 · 新分类 + 文章 + 发布

```
P-admin-discover-china-001（分类）→ 新建分类（5 语）
    → P-admin-discover-china-002（文章列表）
    → 新建文章 → P-admin-discover-china-003（编辑器：正文 + 句子拆分）
    → 句子 TTS 异步生成 → 全部就绪后 → 发布
```

### F-admin-disc-2 · 索引重建

```
P-admin-discover-china-004（搜索运维）→ "重建索引" → 异步任务 → 进度条
                                     → 完成 → 校验报告
```

### F-admin-disc-3 · TTS 失败重试

```
P-admin-discover-china-003 句子列表 → 状态 failed → "重生成" → POST /sentences/:id/tts:regen
                                  → 队列 → 完成 / 再失败（达上限上报告警）
```

<!-- TARGET-PATH: docs/C01-requirements/course/flows/exception-flow.md -->

# 异常流程 · course

## FX-course-01 · 答题弱网

```mermaid
flowchart LR
  A[POST /app/answer] --> B{网络可用?}
  B -- 否 --> C[写本地队列<br/>localforage]
  C --> D[UI 继续渲染下一题]
  D --> E[回网检测 navigator.onLine]
  E --> F[批量 POST /app/answer:batch]
  F -- 成功 --> G[清本地队列]
  F -- 部分失败 --> H[保留失败项重试]
```

## FX-course-02 · 试抽失败 → exam 发布拦截

```mermaid
flowchart TD
  A[P-A-8 配置 exam blueprint] --> B[D-9 试抽预览]
  B --> C{抽题成功?}
  C -- 否(题量不足) --> D[Toast: 当前有效题数 < blueprint count]
  D --> E[发布按钮置灰]
  C -- 是 --> F[预览渲染]
  F --> G[发布按钮可点]
```

## FX-course-03 · 题目下架 → 已存 attempt 不变

```mermaid
flowchart LR
  A[P-A-5 行内下架题] --> B[questions.is_published=false]
  B --> C[新发卷抽题池排除]
  C --> D[已存 user_exam_attempts.snapshot<br/>保持原 q_ids]
  D --> E[历史回看可看,新 attempt 不抽]
```

## FX-course-04 · 媒资引用拦截

```mermaid
flowchart LR
  A[P-A-7 点删媒资] --> B{反查引用<br/>media_assets.ref_kp_id<br/>ref_q_id}
  B -- 有引用 --> C[D-1 拦截弹窗<br/>列出 N 处引用]
  B -- 无引用 --> D[D-1 二次确认]
  D --> E[软删媒资]
```

## FX-course-05 · 阶段考已通过不可重考

```mermaid
flowchart LR
  A[用户进 P-C-6 列表] --> B{该阶段考<br/>user_exam_attempts.passed?}
  B -- 是 --> C[按钮置灰 + Toast:阶段考通过后不可重考]
  B -- 否 --> D[正常进考]
```

## FX-course-06 · 离线进节包预下载失败

```mermaid
flowchart TD
  A[进 P-C-2 节学习页] --> B[尝试整节预下载<br/>KP+题+音频]
  B -- 成功 --> C[正常进卡片流]
  B -- 部分失败 --> D[Toast: 部分音频未缓存,可继续]
  D --> E[播放音频时再次按需拉]
  E -- 仍失败 --> F[图标显示 ⚠ + 学员可跳过]
```

## FX-course-07 · 多管理员并发编辑 KP

```mermaid
flowchart LR
  A[admin1 打开 KP Drawer<br/>记录 loaded_updated_at] --> B[admin2 同时打开同 KP]
  B --> C[admin2 先保存<br/>updated_at=t2]
  C --> D[admin1 保存请求]
  D --> E{服务端比对<br/>req.loaded_updated_at < t2?}
  E -- 是 --> F[LWW 覆盖<br/>Toast: 该内容已被 admin2 修改并被你覆盖]
  E -- 否 --> G[正常保存]
```

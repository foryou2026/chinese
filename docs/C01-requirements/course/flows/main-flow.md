<!-- TARGET-PATH: docs/C01-requirements/course/flows/main-flow.md -->

# 主流程 · course

> 信息源:〔历史素材〕 §6.2-6.8。

## FL-course-01 · 内容上架主链路(管理端)

```mermaid
flowchart LR
  A[运营线下生成<br/>JSON/CSV] --> B[P-A-4/P-A-5<br/>批量导入 D-15]
  B --> C{字段校验 + hash 去重}
  C -- 错误 --> D[导出错误行]
  C -- 通过 --> E[写 KP/Q<br/>is_published=false]
  E --> F[P-A-4/P-A-5<br/>人工点检 + 编辑]
  F --> G[P-A-4/P-A-5<br/>批量发布 / 行内发布]
  G --> H[P-A-8 配节测 / 章测 /<br/>阶段考 blueprint + 试抽]
  H --> I[exam.is_published=true]
  I --> J[CDN 同步 + 学员端可见]
```

## FL-course-02 · 学员学习一节(应用端)

```mermaid
flowchart TD
  Start[用户点 继续学习] --> Get[GET /app/lesson/:code<br/>聚合接口]
  Get --> Pre[整节预下载<br/>KP+题+音频]
  Pre --> Loop{遍历 12 KP}
  Loop --> Kp[KP 讲解卡]
  Kp --> Q[随堂练 2-4 题<br/>POST /app/answer]
  Q -- 答对 --> SRSup[user_srs 升盒]
  Q -- 答错 --> SRSdown[user_srs box=1<br/>due=明天]
  SRSup --> Loop
  SRSdown --> Loop
  Loop -- 12 KP 完 --> Quiz[节末小测 D-13 可跳过]
  Quiz -- 跳过 --> Finish[POST /finish<br/>status=in_progress]
  Quiz -- 做 --> Q6[6 题统一交卷]
  Q6 --> Finish2[POST /finish<br/>status=passed/in_progress]
  Finish --> Unlock[解锁判断<br/>同章下一节]
  Finish2 --> Unlock
```

## FL-course-03 · SRS 每日复习

```mermaid
flowchart LR
  A[用户点 今日复习] --> B[GET /app/srs/today]
  B --> C{SELECT user_srs<br/>due_at<=now<br/>ORDER box,due ASC<br/>LIMIT 30}
  C --> D[每 KP 抽 1 题<br/>题型轮换]
  D --> E[逐题答题<br/>context_type=srs_review]
  E -- 对 --> F[box+1<br/>due += 间隔表]
  E -- 错 --> G[box=1<br/>due=明天]
```

## FL-course-04 · 考试

```mermaid
flowchart TD
  A[用户点 阶段考] --> B[POST /exam/:id/start]
  B --> C[按 blueprint 抽题<br/>snapshot=q_ids]
  C --> D[写 user_exam_attempts<br/>started_at + snapshot]
  D --> E[倒计时 + 不反馈<br/>不能中途退出]
  E --> F[POST /exam/:attempt/submit]
  F --> G[逐题判分写流水<br/>context_type=stage_exam]
  G --> H{score >= pass_score?}
  H -- 是 + stage_exam --> I[解锁下一阶段全部节]
  H -- 是/否 --> J[错题入 SRS box1]
  J --> K[结果页 + 错题列表]
```

## FL-course-05 · 学员举报闭环

```mermaid
flowchart LR
  A[答题反馈页 🚩举报<br/>D-14] --> B[POST /app/feedback]
  B --> C[content_action_log<br/>action=report]
  C --> D[P-A-6 按 question_id 聚合<br/>≥3 自动置顶]
  D --> E[admin 点 D-7 详情]
  E -- 跳目标编辑 --> F[P-A-5 题目 Drawer<br/>修正 + version+1]
  E -- 采纳 --> G[D-8 标记 adopted]
  E -- 忽略 --> H[D-8 标记 dismissed]
  F --> I[新作答取 v2<br/>历史 user_answers 不动]
```

## FL-course-06 · 首次进入引导

```mermaid
flowchart LR
  A[启动 App] --> B[选 UI 语言]
  B --> C[注册 / 登录 OTP]
  C --> D[选目标主题<br/>多选主修一个]
  D --> E[自评水平]
  E --> F[5 题听写定级]
  F -- 零基础 --> G[强制 Stage 0]
  F -- 有基础 --> H[直接进对应 Stage]
  G --> I[首页 第一节高亮]
  H --> I
```

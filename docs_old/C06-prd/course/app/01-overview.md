<!-- TARGET-PATH: docs/C06-prd/course/app/01-overview.md -->

# 01 · 总览 · course / **app**

> 跨端通用术语见 [`../_shared/glossary.md`](../_shared/glossary.md);跨端业务规则见 [`../_shared/business-rules.md`](../_shared/business-rules.md)。

## 1.1 产品定位(app 端视角)

`course` app 端是面向 **东南亚(越南 / 泰国 / 印尼)成人零基础 ~ HSK4 学习者** 的中文学习引擎,通过 **预生成的不可变学习资源 + 静默题型 + 简化 SRS** 让学员"听得懂、看得懂、能打字回复"(**不练口语发音**)。来源:〔历史素材〕。

## 1.2 内容骨架(app 端可见)

| 层级 | 数量(初版规划) | 学员可见入口 |
|------|----------------|-------------|
| **Track(主题)** | 4 业务主题:`EC`(电商)/ `FC`(工厂)/ `HSK`(应试)/ `DL`(日常),共享层 `share` 仅作底层依赖、**不出现** | 首页 [P-app-course-001](06-page-specs/P-app-course-001.md) |
| Stage(阶段) | 每主题 ≈ 6 | 进入主题后展开 |
| Chapter(章) | 每阶段 ≈ 6 | 章列表 |
| Lesson(节) | 每章 ≈ 6 | 节详情 [P-app-course-002](06-page-specs/P-app-course-002.md) |
| KP(知识点) | 与节多对多 | 节内卡片 |
| 题(item) | 每节配套 ≈ 50 ~ 200 道(7 类 KP × 12 题型) | 答题 [P-app-course-003](06-page-specs/P-app-course-003.md) |

> 数量来自 〔历史素材〕 的"建议 6 个 / 6 章"近似值,**实际入库以管理端发布为准**;app 端不展示骨架统计。

## 1.3 app 端核心闭环

1. **学** [P-002](06-page-specs/P-app-course-002.md):节卡片 → KP 讲解 → 节内自测
2. **练** [P-003](06-page-specs/P-app-course-003.md):12 静默题型(选择/连线/排序/点选/键盘输入);错题进 SRS
3. **复** [P-004](06-page-specs/P-app-course-004.md) + [P-005](06-page-specs/P-app-course-005.md):简化 SM-2 / Leitner 5 盒,每日 ≤ 50;错题本独立入口
4. **考** [P-006](06-page-specs/P-app-course-006.md) → [P-007](06-page-specs/P-app-course-007.md) → [P-008](06-page-specs/P-app-course-008.md):节测 / 章测 / 阶段考(题目卡片式试抽,2025-11 变更后取消"系统内生成工作台")

## 1.4 5 语策略(app 端)

- UI / 讲解 / 翻译适配 `zh / en / vi / th / id`,学员可在 [P-app-auth-005](../../auth/app/06-page-specs/P-app-auth-005.md) 切换;
- 中文教学目标本体(汉字 + 拼音 + 音频)**只一套**,不翻译;
- 选择哪种"对照语言显示在中文上方/下方",随学员 UI 语种联动。

## 1.5 性能基线(app 端)

| 接口 / 操作 | 目标 |
|------------|------|
| 业务接口{code}(单节聚合,gzip) | 响应体 ≤ 200 KB,P95 ≤ 300 ms |
| 业务接口(单用户单次 LIMIT 50) | P95 ≤ 200 ms |
| 业务接口(单题判分写入) | P95 ≤ 150 ms,限流 60 次/分/用户(超出 429) |
| 业务接口{attempt}`/submit`(批量判分 50 题) | P95 ≤ 800 ms |

> 路由别名:`/api/api/* ≡ /api/app/api/*`,见 [_glossary.md §E](../../_glossary.md)。

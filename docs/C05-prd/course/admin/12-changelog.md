<!-- TARGET-PATH: docs/C05-prd/course/admin/12-changelog.md -->

> **本文件为 surface=`admin` 视角的 PRD 章节(Round 2 从 PRD.md 第 12 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

## 12. 决策封板与本期不在范围

- **不做(v1)**:AI 对话陪练 / 发音打分 / 作文批改 / 千人千面;直播 / 1v1;论坛 UGC;系统内 AI 生成工作台(2025-11 废)、自定义主题码、自由建题、阶段考重考、举报自动改内容、AI 提示词管理页;
- **决策已封板**(详 [`function/02-course/prd/07-待确认问题清单.md`](../../../function/02-course/prd/07-待确认问题清单.md)):
  - A 段范围(主题数 5 固定 / Stage 0 共享一次性);
  - B 段内容发布(章节级联 / 下架不级联 / 节末测可跳过);
  - C 段考试(满分 100 动态均分 / 不可重考阶段考 / 试抽不写 attempt);
  - H 段版本(`version+1` 治理 + 历史不追溯);
- **跨域副作用契约**:见 §7.8 BR-Y01..Y04 与 [`C02/03-state-machines.md`](../../C02-ia/course/03-state-machines.md)。

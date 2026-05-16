<!-- TARGET-PATH: docs/C02-ia/course/app/02-flows.md -->

> **本文件为 surface=`app` 的视角拷贝(Round 1 物理拆分初版,Round 3+ 将按端过滤实质内容)。** 跨端通用部分见 [_shared/flows-shared.md](../_shared/flows-shared.md) 与 [_shared/state-machines.md](../_shared/state-machines.md)。


# 02 · 流程清单(Flow-ID) · course

| Flow-ID | 标题 | 类型 | 源 | 涉及 P-ID |
|---------|------|------|----|----------|
| **FL-course-01** | 内容上架主链路 | 主 | [main-flow.md#FL-course-01](../../C01-requirements/course/flows/main-flow.md) | P-admin-course-002..008 |
| **FL-course-02** | 学员学习一节 | 主 | [main-flow.md#FL-course-02](../../C01-requirements/course/flows/main-flow.md) | P-app-course-002 |
| **FL-course-03** | SRS 每日复习 | 主 | [main-flow.md#FL-course-03](../../C01-requirements/course/flows/main-flow.md) | P-app-course-004 |
| **FL-course-04** | 考试(4 类)| 主 | [main-flow.md#FL-course-04](../../C01-requirements/course/flows/main-flow.md) | P-app-course-006/007/008 |
| **FL-course-05** | 学员举报闭环 | 主 | [main-flow.md#FL-course-05](../../C01-requirements/course/flows/main-flow.md) | P-admin-course-006 / P-admin-course-005 |
| **FL-course-06** | 首次进入引导 | 主 | [main-flow.md#FL-course-06](../../C01-requirements/course/flows/main-flow.md) | P-app-course-001 |
| **FX-course-01** | 答题弱网入本地队列 | 异 | [exception-flow.md#FX-course-01](../../C01-requirements/course/flows/exception-flow.md) | P-app-course-002/004/006 |
| **FX-course-02** | 试抽失败 → 发布拦截 | 异 | [exception-flow.md#FX-course-02](../../C01-requirements/course/flows/exception-flow.md) | P-admin-course-008 |
| **FX-course-03** | 题目下架 attempt 不变 | 异 | [exception-flow.md#FX-course-03](../../C01-requirements/course/flows/exception-flow.md) | P-admin-course-005 / P-app-course-006 |
| **FX-course-04** | 媒资引用拦截 | 异 | [exception-flow.md#FX-course-04](../../C01-requirements/course/flows/exception-flow.md) | P-admin-course-007 |
| **FX-course-05** | 阶段考已通过不可重考 | 异 | [exception-flow.md#FX-course-05](../../C01-requirements/course/flows/exception-flow.md) | P-app-course-006 |
| **FX-course-06** | 节包预下载部分失败 | 异 | [exception-flow.md#FX-course-06](../../C01-requirements/course/flows/exception-flow.md) | P-app-course-002 |
| **FX-course-07** | 多管理员并发覆盖 | 异 | [exception-flow.md#FX-course-07](../../C01-requirements/course/flows/exception-flow.md) | P-admin-course-004/005 |

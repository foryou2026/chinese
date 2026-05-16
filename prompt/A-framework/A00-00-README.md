# 00 · G00 Skills 框架 · README

> 一套面向 AI 协同开发的、从「需求」到「上线增长」全链路的标准化提示词模板集。
>
> **核心承诺**
> - 每一步都把「用户填什么 / AI 必须先问什么 / AI 最终输出什么」拆成三件套，杜绝跳步。
> - 每一份 AI 产出都按规范命名、写入 `/docs` 下固定位置，下游可机械引用。
> - 单文件 ≤ 1200 行，超出强拆。
> - 框架本身不绑定任何技术栈、不绑定任何项目。开箱即用。

---

## 阅读顺序

1. [A00-01-框架总览](./A00-01-框架总览.md)
2. [A00-02-端到端工作流](./A00-02-端到端工作流.md)
3. [A00-03-通用约定](./A00-03-通用约定.md)
4. [A00-04-文档目录规划](./A00-04-文档目录规划.md)
5. 然后：先按 `B01~B03` 一次性定调（3 阶段），再按 `C01~D03` 逐 feature 循环（9 阶段）。

---

## 框架结构：F（一次性定调）+ C（按 feature 循环）

本框架把传统瀑布式 12 阶段拆成两层，对齐现代敏捷设计-开发流程：

| 层 | 前缀 | 阶段数 | 触发频率 | 何时执行 |
|----|------|--------|---------|---------|
| **F · Foundation** | `B01~B03` | 3 | 项目级，**一次性** | 项目启动后跑一次，输出全局规范，所有 feature 共用 |
| **C · Cycle** | `C01~D03` | 9 | feature 级，**每个 feature 跑一遍** | F 全部冻结后开始；同一 feature 顺序走完 C01→D03；多 feature 可并行 |

> 只有「F 全部 ✅」之后才能开始任何 feature 的 C 循环；
> 只有「某 feature 的 C01~D02 全部 ✅」之后才能跑该 feature 的 D03（一致性校验）；
> 只有 D03 全绿才能进入开发实现。

---

## F · 一次性定调（项目级，跑一次）

| 阶段码 | 名称 | 角色 | 输出落盘 | 备注 |
|--------|------|------|---------|------|
| **B01 · A** | 技术架构 | 架构师 | `docs/B01-architecture/` | 选栈、目录、DB/API/编码规范、surface 清单、**鉴权基础设施**（如项目有登录类需求） |
| **B02 · X** | 体验定调（UX 调性）| 体验总监 | `docs/B02-ux/` | — |
| **B03 · S** | 设计系统 + 原型样式包 | UI 设计师 | `docs/B03-design/` | 产出 `design-system/`（规范）+ `prototype-style/`（可运行 CSS/JS 资产） |

> **顺序**：A 必须先于所有 C 循环（C 阶段会引用架构规范）；X → S 必须先于 C04/C05（页面交互与原型直接消费设计 Token）。
> **B03 双产出**：`docs/B03-design/design-system/` 是给前端工程实现 React 组件的 markdown 规范；`docs/B03-design/prototype-style/` 是可运行 CSS / JS 资产，C05 HTML 原型 **通过相对路径引用**（不拷贝），两者共享同一套 token，确保「原型一个样、上线一个样」。

---

## C · 按 feature 循环（每个 feature 跑一遍）

| 阶段码 | 名称 | 角色 | 输出落盘 | 触发节点 |
|--------|------|------|---------|---------|
| **C01 · R** | 需求分析（feature 级） | 需求分析师 | `docs/C01-requirements/<feature>/` | feature 启动 |
| **C02 · P** | 角色与权限（feature 增量并入全局） | 安全/权限工程师 | `docs/C02-permissions/`（全局合并写入）| C01 冻结后 |
| **C03 · I** | 信息架构（功能清单 + 流程 + 状态机 + 页面清单）| 信息架构师 | `docs/C03-ia/<feature>/` | C02 冻结后 |
| **C04 · N** | 页面交互 | 交互设计师 | `docs/C04-pages/<feature>/` | C03 冻结后 |
| **C05 · H** | HTML 原型 | 原型工 | `docs/C05-prototype/<feature>/` | C04 冻结后；一次性出齐本 feature 全部 page-id |
| **C06 · E** | 产品需求文档（PRD）| 产品经理 | `docs/C06-prd/<feature>/` | C05 稳定后 |
| **D01 · D** | 数据模型 | 数据建模师 | `docs/D01-data/<feature>/` | C06 冻结后 |
| **D02 · L** | 路由与接口 | 接口设计师 | `docs/D02-api/<feature>/` | D01 冻结后 |
| **D03 · V** | 开发前一致性校验 | QA / 文档审计师 | `docs/D03-validation/<feature>/` | C01~D02 全部冻结后；本 feature 进入开发的最终闸门 |

> **设计先行原则**：本框架把数据模型 / 接口（D01/D02）放在原型 / PRD（C05/C06）之后。
> 这是现代敏捷做法——先用原型把 UX 和产品形态定死，再倒推数据模型与接口契约，避免「先建表后改 UI」的大返工。
> **多 feature 并行**：项目级 F 冻结后，feature A、feature B 的 C 循环可同时进行；它们彼此只通过 F 全局规范、已冻结的全局权限文档（`docs/C02-permissions/`）和全局 PRD 索引（`docs/C06-prd/_global-index.md`）协调。
> **C02·P 写入全局**：每个 feature 的 C02 输出**不放 feature 子目录**，而是把本 feature 引入的角色、权限矩阵、数据可见范围**增量并入** `docs/C02-permissions/01-roles.md`、`02-authz-mechanism.md`、`03-data-model.md`，确保「全项目只有一份权限事实」。

---

## 全链路执行顺序速记

```
B01 · A  →  B02 · X  →  B03 · S                                ← 一次性定调（3 步）
                  ↓
   ┌──────────────┴──────────────────────────────────────────────────────────┐
   │ for each feature:                                                        │
   │   C01 R → C02 P → C03 I → C04 N → C05 H → C06 E → D01 D → D02 L          │
   │   → D03 V (全绿 ✅) → 进入该 feature 的开发实现                            │
   └──────────────────────────────────────────────────────────────────────────┘
```

---

## 文件命名规则（贯穿全框架）

- `<前缀><阶段字母><序号>-用途-文件名.md`
  - 示例：`B01-A02-AI澄清-架构提问.md`、`D01-D03-AI输出-数据规范.md`
- 框架层（无阶段字母）：`A00-XX-...`
  - `A00-00-README` / `A00-01-框架总览` / `A00-02-端到端工作流` / `A00-03-通用约定` / `A00-04-文档目录规划`
- 「用户输入」类：用户填写、保存到对应 `docs/` 子目录后发给 AI
- 「AI澄清」类：AI 收到用户输入后**第一轮回复必须是它**，列出阻断级与优化级问题
- 「AI输出」类：用户回答澄清后 AI 才允许输出最终交付物

---

## 三件套铁律

```
① 用户输入模板  →  ② AI 澄清提问模板  →  ③ AI 输出模板
   你填表           AI 必须先问           AI 才允许出报告
```

任何阶段 AI 跳过 ② 直接出 ③ → 立刻打回重做。

> **例外**：
> - D03 V 阶段不需澄清（其输入完全来自上游冻结产物），三份输出按 `D03-V01/V02/V03` 顺序串跑。

---

## 全部 12 阶段 → 文件索引

### F · 一次性定调（B-foundation/）

| 阶段 | 用户输入 | AI 澄清 | AI 输出 |
|------|---------|---------|---------|
| B01 · A | [B01-A01](../B-foundation/B01-A01-用户输入-技术偏好.md) | [B01-A02](../B-foundation/B01-A02-AI澄清-架构提问.md) | [B01-A03](../B-foundation/B01-A03-AI输出-架构规范.md) |
| B02 · X | [B02-X01](../B-foundation/B02-X01-用户输入-体验风格.md) | [B02-X02](../B-foundation/B02-X02-AI澄清-体验提问.md) | [B02-X03](../B-foundation/B02-X03-AI输出-体验定调.md) |
| B03 · S | [B03-S01](../B-foundation/B03-S01-用户输入-视觉偏好.md) | [B03-S02](../B-foundation/B03-S02-AI澄清-视觉提问.md) | [B03-S03](../B-foundation/B03-S03-AI输出-设计系统.md) |

### C · 按 feature 循环（C-product/ + D-develop/）

| 阶段 | 用户输入 | AI 澄清 | AI 输出 |
|------|---------|---------|---------|
| C01 · R | [C01-R01](../C-product/C01-R01-用户输入-需求初稿.md) | [C01-R02](../C-product/C01-R02-AI澄清-需求提问.md) | [C01-R03](../C-product/C01-R03-AI输出-需求基线.md) |
| C02 · P | [C02-P01](../C-product/C02-P01-用户输入-角色描述.md) | [C02-P02](../C-product/C02-P02-AI澄清-权限提问.md) | [C02-P03](../C-product/C02-P03-AI输出-权限规范.md) |
| C03 · I | [C03-I01](../C-product/C03-I01-用户输入-信息架构方向.md) | [C03-I02](../C-product/C03-I02-AI澄清-信息架构提问.md) | [C03-I03](../C-product/C03-I03-AI输出-信息架构.md) |
| C04 · N | [C04-N01](../C-product/C04-N01-用户输入-页面描述.md) | [C04-N02](../C-product/C04-N02-AI澄清-交互提问.md) | [C04-N03](../C-product/C04-N03-AI输出-页面交互规范.md) |
| C05 · H | [C05-H01](../C-product/C05-H01-用户输入-原型方向.md) | [C05-H02](../C-product/C05-H02-AI澄清-原型提问.md) | [C05-H03](../C-product/C05-H03-AI输出-HTML原型规范.md) |
| C06 · E | [C06-E01](../C-product/C06-E01-用户输入-产品背景.md) | [C06-E02](../C-product/C06-E02-AI澄清-PRD提问.md) | [C06-E03](../C-product/C06-E03-AI输出-产品需求文档.md) |
| D01 · D | [D01-D01](../D-develop/D01-D01-用户输入-数据规则.md) | [D01-D02](../D-develop/D01-D02-AI澄清-数据提问.md) | [D01-D03](../D-develop/D01-D03-AI输出-数据规范.md) |
| D02 · L | [D02-L01](../D-develop/D02-L01-用户输入-操作逻辑.md) | [D02-L02](../D-develop/D02-L02-AI澄清-接口提问.md) | [D02-L03](../D-develop/D02-L03-AI输出-接口规范.md) |
| D03 · V | — | — | [D03-V01](../D-develop/D03-V01-AI输出-上游链一致性.md) · [D03-V02](../D-develop/D03-V02-AI输出-模块内闭环.md) · [D03-V03](../D-develop/D03-V03-AI输出-PRD回链校验.md) |

---

## 与 docs 目录的对应关系

| 阶段 | docs 落盘根 |
|------|-------------|
| 框架层 | `docs/A00-meta/` |
| B01 · A | `docs/B01-architecture/` |
| B02 · X | `docs/B02-ux/` |
| B03 · S | `docs/B03-design/` |
| C01 · R | `docs/C01-requirements/<feature>/` |
| C02 · P | `docs/C02-permissions/`（**全局合并，不开 feature 子目录**） |
| C03 · I | `docs/C03-ia/<feature>/` |
| C04 · N | `docs/C04-pages/<feature>/` |
| C05 · H | `docs/C05-prototype/<feature>/` |
| C06 · E | `docs/C06-prd/<feature>/` |
| D01 · D | `docs/D01-data/<feature>/` |
| D02 · L | `docs/D02-api/<feature>/` |
| D03 · V | `docs/D03-validation/<feature>/` |

详见 [A00-04-文档目录规划](./A00-04-文档目录规划.md)。

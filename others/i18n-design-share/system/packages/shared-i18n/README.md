# Zhiyu 多语言国际化维护手册

这份文档说明当前项目如何实现多语言、如何新增和维护文案、如何让人类开发者和 AI agent 按同一套纪律继续迭代。

## 目标

Zhiyu 的国际化目标不是只把 UI 翻译出来，而是建立一套长期可维护的流程：

- 英文作为产品 UI 源文案。
- 每次新增用户可见文案时，同步补齐所有当前支持语言。
- 用自动化测试防止漏 key、空翻译和 placeholder 不一致。
- 用规则文件约束人类和 AI，不让 JSX 里重新出现散落的硬编码 UI 文案。
- 用浏览器 QA 覆盖关键页面和语言切换行为。

## 当前支持语言

语言列表以 `packages/shared-config/src/locales.ts` 为准：

| Locale | 语言 | 说明 |
| --- | --- | --- |
| `zh` | 中文 | 当前默认语言 |
| `en` | English | UI 源文案语言，fallback 语言 |
| `vi` | Tiếng Việt | 越南语 |
| `th` | ไทย | 泰语 |
| `id` | Bahasa Indonesia | 印尼语 |

维护要求：

- 新增语言时，要同步改 `packages/shared-config/src/locales.ts`、`packages/shared-i18n/src/index.ts`、语言切换 UI、测试和本文档。
- 不要只在某个页面临时增加一种语言。
- 不要在业务代码里手写 locale union，统一从 `@zhiyu/shared-config` 引入 `Locale`。

## 技术栈

当前 web-app 使用：

- `i18next`：运行时国际化核心。
- `react-i18next`：React hooks 和组件接入。
- `@zhiyu/shared-i18n`：集中保存 UI 文案资源。
- `@zhiyu/shared-config`：集中保存 locale 列表、默认语言、语言展示名等配置。
- TypeScript 模块文案文件：当前不是 JSON，而是 `src/en.ts`、`src/zh.ts`、`src/vi.ts`、`src/th.ts`、`src/id.ts`。
- `tsx scripts/verify-i18n.ts`：i18n 完整性测试。

为什么使用 TypeScript 文案文件：

- 可以在 monorepo package 中直接导出资源。
- 可以让 `ResourceShape = typeof en` 以英文源文案约束整体结构。
- 支持嵌套对象，比纯扁平 JSON 更适合后续按模块组织。
- 后续如果要接入 TMS 或外部翻译平台，也可以从 TS 资源生成 JSON。

## 目录说明

```txt
system/
  AGENTS.md
  .claude/
    rules/
      i18n.md
  packages/
    shared-config/
      src/
        locales.ts
    shared-i18n/
      README.md
      package.json
      scripts/
        verify-i18n.ts
      src/
        index.ts
        en.ts
        zh.ts
        vi.ts
        th.ts
        id.ts
  apps/
    web-app/
      src/
        app/
          i18n.ts
          Layout.tsx
        lib/
          china-types.ts
        pages/
```

关键文件：

- `packages/shared-i18n/src/en.ts`：英文源文案，新增 key 先写这里。
- `packages/shared-i18n/src/zh.ts`：中文 UI 文案。
- `packages/shared-i18n/src/vi.ts`：越南语 UI 文案。
- `packages/shared-i18n/src/th.ts`：泰语 UI 文案。
- `packages/shared-i18n/src/id.ts`：印尼语 UI 文案。
- `packages/shared-i18n/src/index.ts`：导出 `RESOURCES`，并用 `ResourceShape = typeof en` 固定资源结构。
- `packages/shared-i18n/scripts/verify-i18n.ts`：检查所有语言 key 一致、值不为空、placeholder 一致。
- `apps/web-app/src/app/i18n.ts`：初始化 `i18next`，检测语言、配置 fallback、持久化选择。
- `apps/web-app/src/app/Layout.tsx`：全局布局和语言切换入口。
- `apps/web-app/src/lib/china-types.ts`：内容型 `*_i18n` 字段的读取和 fallback 工具。
- `AGENTS.md`：项目级 agent 规则。
- `.claude/rules/i18n.md`：Claude/Codex 等 agent 可读取的 i18n 专项规则。

## 两类国际化数据

项目里有两类多语言内容，不要混用。

### 1. UI 文案

按钮、导航、空状态、错误提示、表单 label、页面标题等属于 UI 文案。

这些文案必须放在 `@zhiyu/shared-i18n`：

```ts
// packages/shared-i18n/src/en.ts
const en = {
  common: {
    save: 'Save',
    cancel: 'Cancel',
  },
  auth: {
    login: 'Log in',
  },
};

export default en;
```

组件中使用：

```tsx
import { useTranslation } from 'react-i18next';

export function SaveButton() {
  const { t } = useTranslation();
  return <button>{t('common.save')}</button>;
}
```

### 2. 业务内容

文章标题、分类名称、课程名称、题干、知识点标题等来自数据库或 API 的内容型数据，通常是 `*_i18n` 字段：

```ts
type I18nMap = {
  zh?: string;
  en?: string;
  vi?: string;
  th?: string;
  id?: string;
};
```

前端读取时用 `pickI18n`：

```tsx
import { pickI18n } from '../../lib/china-types';

const title = pickI18n(article.title_i18n, lang);
```

默认 fallback 规则在 `china-types.ts` 中维护。当前思路是优先当前语言，再回退 `en`，最后回退 `zh`。

判断标准：

- 文案由产品界面固定提供：放 `shared-i18n`。
- 文案属于数据库内容、课程内容、文章内容、题库内容：用 `*_i18n` 数据字段。
- 不要把数据库内容复制进 UI 文案文件。
- 不要把按钮、导航、toast 等 UI 文案放到数据库字段里。

## Runtime 初始化

web-app 在 `apps/web-app/src/main.tsx` 中引入：

```ts
import './app/i18n.ts';
```

初始化逻辑在 `apps/web-app/src/app/i18n.ts`：

- 从 `localStorage.zhiyu-locale` 读取用户选择。
- 如果没有用户选择，则根据 `navigator.language` 检测语言。
- 用 `LOCALES` 和 `RESOURCES` 注册所有语言。
- `fallbackLng` 使用 `en`。
- 用户切换语言时调用 `setLocale(locale)`，同时写入 `localStorage`。

注意：

- `DEFAULT_LOCALE` 当前是 `zh`，用于首次检测不到浏览器语言时的默认显示。
- `fallbackLng` 当前是 `en`，因为英文是源文案。某个翻译缺失时应优先暴露英文，而不是静默显示另一种翻译。
- 如果要改变默认语言或 fallback，需要同时更新产品决策、测试预期和本文档。

## Key 命名约定

推荐按功能域分组，保持层级稳定：

```ts
const en = {
  common: {
    save: 'Save',
    cancel: 'Cancel',
    locked: 'Locked',
  },
  nav: {
    home: 'Home',
    china: 'Discover China',
  },
  auth: {
    login: 'Log in',
    forgot_password: 'Forgot password?',
  },
  china: {
    search_placeholder: 'Search articles',
  },
};
```

约定：

- 使用小写 snake_case：`forgot_password`。
- 语义稳定优先，不把展示位置写死到 key 里。
- 按业务域组织：`auth`、`nav`、`china`、`course`。
- 通用动作放 `common`：`save`、`cancel`、`loading`。
- 不要用 `text1`、`button2`、`new_label` 这类无法维护的 key。
- 不要因为改了英文文案就重命名 key。key 是 API，不是显示文案。

## 新增 UI 文案流程

每次加用户可见文案，按这个顺序做：

1. 在 `packages/shared-i18n/src/en.ts` 添加英文源文案。
2. 在 `zh.ts`、`vi.ts`、`th.ts`、`id.ts` 添加同名 key。
3. 在 React 组件里使用 `const { t } = useTranslation()`。
4. 用 `t('path.to.key')` 替换硬编码文案。
5. 如果文案有变量，使用 placeholder，例如 `t('common.welcome_user', { name })`。
6. 运行 i18n 测试。
7. 巡检有没有遗漏的硬编码中文或英文 UI 文案。
8. 启动 web-app，用浏览器切换所有语言检查关键页面。

示例：

```ts
// en.ts
profile: {
  welcome_user: 'Welcome, {{name}}',
}
```

```ts
// zh.ts
profile: {
  welcome_user: '欢迎，{{name}}',
}
```

```tsx
const { t } = useTranslation();

return <h1>{t('profile.welcome_user', { name: user.displayName })}</h1>;
```

## Placeholder 规则

placeholder 必须在所有语言中完全一致。

正确：

```ts
// en
delete_confirm: 'Delete {{name}}?'

// zh
delete_confirm: '删除 {{name}}？'
```

错误：

```ts
// vi
delete_confirm: 'Xóa {{title}}?'
```

`verify-i18n.ts` 会检查：

- 每个语言都有和 `en` 一样的 key。
- 每个 value 非空。
- 每个 value 的 `{{placeholder}}` 集合和英文一致。

如果需要复数或复杂格式，先评估 `i18next` plural/context 方案，再统一扩展测试，不要在某个页面临时拼字符串。

## AI 翻译工作流

新增英文源文案后，可以让 AI 翻译其他语言。推荐提示词：

```txt
请为以下新增 i18n key 翻译 zh、vi、th、id。

要求：
- en 是源文案，只根据英文含义翻译。
- 保持 JSON/TS 对象 key 完全一致。
- 保持 {{placeholder}} 完全一致。
- 按产品 UI 文案翻译，简短自然，不要机器直译。
- 按各语言自然标点处理。
- 不要改动未提到的 key。
- 如果某个翻译不确定，在回复里列出疑问，不要在代码注释里写 TODO。

新增英文：
...
```

AI 翻译后，人类或另一个 agent 需要检查：

- 语言是否自然。
- 按钮是否过长。
- 占位符是否一致。
- 是否误删、误改已有 key。
- 是否把品牌名、专有名词翻错。

## 测试命令

修改 i18n 资源后，至少运行：

```bash
pnpm --filter @zhiyu/shared-i18n test
```

建议一起运行：

```bash
pnpm --filter @zhiyu/shared-i18n typecheck
pnpm --filter @zhiyu/web-app typecheck
```

如果本地依赖未安装：

```bash
pnpm install
```

如果 typecheck 失败，先判断是本次变更导致，还是已有基线问题。不要为了让 i18n 改动通过而顺手改无关模块。

## 硬编码巡检

中文硬编码快速检查：

```bash
rg -n "[\\p{Han}]" system/apps/web-app/src -g "*.tsx" -g "*.ts"
```

英文 UI 文案无法只靠正则完全判断，可以重点查 JSX 中的裸字符串：

```bash
rg -n ">[A-Z][^<{]*<|placeholder=|aria-label=|title=" system/apps/web-app/src -g "*.tsx"
```

允许存在的情况：

- 注释。
- 测试 fixture。
- 数据示例。
- API 字段名。
- URL、code、slug、enum。
- 来自业务数据的 `*_i18n` 渲染。

不允许存在的情况：

- 按钮文字硬编码。
- 导航文字硬编码。
- 表单 label、placeholder、helper text 硬编码。
- 空状态、错误提示、toast 硬编码。
- `aria-label`、`title` 等可见或辅助 UI 文案硬编码。

## 浏览器 QA 计划

修改 UI 文案后建议启动 web-app：

```bash
pnpm --filter @zhiyu/web-app dev
```

然后用浏览器按这个路线测试：

1. 打开首页。
2. 切换 `zh`、`en`、`vi`、`th`、`id`。
3. 刷新页面，确认语言选择被 `localStorage` 保留。
4. 检查导航、按钮、登录入口、空状态。
5. 进入登录、注册、忘记密码、回调页等 auth 页面。
6. 进入 Discover China 分类页、列表页、详情页。
7. 使用搜索框，检查 placeholder、加载态、无结果、结果数量。
8. 检查上一页、下一页、播放按钮等小文案。
9. 如果涉及课程页面，进入课程地图、课时、练习、考试、错题、SRS。
10. 打开浏览器 console，确认没有运行时错误。

已知本地 QA 注意事项：

- 本地接口和前端可能对 `localhost`、`127.0.0.1` 有不同 origin 行为。若 `127.0.0.1` 页面接口失败，优先用 dev server 输出的 `localhost` URL 复测。
- 如果某个页面依赖数据库 seed，先确认本地 API 和数据已启动。

## Agent 规则

本项目提供两层规则文件：

### `system/AGENTS.md`

这是项目级规则。所有 agent 在改代码前都应该先读它。和 i18n 相关的核心要求是：

- React 用户可见文案必须使用 `@zhiyu/shared-i18n`。
- 英文是源文案。
- 新 key 必须同步所有语言。
- placeholder 必须一致。
- 修改资源后运行 `pnpm --filter @zhiyu/shared-i18n test`。

### `system/.claude/rules/i18n.md`

这是面向 Claude/Codex 类 agent 的细分规则。它通过 glob 覆盖：

- `packages/shared-i18n/src/**`
- `packages/shared-config/src/locales.ts`
- `apps/**/*.tsx`
- `apps/**/*.ts`

如果后续接入其他 agent 平台，可以把同样规则复制成对应平台的 rules 或 memory 文件。

## 推荐 Agent 工作流

当 AI agent 处理任何 UI 变更时，按这个流程执行：

1. 读取 `AGENTS.md` 和本 README。
2. 确认当前支持语言来自 `packages/shared-config/src/locales.ts`。
3. 搜索目标页面中已有 `useTranslation` 和 `t(...)` 用法。
4. 新增文案先写 `en.ts`。
5. 翻译并补齐 `zh.ts`、`vi.ts`、`th.ts`、`id.ts`。
6. 替换 JSX 中的硬编码文案。
7. 保持业务内容继续使用 `pickI18n`，不要塞进 UI 文案包。
8. 运行 `pnpm --filter @zhiyu/shared-i18n test`。
9. 运行相关 typecheck。
10. 用 `rg` 巡检硬编码。
11. 用浏览器切换所有语言做冒烟测试。
12. 在 PR 或提交说明中列出新增 key、测试结果、未覆盖风险。

## Skills 和工具使用建议

当前维护多语言时常用这些能力：

| 场景 | 推荐工具或 skill | 用途 |
| --- | --- | --- |
| 修改 React UI | 普通 Codex 编辑能力 | 添加 `t(...)`、维护 locale 文件、跑测试 |
| 本地浏览器检查 | `browser-use:browser` 或 Browser 插件 | 打开 localhost、切换语言、点击页面、看 console |
| GitHub 发布 | `github:yeet` | 检查 diff、建分支、提交、推送、开 PR |
| 修复 PR 反馈 | `github:gh-address-comments` | 读取 review comments 并逐条修复 |
| 修复 CI | `github:gh-fix-ci` | 查看 GitHub Actions 日志并修复失败 |
| 设计或改 UI 布局 | `frontend-design` | 仅当涉及视觉和交互设计时使用 |
| 性能相关 React 改动 | `vercel-react-best-practices` | 仅当涉及 React 性能、渲染、bundle 时使用 |

不建议为了普通翻译任务使用图片、文档、表格等无关 skill。

## PR 描述模板

```md
## Summary

- Added/updated i18n keys for ...
- Replaced hardcoded UI copy in ...
- Updated locale resources for zh/en/vi/th/id.

## Validation

- pnpm --filter @zhiyu/shared-i18n test
- pnpm --filter @zhiyu/web-app typecheck
- Browser smoke: zh/en/vi/th/id language switch on ...

## Notes

- English is the source copy.
- Uncertain translations: none / list here.
- Known existing issues not caused by this PR: ...
```

## 新增语言流程

新增语言是产品级变更，不要只改一个文件。流程：

1. 在 `packages/shared-config/src/locales.ts` 增加 locale code 和 label。
2. 在 `packages/shared-i18n/src/` 新增对应语言文件。
3. 从 `en.ts` 复制结构，翻译所有 leaf string。
4. 在 `packages/shared-i18n/src/index.ts` import 并加入 `RESOURCES`。
5. 确认 `apps/web-app/src/app/i18n.ts` 的语言检测逻辑是否需要扩展。
6. 确认 `Layout.tsx` 语言切换器展示正常。
7. 确认 API、数据库、seed、`*_i18n` 字段是否也要支持这个 locale。
8. 更新 `AGENTS.md`、`.claude/rules/i18n.md` 和本 README。
9. 运行 i18n test、typecheck、浏览器 QA。

## 常见问题

### 为什么英文是源文案，但默认语言是中文？

这是两个不同概念：

- 源文案语言：开发和翻译的基准，当前是 `en`。
- 默认显示语言：用户没有选择且浏览器语言无法匹配时显示什么，当前是 `zh`。

英文作为源文案有利于 AI 翻译和长期国际化维护；中文默认显示符合当前产品主要用户。

### 可以在 JSX 里临时写中文吗？

不可以。即使是很小的按钮，也要进 `shared-i18n`。临时文案最容易变成永久技术债。

### 可以只补中文和英文，其他语言以后再说吗？

不可以。当前支持语言是 `zh/en/vi/th/id`，key 必须同次补齐。否则用户切换语言时会看到 fallback 或缺失文案。

### 翻译不确定怎么办？

先给出最合理的自然翻译，并在 PR summary 的 Notes 中说明不确定点。不要在 TS 文案对象里写 TODO 注释。

### UI 文案和课程内容都叫多语言，为什么分开？

因为生命周期不同。UI 文案随代码发布，课程、文章、题库内容随数据和内容系统更新。混在一起会让发布、审核、回滚都变复杂。

## 最小维护清单

每次合并 i18n 相关改动前，至少确认：

- `en.ts` 有源文案。
- `zh.ts`、`vi.ts`、`th.ts`、`id.ts` key 完整。
- 没有空字符串。
- placeholder 完全一致。
- React UI 使用 `t(...)`。
- 内容型数据继续使用 `pickI18n(...)`。
- `pnpm --filter @zhiyu/shared-i18n test` 通过。
- 关键页面切换所有语言后没有明显硬编码 UI 文案。

# 国际化核心规范

> **阶段**：B01-A 技术架构
> **冻结状态**：已冻结

---

## 语言列表与默认

| Locale | 语言 | 说明 |
|--------|------|------|
| `zh` | 中文 | 默认显示语言 |
| `en` | English | UI 源文案语言、fallback 语言 |
| `vi` | Tiếng Việt | 越南语 |
| `th` | ไทย | 泰语 |
| `id` | Bahasa Indonesia | 印尼语 |

## 决策

| 项目 | 决定 |
|------|------|
| 源文案语言 | `en`（英文先写，再翻译其他语言） |
| 默认显示语言 | `zh`（浏览器无法匹配时的回退） |
| fallbackLng | `en`（翻译缺失时暴露英文，不静默显示其他语言） |
| 语言检测 | `localStorage` > `navigator.language` > 默认 `zh` |

> 源文案语言和默认显示语言是两个独立概念。英文作为源文案有利于 AI 翻译和国际化维护；中文默认显示符合主要用户群。

## 技术栈

| 组件 | 选型 | 说明 |
|------|------|------|
| 运行时核心 | `i18next` | 国际化运行时 |
| React 接入 | `react-i18next` | hooks 和组件绑定 |
| 资源格式 | TypeScript 模块（`en.ts`, `zh.ts` 等） | 非 JSON，支持嵌套和类型约束 |
| 共享资源包 | `packages/shared-i18n` | 集中保存 UI 文案资源 |
| 共享配置包 | `packages/shared-config` | locale 列表、默认语言、语言展示名 |
| 类型约束 | `ResourceShape = typeof en` | 其他语言结构必须与 en 一致 |
| 校验脚本 | `verify-i18n.ts` | 检查 key 完整、值非空、placeholder 一致 |

## 为什么用 TypeScript 文案文件

- monorepo package 中直接导出资源
- 以英文源文案约束整体结构（`ResourceShape = typeof en`）
- 支持嵌套对象，适合按模块组织
- 后续可从 TS 资源生成 JSON 对接 TMS

## 初始化逻辑

```typescript
// 语言检测优先级
function detect(): Locale {
  const saved = localStorage.getItem('zhiyu-locale');
  if (saved && LOCALES.includes(saved)) return saved;
  const nav = navigator.language.toLowerCase();
  // 按前缀匹配：zh→zh, vi→vi, th→th, id→id, en→en
  // 无匹配 → DEFAULT_LOCALE (zh)
}

// 初始化配置
i18n.init({
  resources: Object.fromEntries(
    LOCALES.map(l => [l, { translation: RESOURCES[l] }])
  ),
  lng: detect(),
  fallbackLng: 'en',
  interpolation: { escapeValue: false },
});

// 切换语言：同时更新 i18next 和 localStorage
function setLocale(l: Locale) {
  i18n.changeLanguage(l);
  localStorage.setItem('zhiyu-locale', l);
}
```

## Locale 配置源码规范

```typescript
// packages/shared-config/src/locales.ts
export const LOCALES = ['zh', 'en', 'vi', 'th', 'id'] as const;
export type Locale = (typeof LOCALES)[number];
export const DEFAULT_LOCALE: Locale = 'zh';
export const LOCALE_LABEL: Record<Locale, string> = {
  zh: '中文', en: 'English', vi: 'Tiếng Việt', th: 'ไทย', id: 'Bahasa Indonesia',
};
```

> 业务代码禁止手写 locale union，统一从 `@zhiyu/shared-config` 引入 `Locale`。

## 新增语言流程

1. `packages/shared-config/src/locales.ts` 增加 locale code 和 label
2. `packages/shared-i18n/src/` 新增语言文件，从 en.ts 复制结构翻译
3. `packages/shared-i18n/src/index.ts` import 并加入 `RESOURCES`
4. 确认 `i18n.ts` 语言检测逻辑是否需扩展
5. 确认语言切换器展示正常
6. 确认 API、数据库、`*_i18n` 字段是否也要支持
7. 更新 agent 规则和本文档
8. 运行 i18n test + typecheck + 浏览器 QA

---

## 99. 待确认问题

无

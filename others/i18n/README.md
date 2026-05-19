# Zhiyu i18n Design Share

这份目录是从 Zhiyu 项目中抽出的国际化设计与实现样例，保留了原项目的相对路径，方便复制到其他 React / monorepo 项目中参考。

## 包含内容

```txt
i18n-design-share/
  README.md
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
        tsconfig.json
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
```

## 文件用途

- `system/packages/shared-i18n/README.md`：完整的多语言维护手册，建议先读这个。
- `system/packages/shared-i18n/src/*.ts`：当前 UI 文案资源，英文是源文案，支持 `zh/en/vi/th/id`。
- `system/packages/shared-i18n/scripts/verify-i18n.ts`：检查 key 完整性、空翻译、placeholder 一致性。
- `system/packages/shared-config/src/locales.ts`：当前支持语言、默认语言和语言展示名。
- `system/apps/web-app/src/app/i18n.ts`：React web-app 的 `i18next` 初始化方式。
- `system/apps/web-app/src/app/Layout.tsx`：语言切换器和实际 UI 使用方式示例。
- `system/apps/web-app/src/lib/china-types.ts`：业务内容 `*_i18n` 字段的读取和 fallback 示例。
- `system/AGENTS.md`：项目级 AI agent 国际化规则。
- `system/.claude/rules/i18n.md`：Claude/Codex 类 agent 的 i18n 专项规则。

## 推荐阅读顺序

1. `system/packages/shared-i18n/README.md`
2. `system/packages/shared-config/src/locales.ts`
3. `system/packages/shared-i18n/src/en.ts`
4. `system/packages/shared-i18n/scripts/verify-i18n.ts`
5. `system/apps/web-app/src/app/i18n.ts`
6. `system/apps/web-app/src/app/Layout.tsx`
7. `system/AGENTS.md`
8. `system/.claude/rules/i18n.md`

## 迁移到其他项目的最小集合

普通 React 项目最少需要这几块：

- 一个 `i18next` 初始化文件。
- 一组 locale 资源文件。
- 一个语言列表配置。
- 一个语言切换器。
- 一个 key 完整性测试。
- 一份 agent / contributor 规则。

当前目录保留了更完整的实现，包括 UI 文案和业务内容 `*_i18n` 的边界说明。

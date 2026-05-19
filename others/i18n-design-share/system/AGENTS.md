# Project Rules

## i18n Rules

- Read `packages/shared-i18n/README.md` before making substantial i18n changes.
- All user-facing React UI text must use i18n keys from `@zhiyu/shared-i18n`.
- Do not hardcode visible UI copy directly in `.tsx` files, except test fixtures, debug-only text, or data examples that are not product UI.
- English (`en`) is the source language for product copy.
- Supported locales are `zh`, `en`, `vi`, `th`, and `id`; keep this list in sync with `packages/shared-config/src/locales.ts` and `packages/shared-i18n/src/index.ts`.
- When adding a new key, add it to every locale file in the same change.
- Keep keys stable. Do not rename keys unless necessary.
- Prefer short, product-style copy.
- Translations should be natural, not machine-literal.
- Preserve placeholders exactly across languages, for example `{{name}}` and `{{count}}`.
- If a translation is uncertain, mention it in the PR summary instead of adding comments inside locale modules.
- Run `pnpm --filter @zhiyu/shared-i18n test` after changing i18n resources.

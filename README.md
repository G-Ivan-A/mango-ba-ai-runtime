---
status: runtime
version: 0.5
meta_model_version: 0.4
updated: 2026-09-26
---

# Mango BA AI Runtime — MVP BCREQ 0.5

Репозиторий, на который БА ссылается при работе в чате модели. Маршрут
`A-IN → A-CORE → A-BCREQ` исполняет модель по системным промптам из этого
репозитория; итог — бизнес-требование `A-BCREQ` в Markdown. Репозиторий не
привязан к среде и варианту развёртывания.

## Первый запуск

1. Откройте [быстрый старт](docs/guides/00-quick-start.md).
2. Откройте новый чат модели для новой задачи, дайте ссылку на этот
   репозиторий и вставьте пример из быстрого старта. Один чат — одна задача.
3. Получите `A-BCREQ` в диалоге.

Все инструкции: [docs/guides/README.md](docs/guides/README.md).

## Состав

| Путь | Назначение |
| --- | --- |
| `AGENTS.md` | загрузочный системный промпт |
| `skills/` | 11 навыков узлов MVP |
| `contracts/` | системные промпты-контракты `C-IN`, `C-CORE`, `C-QUEST`, `C-OUT-BCREQ`, `C-RK` |
| `taxonomy/`, `routes/` | закрытые словари и граф маршрута |
| `taxonomy/mango-products.yaml` | закрытый каталог продуктов Mango (Domain → Capability → Feature → Atomic Function); значение `atomic_function` берётся из него по id |
| `taxonomy/domain-glossary*.yaml` | словарь домена на продуктовый класс: `domain-glossary.yaml` — `contact-center`, `domain-glossary-voice-ucaas.yaml`, `domain-glossary-analytics-reporting.yaml`; пары `confusable_with` — источник отрицательных эталонов (EP-G7) |
| `templates/`, `golden/`, `evaluation/` | шаблоны, эталоны, гейты и промпт `G-mach` |
| `golden/cases*.yaml` | Golden Set на продуктовый класс: `cases.yaml` — `contact-center` (читает `G-mach`), `cases-voice-ucaas.yaml`, `cases-analytics-reporting.yaml`; `atomic_function` случая — функция каталога класса набора |
| `docs/kb/` | база знаний (уровень `ST-5-LOCAL`) |
| `docs/guides/` | пошаговые инструкции для пользователя |

## Маршрутизация знаний

Порядок: материал задачи → корпоративная БЗ → Confluence → публичные ресурсы
Манго → внешние системы → `docs/kb` → вопрос человеку. Работу с внешними
базами знаний регламентирует сама модель: недоступный уровень пропускается с
записью причины и работу не блокирует.

`docs/kb/` — копия `kb/processed` из
[`mango_ba_prompts`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/kb/processed).
Навигация: [`docs/kb/MAP.json`](docs/kb/MAP.json) →
`docs/kb/maps/<документ>.json` → `sections/NN-*.md`.
Порядок выбора и повторного поиска: [`docs/kb/USAGE.md`](docs/kb/USAGE.md).

## Версии и происхождение

- пакет: `0.5`; зависимость от мета-модели: `0.4`;
- исходные снимки и SHA записаны в `compilation-manifest.yaml`.

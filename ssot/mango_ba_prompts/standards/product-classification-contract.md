---
status: draft
version: 0.1
updated: 2026-06-04
ai-generated: true
type: contract
scope: mango-only
glossary_ref: "standards/GLOSSARY.md"
research_dep:
  - "docs/hub-research-dependencies.md#classification"
  - "docs/hub-research-dependencies.md#taxonomy-concept"
related_standards:
  - "standards/GLOSSARY.md"
source_hub: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/038868dd125b4e2d849ff73604890f1d2787ac0f/projects/mango/standards/classification-glossary.md"
source_sha: "038868dd125b4e2d849ff73604890f1d2787ac0f"
---

# Product Classification Contract

Версия: 0.1

Дата исходного Hub-артефакта: 2026-05-26

Дата миграции в спок: 2026-06-04

Этот контракт фиксирует Mango-specific терминологию классификации
функциональности для промптов, проектных артефактов и будущей capability
taxonomy Mango. Он не является общим глоссарием репозитория и не должен
блокировать другие проекты `hybrid-Intelligence-lab`.

Для значений общих терминов см. [`standards/GLOSSARY.md`](GLOSSARY.md). Этот
контракт задает классификацию `Domain -> Capability -> Feature -> Atomic
Function` и не смешивается с глоссарием терминов.

## Область применения

Контракт применяется только к Mango:

1. исследованиям Хаба, зарегистрированным через
   `docs/hub-research-dependencies.md`;
2. проектным артефактам в споке `mango_ba_prompts`;
3. будущим файлам Mango `kb/`, если они описывают продукты, требования,
   capability, feature, gap или coverage status.

Если термин нужен для другого проекта, его нужно согласовывать отдельно через
общий [`standards/GLOSSARY.md`](GLOSSARY.md), а не копировать Mango-иерархию как
обязательную.

## Правило применения

Все артефакты Mango, которые используют эту классификацию, ссылаются на
`standards/product-classification-contract.md`.

Исследовательские источники контракта указаны во frontmatter через
`research_dep` и должны резолвиться через единый реестр
`docs/hub-research-dependencies.md`, а не через Hub-relative пути.

Если входящий термин не находится в источниках или не имеет устойчивого аналога,
помечайте его как `⚠️ Требуется уточнение` и сохраняйте ближайший рабочий
mapping без блокировки анализа.

## Иерархия классификации

```text
Domain (Семейство)
  -> Capability (Класс)
    -> Feature (Подкласс)
      -> Atomic Function (Функция)
```

| Уровень | Назначение | Основной вопрос |
| --- | --- | --- |
| Domain | Крупная бизнес-область Mango. | В какой продуктовой или сервисной зоне находится требование? |
| Capability | Группа функций, решающая бизнес-задачу в домене. | Какую способность должен иметь продукт или команда? |
| Feature | Настраиваемая возможность внутри capability. | Что именно пользователь или администратор включает, настраивает или использует? |
| Atomic Function | Минимальная проверяемая единица функциональности. | Какую неделимую функцию, параметр или правило можно протестировать отдельно? |

## 🔹 Domain (Семейство)

**Определение**: крупная бизнес-область, объединяющая связанные возможности,
продукты, процессы и требования Mango.

**Источники**: TM Forum SID `Domain` как группировка связанных business
entities; UNSPSC `Segment` как верхний уровень товарно-сервисной классификации;
BABOK `domain` как сфера знаний с общими требованиями, терминологией и
функциональностью.

**Примеры Mango**: `voice-ucaas`, `contact-center`, `digital-channels`,
`ai-automation`, `analytics`, `hardware`, `security`.

**Правило**: domain не описывает конкретную функцию. Он нужен для маршрутизации,
владельца, верхнего отчета и границ анализа.

## 🔹 Capability (Класс)

**Определение**: группа функций, решающая конкретную бизнес-задачу в рамках
домена и выражающая способность продукта, сервиса или команды достигать
результата.

**Источники**: BABOK `capability`; TM Forum SID как общий язык сущностей CSP;
TM Forum eTOM для группировки действий service provider по customer, product,
service и resource areas.

**Примеры Mango**: `outbound-calling`, `call-recording`, `crm-integration`,
`realtime-analytics`, `omnichannel-routing`, `speech-analytics`.

**Правило**: capability формулируется достаточно крупно, чтобы объединять
несколько features, но достаточно конкретно, чтобы назначить owner и evidence.

## 🔹 Feature (Подкласс)

**Определение**: конкретная настраиваемая возможность внутри capability,
которая реализует связанный набор требований и дает ценность группе
stakeholders.

**Источники**: BABOK `feature`; IREB `functional requirement`; Mango research
`classification.md` для продуктовых примеров и текущих capability mappings.

**Примеры Mango**: `predictive-dialing`, `callback-scheduling`,
`agent-performance-dashboard`, `skill-based-routing`, `call-transcription`.

**Правило**: feature должна быть применима в пользовательском, админском или
интеграционном сценарии. Если элемент является только техническим параметром,
это обычно `Atomic Function`.

## 🔹 Atomic Function (Функция)

**Определение**: минимальная неделимая единица функциональности с
бизнес-ценностью или проверяемым эффектом, которую можно независимо описать,
настроить, протестировать или связать с acceptance criteria.

**Источники**: IREB requirement quality и `functional requirement`; IREB
`user story` как atomic backlog item в agile context; TM Forum product/service
modeling для atomic product/service specification. Термин `Atomic Function`
является Mango-specific адаптацией, а не отдельным общим стандартом.

**Примеры Mango**: `dial_ratio parameter`, `abandon_rate_limit threshold`,
`retry_interval configuration`, `recording_retention_days`,
`webhook_retry_policy`.

**Правило**: atomic function не делится дальше без потери смысла проверки. Если
параметр требует отдельной политики, SLA или compliance-review, это все равно
atomic function плюс overlay, а не новый domain.

## Маппинг терминов Mango

| Термин Mango | Международный аналог | Источник | Пример использования |
| --- | --- | --- | --- |
| Виртуальная АТС | UCaaS / Hosted PBX | TM Forum Product/Service, Mango `classification.md` | «Требование относится к domain `voice-ucaas` и capability `call-management`.» |
| Исходящий обзвон | Outbound Campaign / Outbound Contact | TM Forum Customer Interaction, Genesys Outbound | «Система должна поддерживать создание кампаний обзвона.» |
| Предиктивный набор | Predictive Dialing | Genesys Predictive Dialing; Cisco UCCE требует проверки версии | «Алгоритм должен учитывать доступность операторов перед набором.» |
| Обратный звонок | Callback / Callback Scheduling | TM Forum Customer Interaction, IREB Functional Requirement | «Клиент может заказать обратный звонок из очереди ожидания.» |
| Запись разговоров | Call Recording | TM Forum Service Usage / Customer Interaction, Mango `classification.md` | «Разговор должен сохраняться с retention policy и правами доступа.» |
| Голосовое меню IVR | Interactive Voice Response (IVR) | TM Forum Customer Interaction, contact-center practice | «IVR маршрутизирует клиента по выбранному пункту меню.» |
| Распределение звонков | Automatic Call Distribution / Routing | TM Forum Customer Interaction, contact-center practice | «Очередь должна распределять звонки по skill-based routing.» |
| Омниканальные коммуникации | Omnichannel Customer Interaction | TM Forum Customer Centricity, TM Forum eTOM | «Оператор работает с голосом, чатом и email в едином окне.» |
| Рабочее место оператора | Agent Desktop | UNSPSC Contact Center Software, contact-center practice | «Оператор видит карточку обращения и историю контактов.» |
| Речевая аналитика | Speech Analytics / Voice Recognition Software | UNSPSC `43233413`, Mango `classification.md` | «Система анализирует записи звонков по чек-листу качества.» |
| Управление качеством | Quality Management / Compliance Software | TM Forum Service Assurance, UNSPSC `43232606` | «Супервизор проверяет оценку качества и спорные звонки.» |
| WFM / управление персоналом | Workforce Management | Contact-center practice, TM Forum operations mapping | «Планирование смен учитывает прогноз входящей нагрузки.» |
| Интеграция с CRM | CRM Integration / External Interface | BABOK External Interface, TM Forum Open APIs | «Система передает событие звонка во внешнюю CRM.» |
| Webhook / API | Open API / Event Notification | TM Forum Open APIs, BABOK Interface | «Webhook повторяет доставку события при временной ошибке.» |
| Коллтрекинг | Call Tracking / Marketing Attribution | TM Forum Market & Sales, Mango `classification.md` | «Динамический номер связывает звонок с рекламным источником.» |
| Сквозная аналитика | End-to-End Marketing Analytics | ⚠️ Требуется уточнение: точный стандартный термин зависит от модели атрибуции | «Отчет связывает расходы, обращения, сделки и ROMI.» |

## Термины для уточнения

| Термин Mango | Почему требуется уточнение | Рабочий подход |
| --- | --- | --- |
| Робот-администратор | В международных источниках нет одного устойчивого аналога для Mango product naming. | Маппить как `virtual assistant` или `conversational automation` после проверки product evidence. |
| Сквозная аналитика | Встречается как продуктовый и маркетинговый термин, но не как единый стандартный класс. | Разделять `marketing attribution`, `analytics reporting`, `data integration` и compliance overlay. |
| Карусельные номера | Термин связан с локальным операторским сценарием и может иметь разные реализации. | Маппить через numbering/resource management и фиксировать уточняющий вопрос SME. |

## Связанные артефакты

- [README.md](../README.md) - навигация по споку `mango_ba_prompts`.
- [standards/GLOSSARY.md](GLOSSARY.md) - общий глоссарий терминов, не
  заменяемый этим Mango-only контрактом.
- `research_dep: docs/hub-research-dependencies.md#classification` - рабочая
  классификация продуктов MANGO OFFICE.
- `research_dep: docs/hub-research-dependencies.md#taxonomy-concept` -
  draft-концепция Unified Capability Taxonomy Mango.

## Источники

- TM Forum, Information Framework (SID):
  <https://www.tmforum.org/open-digital-architecture/information-framework-sid/>
- TM Forum, Business Process Framework (eTOM):
  <https://www.tmforum.org/oda/business/process-framework-etom/>
- IIBA, BABOK Guide Appendix A Glossary:
  <https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/glossary/>
- IREB, CPRE Glossary:
  <https://cpre.ireb.org/en/downloads-and-resources/glossary>
- UNDP, United Nations Standard Products and Services Code:
  <https://www.undp.org/unspsc>
- UNGM, UNSPSC browser and Excel export:
  <https://www.ungm.org/Public/UNSPSC>
- Genesys Documentation, Predictive Dialing Modes:
  <https://docs.genesys.com/Documentation/OU/8.1.5/Dep/DialingModes>

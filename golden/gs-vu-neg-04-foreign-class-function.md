---
golden_id: GS-VU-NEG-04
product_class: voice-ucaas
artifact_class: A-BCREQ
origin: synthetic
confirmed_by: none
status: draft
version: 0.2
updated: 2026-11-04
temperature: 0.1
---

# Негативный эталон GS-VU-NEG-04: функция чужого класса

Случай проверяет привязку функции к классу: функция каталога, в `classes`
которой нет объявленного класса, останавливает маршрут, а не меняет класс
прогона и не заменяется функцией класса.

## Вход

`A-IN`, `raw`, источник `SRC-01` — письмо маркетолога:

> «Нам нужен отдельный номер под каждую рекламную кампанию, чтобы было видно,
> откуда звонят.»

Реестр продуктов: маркер `А`, класс `voice-ucaas`, atomic function
`call-tracking/function/dynamic-number-substitution`, профиль `P-SETTINGS`,
владелец — маркетолог.

Функция есть в каталоге, но её `classes` — `["analytics-reporting"]`. В индексе
`golden/cases-voice-ucaas.yaml` поле `atomic_function` случая —
`number-management/function/number-assignment` (функция класса, о которой
сценарий в части выделения номеров); значение входа записано в
`declared_function`, проверка — `catalog_check: foreign-class`.

## Ожидаемый отказ

- узел `n1` (пакет `SK-transcript-normalization`), шаг проверки входа: пара
  «класс — функция» реестра не согласована с каталогом;
- причина — «функция чужого класса» (условие `c-in.products[]`);
- основание — правило 1 AGENTS.md (значение не подбирается) и правило 2 (класс
  объявлен до начала и не выводится из функции);
- лист прогона фиксирует `verdict: refused` и `outcome: refused`;
- `A-BCREQ` не формируется.

Недопустимые формы прохождения: агент меняет класс прогона на
`analytics-reporting` по функции или берёт функцию `voice-ucaas` вместо
объявленной.

## Зависимость от нормы

Как и в GS-CC-NEG-05: отказ — условие `c-in.products[]` (правило PT-5,
`contracts/c-in.md`), причина — «функция чужого класса»: `product_class`
записи не входит в `classes` узла. `check_golden` (пункты 6 и 8) проверяет
причину и пакет `refusing_pack` узла `n1`. Эталон synthetic и до
подтверждения человеком применяется структурно.

## Чего в эталоне намеренно нет

- Утверждения о доступности функции клиенту: каталог её не устанавливает
  (`availability: not-established-by-taxonomy`).

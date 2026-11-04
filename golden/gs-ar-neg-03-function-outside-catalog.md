---
golden_id: GS-AR-NEG-03
product_class: analytics-reporting
artifact_class: A-BCREQ
origin: synthetic
confirmed_by: none
status: draft
version: 0.2
updated: 2026-11-04
temperature: 0.1
---

# Негативный эталон GS-AR-NEG-03: функция вне каталога

Случай проверяет закрытость каталога функций `taxonomy/mango-products.yaml`:
функция, которой в каталоге нет, останавливает маршрут, а не заменяется
похожей.

## Вход

`A-IN`, `raw`, источник `SRC-01` — письмо директора по маркетингу:

> «Нужна выгрузка дашборда ROMI в PDF раз в неделю для собственника.»

Реестр продуктов: маркер `А`, класс `analytics-reporting`, atomic function
`romi-dashboard-export`, профиль `P-NO-SETTINGS`, владелец — директор по
маркетингу.

Значения `romi-dashboard-export` в каталоге нет. В индексе
`golden/cases-analytics-reporting.yaml` поле `atomic_function` случая —
`end-to-end-analytics/function/romi-calculation` (функция каталога, о которой
сценарий); значение входа записано в `declared_function`, проверка —
`catalog_check: outside-catalog`.

## Ожидаемый отказ

- узел `n1` (пакет `SK-transcript-normalization`), шаг проверки входа: функция
  реестра не найдена среди узлов `level: function` каталога;
- причина — «функция вне каталога» (условие `c-in.products[]`); основание —
  правило 1 AGENTS.md: значение вне закрытого словаря не изобретается и не
  подбирается;
- лист прогона фиксирует `verdict: refused` и `outcome: refused`;
- `A-BCREQ` не формируется.

Недопустимая форма прохождения: агент сам подбирает `romi-calculation` или
функцию отчётов и продолжает.

## Зависимость от нормы

Как и в GS-CC-NEG-05: отказ — условие `c-in.products[]` (правило PT-5,
`contracts/c-in.md`), причина — «функция вне каталога»; `check_golden`
(пункты 6 и 8) проверяет причину и пакет `refusing_pack` узла `n1`. Эталон
synthetic и до подтверждения человеком применяется структурно.

## Чего в эталоне намеренно нет

- Утверждения о доступности функции клиенту: каталог её не устанавливает
  (`availability: not-established-by-taxonomy`).

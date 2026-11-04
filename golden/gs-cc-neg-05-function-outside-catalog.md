---
golden_id: GS-CC-NEG-05
product_class: contact-center
artifact_class: A-BCREQ
origin: synthetic
confirmed_by: none
status: draft
version: 1.0
updated: 2026-11-04
temperature: 0.1
---

# Негативный эталон GS-CC-NEG-05: функция вне каталога

Эталон проверяет правило 1 `AGENTS.md` и условие `c-in.products[]`: функция
продукта — закрытое значение каталога `taxonomy/mango-products.yaml`. В отличие
от `GS-CC-NEG-01`…`GS-CC-NEG-04` отказ вызывает не пара терминов словаря домена,
а реестр продуктов входа, поэтому `glossary_pair` у эталона нет.

## Вход

`A-IN`, `raw`, источник `SRC-01` — расшифровка встречи:

> «Когда очередь переполнена, предлагайте абоненту обратный звонок вместо
> ожидания.»

Реестр продуктов: маркер `А`, класс `contact-center`, atomic function
`queue-callback-offer`, профиль `P-SETTINGS`, владелец — руководитель
контакт-центра.

`queue-callback-offer` — придуманный идентификатор прежней версии эталона
`GS-CC-01`. Узла с таким `id` в каталоге нет; ближайшие по смыслу узлы
(`call-routing/function/overflow-routing`,
`outbound-calling/function/callback-scheduling`) имеют другие `id`.

## Ожидаемый отказ

Прогон обязан **остановиться до первого шага**, а не подобрать похожее значение
каталога. Ожидаемый вердикт:

- узел `n1`, навык `transcript-normalization-contact-center`, шаг `check-schema`
  отказывает с основанием «функция вне каталога: `queue-callback-offer`»;
- лист прогона фиксирует `verdict: refused` и `outcome: refused`;
- `A-BCREQ` не формируется.

## Чего в эталоне намеренно нет

- Подстановки ближайшего `id` каталога: замена `queue-callback-offer` на
  `call-routing/function/overflow-routing` — именно тот дефект, который эталон
  обязан ловить.
- Вывода функции из текста источника: функция объявляется во входе, а не
  восстанавливается навыком.

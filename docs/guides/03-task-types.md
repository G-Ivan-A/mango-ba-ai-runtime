# Типы задач

## Расшифровка в бизнес-требование

```text
TASK-0002. Преобразуй приложенную расшифровку в A-BCREQ по RG-BCREQ-v1.
product_class=contact-center, profile=P-SETTINGS, projection=V-BIZ.
```

## Объявление продуктов задачи

Продукт задачи объявляется до запуска маршрута: `product_class`,
`atomic_function`, `profile` и владелец. Значение `atomic_function` берётся из
закрытого каталога продуктов [`taxonomy/mango-products.yaml`](../../taxonomy/mango-products.yaml)
по id узла `level: function`; придумывать функцию нельзя. Цепочка
Domain → Capability → Feature → Atomic Function читается по полю `parents`.
Если подходящей функции в каталоге нет или подходят две, не выбирайте
ближайшую: укажите это во входе как вопрос.

```text
TASK-0004. Продукт A: product_class=contact-center,
atomic_function=call-routing/function/queue-management, profile=P-SETTINGS,
владелец: Иван.
```

## Сырое требование в бизнес-требование

```text
TASK-0003. Сырое требование: в отчёте очереди нужен экспорт CSV.
Владелец: Ольга. Сформируй A-BCREQ; неизвестные факты вынеси в G-human.
```

## Уточнение незавершённого прогона

```text
Продолжи TASK-0003, RUN-0003. Ответ на Q-01: экспорт содержит выбранный период
и текущий набор фильтров. Не создавай новую задачу.
```

## Опциональные параметры

| Параметр | Допустимый пример | Зачем |
| --- | --- | --- |
| `projection` | `V-BIZ`, `V-APPROVE`, `V-DEV`, `V-CONTRACT` | адресат документа |
| `profile` | `P-SETTINGS`, `P-NO-SETTINGS`, `P-DEVICE`, `P-API` | профиль продукта |
| `source tiers` | `ST-1-CORPORATE`, `ST-5-LOCAL` | разрешённые источники |
| `language` | `ru` | язык контракта C-IN |

[← Процессы](02-processes.md) · [Далее: G-human →](05-human-review.md)

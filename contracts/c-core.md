---
type: system-prompt
contract: c-core
status: runtime
version: 0.5
updated: 2026-09-26
---

# C-CORE — контракт ядра требований

Это системный промпт-контракт. Модель, исполняющая узел маршрута, строит вход или выход строго по структуре ниже: имена полей, вложенность, обязательность и допустимые значения неизменны. Несоответствие контракту — отказ узла (fail-closed), а не предупреждение.

## Назначение

A-CORE — машиночитаемый промежуточный контракт между выявлением и специфицированием. Каждый элемент несёт ссылку на источник: элемент без source_ref не принадлежит ядру (GT-5, проверка check-source-evidence на ярусе G6).

## Структура

### `c-core`

Обязательные поля: `artifact_class`, `state`, `task_id`, `products`, `entities`, `actors`, `statements`, `constraints`, `metrics`, `ambiguities`. Поля вне перечня запрещены.

| Поле | Обязательно | Значение | Пояснение |
| --- | --- | --- | --- |
| `artifact_class` | да | константа `"A-CORE"` |  |
| `state` | да | одно из: `raw`, `draft`, `in-review`, `validated`, `approved`, `baselined`, `needs-clarification` |  |
| `task_id` | да | string (шаблон `^TASK-[0-9]{4}$`) |  |
| `products` | да | массив из (объект, см. ниже) (мин. элементов `1`) |  |
| `entities` | да | массив из (объект, см. ниже) |  |
| `actors` | да | массив из (объект, см. ниже) |  |
| `statements` | да | массив из (объект, см. ниже) (мин. элементов `1`) |  |
| `constraints` | да | массив из (объект, см. ниже) |  |
| `metrics` | да | массив из (объект, см. ниже) |  |
| `ambiguities` | да | массив из (объект, см. ниже) |  |
| `trace` | нет | массив из (объект, см. ниже) |  |

#### `c-core.entities[]`

Обязательные поля: `id`, `name`, `source_ref`. Поля вне перечня запрещены.

| Поле | Обязательно | Значение | Пояснение |
| --- | --- | --- | --- |
| `id` | да | string (шаблон `^ENT-[0-9]{2}$`) |  |
| `name` | да | string (мин. длина `1`) |  |
| `glossary_term` | нет | string |  |
| `source_ref` | да | ссылка `#/definitions/source_ref` |  |

#### `c-core.actors[]`

Обязательные поля: `id`, `role`, `kind`, `source_ref`. Поля вне перечня запрещены.

| Поле | Обязательно | Значение | Пояснение |
| --- | --- | --- | --- |
| `id` | да | string (шаблон `^ACT-[0-9]{2}$`) |  |
| `role` | да | string (мин. длина `1`) |  |
| `kind` | да | одно из: `human`, `agent`, `system` |  |
| `source_ref` | да | ссылка `#/definitions/source_ref` |  |

#### `c-core.statements[]`

Обязательные поля: `id`, `text`, `slot`, `atomic`, `source_ref`. Поля вне перечня запрещены.

| Поле | Обязательно | Значение | Пояснение |
| --- | --- | --- | --- |
| `id` | да | string (шаблон `^ST-[0-9]{2}$`) |  |
| `text` | да | string (мин. длина `1`) |  |
| `slot` | да | одно из: `S-PROBLEM`, `S-SCOPE`, `S-SOLUTION`, `S-FR`, `S-SETTINGS`, `S-UI`, `S-SCENARIO`, `S-AC`, `S-NFR`, `S-LIMITS`, `S-INTEGRATION` |  |
| `atomic` | да | boolean |  |
| `product_marker` | нет | string (шаблон `^[A-ZА-Я]$`) |  |
| `source_ref` | да | ссылка `#/definitions/source_ref` |  |

#### `c-core.constraints[]`

Обязательные поля: `id`, `subject`, `value`, `source_ref`. Поля вне перечня запрещены.

| Поле | Обязательно | Значение | Пояснение |
| --- | --- | --- | --- |
| `id` | да | string (шаблон `^CON-[0-9]{2}$`) |  |
| `subject` | да | string (мин. длина `1`) |  |
| `value` | да | string (мин. длина `1`) |  |
| `source_ref` | да | ссылка `#/definitions/source_ref` |  |

#### `c-core.metrics[]`

Обязательные поля: `id`, `name`, `value`, `unit`, `source_ref`. Поля вне перечня запрещены.

| Поле | Обязательно | Значение | Пояснение |
| --- | --- | --- | --- |
| `id` | да | string (шаблон `^MET-[0-9]{2}$`) |  |
| `name` | да | string (мин. длина `1`) |  |
| `value` | да | string \| number |  |
| `unit` | да | string (мин. длина `1`) |  |
| `source_ref` | да | ссылка `#/definitions/source_ref` |  |

#### `c-core.ambiguities[]`

Обязательные поля: `id`, `target_id`, `kind`, `severity`, `text`. Поля вне перечня запрещены.

| Поле | Обязательно | Значение | Пояснение |
| --- | --- | --- | --- |
| `id` | да | string (шаблон `^AMB-[0-9]{2}$`) |  |
| `target_id` | да | string (мин. длина `1`) |  |
| `kind` | да | одно из: `referential`, `quantitative`, `modal`, `terminological` |  |
| `severity` | да | одно из: `blocker`, `major`, `minor` |  |
| `text` | да | string (мин. длина `1`) |  |
| `resolved_by` | нет | string |  |

### Условие `definitions` для `c-core`

```json
{
  "source_ref": {
    "type": "object",
    "required": [
      "source_id",
      "locator",
      "quote"
    ],
    "additionalProperties": false,
    "properties": {
      "source_id": {
        "type": "string",
        "pattern": "^SRC-[0-9]{2}$"
      },
      "locator": {
        "type": "string",
        "minLength": 1
      },
      "quote": {
        "type": "string",
        "minLength": 1
      }
    }
  }
}
```

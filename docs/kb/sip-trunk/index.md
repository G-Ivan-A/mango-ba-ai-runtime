---
type: kb-source-index
doc_code: SIPT
doc_title: "SIP TRUNK. Руководство пользователя"
doc_version: "1.23.43"
status: extracted
ai-generated: true
source_document: "MO_SIP_Trunk.pdf"
extraction_date: "2026-08-25"
model_used: "pdfplumber 0.11.10 + PyMuPDF 1.28.2"
confidence_level: "high"
pages_covered: "1-42"
---

# SIP TRUNK. Руководство пользователя — индекс БЗ (карта разделов)

> Источник: `kb/sources/sip-trunk/MO_SIP_Trunk.pdf` · извлечено: pdfplumber 0.11.10 ·
> токены: tiktoken:cl100k_base. Это **карта поиска** для агента (замена
> retrieval-шага до RAG, ADR-007 R2): найди раздел по колонке «Когда
> обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия **high**. Неоднозначности помечены в разделах маркерами `❓ ТРЕБУЕТСЯ ПРОВЕРКА` / `⚠️ ПРОБЕЛ ИЗВЛЕЧЕНИЯ` с точной ссылкой «PDF + страница».

## Как цитировать

`[SIPT, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `kb/processed/<doc>/sections/<file>#<якорь>` (ADR-007 R3).

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-3 | ч.1 с.1-3 | 675 | SIP TRUNK |
| 1 | Термины и определения | [sections/01-terminy-i-opredeleniya.md](sections/01-terminy-i-opredeleniya.md) | 3 | ч.1 с.3 | 138 | DID-номера - телефонные номера, которые предоставляет MANGO OFFICE. |
| 2 | Что такое SIP Trunk | [sections/02-chto-takoe-sip-trunk.md](sections/02-chto-takoe-sip-trunk.md) | 3-4 | ч.1 с.3-4 | 262 | SIP Trunk – это виртуальный канал связи между вашей АТС (кАТС) и |
| 3 | Создание и редактирование SIP Trunk | [sections/03-sozdanie-i-redaktirovanie-sip-trunk.md](sections/03-sozdanie-i-redaktirovanie-sip-trunk.md) | 4 | ч.1 с.4 | 270 | В подразделе “Настройки SIP” раздела “Настройки и инструменты” Личного кабинета |
| 3 | 1. | [sections/04-1.md](sections/04-1.md) | 5 | ч.1 с.5 | 52 | — |
| 3 | 2. | [sections/05-2.md](sections/05-2.md) | 5 | ч.1 с.5 | 52 | — |
| 3 | 3. | [sections/06-3.md](sections/06-3.md) | 5 | ч.1 с.5 | 73 | — |
| 3.1 | Внешний SIP Trunk | [sections/07-vneshniy-sip-trunk.md](sections/07-vneshniy-sip-trunk.md) | 5 | ч.1 с.5 | 65 | — |
| 3.1.1 | Настройка | [sections/08-nastroyka.md](sections/08-nastroyka.md) | 5-8 | ч.1 с.5-8 | 1779 | В открывшейся вкладке Настройка заполните поля: |
| 3.1.2 | Номера | [sections/09-nomera.md](sections/09-nomera.md) | 8-9 | ч.1 с.8-9 | 639 | Заполните поля: |
| 3.1.3 | Маршрутизация | [sections/10-marshrutizaciya.md](sections/10-marshrutizaciya.md) | 9-11 | ч.1 с.9-11 | 1636 | Заполните поля: |
| 3.1.3.1 | Правила использование масок: | [sections/11-pravila-ispolzovanie-masok.md](sections/11-pravila-ispolzovanie-masok.md) | 11-12 | ч.1 с.11-12 | 493 | ● \d - одна цифра; |
| 3.1.3.2 | Правила преобразования номера: | [sections/12-pravila-preobrazovaniya-nomera.md](sections/12-pravila-preobrazovaniya-nomera.md) | 12 | ч.1 с.12 | 313 | ● $n - часть совпадения по шаблону, указанная в скобках; |
| 3.1.4 | Резервирование | [sections/13-rezervirovanie.md](sections/13-rezervirovanie.md) | 12-13 | ч.1 с.12-13 | 226 | На вкладке Резервирование следует задать список резервных SIP Trunk |
| 3.2 | Внутренний SIP Trunk | [sections/14-vnutrenniy-sip-trunk.md](sections/14-vnutrenniy-sip-trunk.md) | 13 | ч.1 с.13 | 67 | — |
| 3.2.1 | Настройка | [sections/15-nastroyka.md](sections/15-nastroyka.md) | 13-14 | ч.1 с.13-14 | 287 | Для настройки внутреннего SIP Trunk необходимо установить связь между двумя ВАТС, |
| 3.2.2 | Номера | [sections/16-nomera.md](sections/16-nomera.md) | 14-15 | ч.1 с.14-15 | 223 | Заполните поля: |
| 3.2.3 | Маршрутизация | [sections/17-marshrutizaciya.md](sections/17-marshrutizaciya.md) | 15-16 | ч.1 с.15-16 | 172 | При заполнении полей формы, руководствуйтесь инструкциями, предоставленными в |
| 3.3 | Активация SIP Trunk в карточке сотрудника | [sections/18-aktivaciya-sip-trunk-v-kartochke-sotrudn.md](sections/18-aktivaciya-sip-trunk-v-kartochke-sotrudn.md) | 16 | ч.1 с.16 | 361 | Чтобы установить SIP Trunk для исходящих вызовов конкретного сотрудника, откройте |
| 3 | 1. | [sections/19-1.md](sections/19-1.md) | 17 | ч.1 с.17 | 52 | — |
| 3 | 2. | [sections/20-2.md](sections/20-2.md) | 17 | ч.1 с.17 | 52 | — |
| 3 | 3. | [sections/21-3.md](sections/21-3.md) | 17 | ч.1 с.17 | 52 | — |
| 3 | 3.1. | [sections/22-3-1.md](sections/22-3-1.md) | 17 | ч.1 с.17 | 54 | — |
| 3 | 3.2. | [sections/23-3-2.md](sections/23-3-2.md) | 17 | ч.1 с.17 | 54 | — |
| 3 | 3.3. | [sections/24-3-3.md](sections/24-3-3.md) | 17 | ч.1 с.17 | 357 | Результат: звонок инициируется через определенный транк с префиксом |
| 3.4 | Редактирование SIP Trunk | [sections/25-redaktirovanie-sip-trunk.md](sections/25-redaktirovanie-sip-trunk.md) | 17 | ч.1 с.17 | 137 | Чтобы отредактировать созданный SIP Trunk кликните на наименование транка в списке |
| 3.5 | Удаление SIP Trunk | [sections/26-udalenie-sip-trunk.md](sections/26-udalenie-sip-trunk.md) | 17 | ч.1 с.17 | 286 | Чтобы удалить SIP Trunk, кликните по названию транка в списке транков на рабочей |
| 4 | Рабочая панель SIP Trunk | [sections/27-rabochaya-panel-sip-trunk.md](sections/27-rabochaya-panel-sip-trunk.md) | 17-18 | ч.1 с.17-18 | 165 | Рабочая панель SIP Trunk состоит из вкладок Список транков и Список правил |
| 4.1 | Список транков | [sections/28-spisok-trankov.md](sections/28-spisok-trankov.md) | 18 | ч.1 с.18 | 591 | Название транка - название транка, установленное пользователем; |
| 4.2 | Список правил маршрутизации | [sections/29-spisok-pravil-marshrutizacii.md](sections/29-spisok-pravil-marshrutizacii.md) | 18-19 | ч.1 с.18-19 | 241 | Маска набора номера - задается пользователем во вкладке «Маршрутизация»; |
| 5 | Настройка схемы распределения звонков в Личном кабинете | [sections/30-nastroyka-shemy-raspredeleniya-zvonkov-v.md](sections/30-nastroyka-shemy-raspredeleniya-zvonkov-v.md) | 19-22 | ч.1 с.19-22 | 837 | Личном кабинете |
| 6 | Примеры настройки звонков через SIP Trunk | [sections/31-primery-nastroyki-zvonkov-cherez-sip-tru.md](sections/31-primery-nastroyki-zvonkov-cherez-sip-tru.md) | 22-30 | ч.1 с.22-30 | 3627 | Для совершения исходящих вызовов ВАТС должна знать какой номер, в каком формате, |
| 7 | Конфигурация популярных PBX | [sections/32-konfiguraciya-populyarnyh-pbx.md](sections/32-konfiguraciya-populyarnyh-pbx.md) | 30 | ч.1 с.30 | 76 | ● Asterisk |
| 7.1 | Создание SIP trunk для FreePBX (Asterisk) | [sections/33-sozdanie-sip-trunk-dlya-freepbx-asterisk.md](sections/33-sozdanie-sip-trunk-dlya-freepbx-asterisk.md) | 30-35 | ч.1 с.30-35 | 2430 | Откройте меню администрирования транков во вкладке Trunks раздела |
| 7.1.1 | Как проверить состояние транка | [sections/34-kak-proverit-sostoyanie-tranka.md](sections/34-kak-proverit-sostoyanie-tranka.md) | 35 | ч.1 с.35 | 123 | Проверить состояние транка можно через меню Reports-Asterisk Info: |
| 7.1.2 | Исходящая маршрутизация | [sections/35-ishodyaschaya-marshrutizaciya.md](sections/35-ishodyaschaya-marshrutizaciya.md) | 35-38 | ч.1 с.35-38 | 995 | Outbound Routes - исходящая маршрутизация FreePBX. |
| 7.2 | Создание SIP trunk для FusionPBX (Freeswitch) | [sections/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw.md](sections/36-sozdanie-sip-trunk-dlya-fusionpbx-freesw.md) | 38-40 | ч.1 с.38-40 | 439 | Откройте меню администрирования транков во вкладке Gateways раздела |
| 7.2 | 7.2.1.Исходящая маршрутизация | [sections/37-7-2-1-ishodyaschaya-marshrutizaciya.md](sections/37-7-2-1-ishodyaschaya-marshrutizaciya.md) | 40-42 | ч.1 с.40-42 | 338 | Outbound Routes - Исходящая маршрутизация FusionPBX (Freeswitch). |
| 8 | Роли и права доступа. | [sections/38-roli-i-prava-dostupa.md](sections/38-roli-i-prava-dostupa.md) | 42 | ч.1 с.42 | 372 | В данном разделе приведено сводное описание параметров доступности, разрешений |
| | **ИТОГО** | | | | **19061** | весь документ |

## Источники

- Источник БЗ, часть 1: `kb/sources/sip-trunk/MO_SIP_Trunk.pdf`
- Стандарт цитирования: [`standards/kb-standard.md`](../../../standards/kb-standard.md), [ADR-007](../../../docs/adr/007-kb-standard.md)

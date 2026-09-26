---
type: kb-source-index
doc_code: ROLES
doc_title: "Руководство пользователя. Роли и права доступа"
doc_version: "1.26.08"
status: extracted
ai-generated: true
source_document: "Rolevaya-model-VATS_1_26_08.pdf"
extraction_date: "2026-08-22"
model_used: "pdfplumber 0.11.10 + PyMuPDF 1.28.2"
confidence_level: "high"
pages_covered: "1-59"
---

# Руководство пользователя. Роли и права доступа — индекс БЗ (карта разделов)

> Источник: `kb/sources/Rolevaya-model-vats/Rolevaya-model-VATS_1_26_08.pdf` · извлечено: pdfplumber 0.11.10 ·
> токены: tiktoken:cl100k_base. Это **карта поиска** для агента (замена
> retrieval-шага до RAG, ADR-007 R2): найди раздел по колонке «Когда
> обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия **high**. Неоднозначности помечены в разделах маркерами `❓ ТРЕБУЕТСЯ ПРОВЕРКА` / `⚠️ ПРОБЕЛ ИЗВЛЕЧЕНИЯ` с точной ссылкой «PDF + страница».

## Как цитировать

`[ROLES, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `kb/processed/<doc>/sections/<file>#<якорь>` (ADR-007 R3).

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-4 | ч.1 с.1-4 | 1715 | РУКОВОДСТВО |
| 1 | Общие сведения | [sections/01-obschie-svedeniya.md](sections/01-obschie-svedeniya.md) | 4-5 | ч.1 с.4-5 | 517 | Ролевая модель предназначена для разграничения прав доступа пользователей в системе. |
| 2 | Стандартные роли | [sections/02-standartnye-roli.md](sections/02-standartnye-roli.md) | 5-7 | ч.1 с.5-7 | 974 | В Виртуальной АТС MANGO OFFICE предусмотрены стандартные системные роли. |
| 3 | Управление ролями | [sections/03-upravlenie-rolyami.md](sections/03-upravlenie-rolyami.md) | 7 | ч.1 с.7 | 454 | Управление ролями выполняется в разделе: |
| 3.1 | Просмотр списка ролей | [sections/04-prosmotr-spiska-roley.md](sections/04-prosmotr-spiska-roley.md) | 7-8 | ч.1 с.7-8 | 259 | Список ролей отображается на странице управления ролями. |
| 3.2 | Создание роли | [sections/05-sozdanie-roli.md](sections/05-sozdanie-roli.md) | 8-9 | ч.1 с.8-9 | 472 | Создание роли позволяет определить новый набор прав доступа для пользователей системы. |
| 3.3 | Создание роли путем копирования | [sections/06-sozdanie-roli-putem-kopirovaniya.md](sections/06-sozdanie-roli-putem-kopirovaniya.md) | 9 | ч.1 с.9 | 164 | копирования |
| 3.3.1 | Копировать роль без запретов на изменение настроек | [sections/07-kopirovat-rol-bez-zapretov-na-izmenenie.md](sections/07-kopirovat-rol-bez-zapretov-na-izmenenie.md) | 9-11 | ч.1 с.9-11 | 937 | изменение настроек |
| 3.3.2 | Копировать роль | [sections/08-kopirovat-rol.md](sections/08-kopirovat-rol.md) | 11-12 | ч.1 с.11-12 | 538 | Данная строка меню доступна для нажатия если у пользователя активировано право доступа |
| 3.4 | Удаление роли | [sections/09-udalenie-roli.md](sections/09-udalenie-roli.md) | 12 | ч.1 с.12 | 216 | Удалить можно только пользовательские роли. |
| 3.5 | Сбросить настройки роли | [sections/10-sbrosit-nastroyki-roli.md](sections/10-sbrosit-nastroyki-roli.md) | 12-14 | ч.1 с.12-14 | 480 | Если права доступа роли были изменены, их можно вернуть к исходным значениям. |
| 4 | Настройка прав доступа роли | [sections/11-nastroyka-prav-dostupa-roli.md](sections/11-nastroyka-prav-dostupa-roli.md) | 14-16 | ч.1 с.14-16 | 1531 | роли |
| 4.1 | Гибкая настройка прав доступа с учетом ролей объекта | [sections/12-gibkaya-nastroyka-prav-dostupa-s-uchetom.md](sections/12-gibkaya-nastroyka-prav-dostupa-s-uchetom.md) | 16-19 | ч.1 с.16-19 | 1444 | учетом ролей объекта |
| 5 | Матрица ролей и прав доступа | [sections/13-matrica-roley-i-prav-dostupa.md](sections/13-matrica-roley-i-prav-dostupa.md) | 19 | ч.1 с.19 | 227 | В разделе описаны возможности подключения/отключения прав доступа, установленные по умолчанию для системных ролей. |
| 5.1 | Раздел «Сотрудники» | [sections/14-razdel-sotrudniki.md](sections/14-razdel-sotrudniki.md) | 19 | ч.1 с.19 | 77 | — |
| 5.1.1 | Выбор подконтрольных групп | [sections/15-vybor-podkontrolnyh-grupp.md](sections/15-vybor-podkontrolnyh-grupp.md) | 19 | ч.1 с.19 | 350 | — |
| 5.1.2 | Сотрудники и группы | [sections/16-sotrudniki-i-gruppy.md](sections/16-sotrudniki-i-gruppy.md) | 19-24 | ч.1 с.19-24 | 5463 | Роли и права доступа | v. |
| 5.2 | Раздел «Инструменты» | [sections/17-razdel-instrumenty.md](sections/17-razdel-instrumenty.md) | 24 | ч.1 с.24 | 77 | — |
| 5.2.1 | WFM | [sections/18-wfm.md](sections/18-wfm.md) | 24-25 | ч.1 с.24-25 | 1127 | Роли и права доступа | v. |
| 5.2.2 | Адресная книга | [sections/19-adresnaya-kniga.md](sections/19-adresnaya-kniga.md) | 25-26 | ч.1 с.25-26 | 901 | Роли и права доступа | v. |
| 5.2.3 | Аналитика | [sections/20-analitika.md](sections/20-analitika.md) | 26-27 | ч.1 с.26-27 | 293 | Роли и права доступа | v. |
| 5.2.4 | Аналитика Calltouch | [sections/21-analitika-calltouch.md](sections/21-analitika-calltouch.md) | 27 | ч.1 с.27 | 215 | — |
| 5.2.5 | Голосовые сообщения | [sections/22-golosovye-soobscheniya.md](sections/22-golosovye-soobscheniya.md) | 27-28 | ч.1 с.27-28 | 749 | Роли и права доступа | v. |
| 5.2.6 | Динамический коллтрекинг | [sections/23-dinamicheskiy-kolltreking.md](sections/23-dinamicheskiy-kolltreking.md) | 28 | ч.1 с.28 | 498 | — |
| 5.2.7 | Задачи | [sections/24-zadachi.md](sections/24-zadachi.md) | 28-29 | ч.1 с.28-29 | 340 | Роли и права доступа | v. |
| 5.2.8 | Заказ звонка | [sections/25-zakaz-zvonka.md](sections/25-zakaz-zvonka.md) | 29 | ч.1 с.29 | 221 | — |
| 5.2.9 | Запись разговоров | [sections/26-zapis-razgovorov.md](sections/26-zapis-razgovorov.md) | 29-32 | ч.1 с.29-32 | 2780 | Роли и права доступа | v. |
| 5.2.10 | История вызовов | [sections/27-istoriya-vyzovov.md](sections/27-istoriya-vyzovov.md) | 32 | ч.1 с.32 | 753 | — |
| 5.2.11 | Исходящий обзвон | [sections/28-ishodyaschiy-obzvon.md](sections/28-ishodyaschiy-obzvon.md) | 32-33 | ч.1 с.32-33 | 774 | Роли и права доступа | v. |
| 5.2.12 | Контроль качества | [sections/29-kontrol-kachestva.md](sections/29-kontrol-kachestva.md) | 33-34 | ч.1 с.33-34 | 860 | Роли и права доступа | v. |
| 5.2.13 | МангоМобайл | [sections/30-mangomobayl.md](sections/30-mangomobayl.md) | 34-35 | ч.1 с.34-35 | 299 | Роли и права доступа | v. |
| 5.2.14 | Обращения | [sections/31-obrascheniya.md](sections/31-obrascheniya.md) | 35-36 | ч.1 с.35-36 | 1276 | Роли и права доступа | v. |
| 5.2.15 | Отправка SMS | [sections/32-otpravka-sms.md](sections/32-otpravka-sms.md) | 36-37 | ч.1 с.36-37 | 340 | Роли и права доступа | v. |
| 5.2.16 | Отчеты Контакт-Центра | [sections/33-otchety-kontakt-centra.md](sections/33-otchety-kontakt-centra.md) | 37-39 | ч.1 с.37-39 | 2138 | Роли и права доступа | v. |
| 5.2.17 | Панель показателей | [sections/34-panel-pokazateley.md](sections/34-panel-pokazateley.md) | 39 | ч.1 с.39 | 262 | — |
| 5.2.18 | Раздел "Управление дозвоном" | [sections/35-razdel-upravlenie-dozvonom.md](sections/35-razdel-upravlenie-dozvonom.md) | 39-40 | ч.1 с.39-40 | 314 | Роли и права доступа | v. |
| 5.2.19 | Речевая аналитика | [sections/36-rechevaya-analitika.md](sections/36-rechevaya-analitika.md) | 40-41 | ч.1 с.40-41 | 626 | Роли и права доступа | v. |
| 5.2.20 | Роботы | [sections/37-roboty.md](sections/37-roboty.md) | 41 | ч.1 с.41 | 208 | — |
| 5.2.21 | Сделки | [sections/38-sdelki.md](sections/38-sdelki.md) | 41-42 | ч.1 с.41-42 | 792 | Роли и права доступа | v. |
| 5.2.22 | Скрипты | [sections/39-skripty.md](sections/39-skripty.md) | 42 | ч.1 с.42 | 228 | — |
| 5.2.23 | Статистика и мониторинг | [sections/40-statistika-i-monitoring.md](sections/40-statistika-i-monitoring.md) | 42-43 | ч.1 с.42-43 | 310 | Роли и права доступа | v. |
| 5.2.24 | Статический коллтрекинг | [sections/41-staticheskiy-kolltreking.md](sections/41-staticheskiy-kolltreking.md) | 43 | ч.1 с.43 | 230 | — |
| 5.2.25 | Текстовые рассылки | [sections/42-tekstovye-rassylki.md](sections/42-tekstovye-rassylki.md) | 43 | ч.1 с.43 | 223 | — |
| 5.2.26 | Управление звонками | [sections/43-upravlenie-zvonkami.md](sections/43-upravlenie-zvonkami.md) | 43-45 | ч.1 с.43-45 | 1007 | Роли и права доступа | v. |
| 5.2.27 | Управление сотрудниками | [sections/44-upravlenie-sotrudnikami.md](sections/44-upravlenie-sotrudnikami.md) | 45-46 | ч.1 с.45-46 | 1303 | Роли и права доступа | v. |
| 5.3 | Раздел «Обработка звонков» | [sections/45-razdel-obrabotka-zvonkov.md](sections/45-razdel-obrabotka-zvonkov.md) | 46 | ч.1 с.46 | 78 | — |
| 5.3.1 | Голосовое меню и распределение звонков | [sections/46-golosovoe-menyu-i-raspredelenie-zvonkov.md](sections/46-golosovoe-menyu-i-raspredelenie-zvonkov.md) | 46-48 | ч.1 с.46-48 | 1663 | Роли и права доступа | v. |
| 5.3.2 | Настройки дозвона и сообщений по умолчанию | [sections/47-nastroyki-dozvona-i-soobscheniy-po-umolc.md](sections/47-nastroyki-dozvona-i-soobscheniy-po-umolc.md) | 48 | ч.1 с.48 | 226 | — |
| 5.3.3 | Номера, подключенные к АТС | [sections/48-nomera-podklyuchennye-k-ats.md](sections/48-nomera-podklyuchennye-k-ats.md) | 48-49 | ч.1 с.48-49 | 778 | Роли и права доступа | v. |
| 5.3.4 | Переадресация по номеру клиента | [sections/49-pereadresaciya-po-nomeru-klienta.md](sections/49-pereadresaciya-po-nomeru-klienta.md) | 49 | ч.1 с.49 | 216 | — |
| 5.3.5 | Черный/белый список | [sections/50-chernyy-belyy-spisok.md](sections/50-chernyy-belyy-spisok.md) | 49-50 | ч.1 с.49-50 | 298 | Роли и права доступа | v. |
| 5.4 | Раздел «Настройки АТС» | [sections/51-razdel-nastroyki-ats.md](sections/51-razdel-nastroyki-ats.md) | 50 | ч.1 с.50 | 77 | — |
| 5.4.1 | Аудиофайлы | [sections/52-audiofayly.md](sections/52-audiofayly.md) | 50 | ч.1 с.50 | 270 | — |
| 5.4.2 | Безопасность и ограничения | [sections/53-bezopasnost-i-ogranicheniya.md](sections/53-bezopasnost-i-ogranicheniya.md) | 50-51 | ч.1 с.50-51 | 990 | Роли и права доступа | v. |
| 5.4.3 | Дополнительные настройки | [sections/54-dopolnitelnye-nastroyki.md](sections/54-dopolnitelnye-nastroyki.md) | 51-52 | ч.1 с.51-52 | 303 | Роли и права доступа | v. |
| 5.4.4 | Интеграции | [sections/55-integracii.md](sections/55-integracii.md) | 52 | ч.1 с.52 | 215 | — |
| 5.4.5 | Конференц-связь | [sections/56-konferenc-svyaz.md](sections/56-konferenc-svyaz.md) | 52-53 | ч.1 с.52-53 | 503 | Роли и права доступа | v. |
| 5.4.6 | Настройка SIP | [sections/57-nastroyka-sip.md](sections/57-nastroyka-sip.md) | 53-54 | ч.1 с.53-54 | 918 | Роли и права доступа | v. |
| 5.4.7 | Управление услугами | [sections/58-upravlenie-uslugami.md](sections/58-upravlenie-uslugami.md) | 54 | ч.1 с.54 | 215 | — |
| 5.5 | Раздел «Финансы» | [sections/59-razdel-finansy.md](sections/59-razdel-finansy.md) | 54 | ч.1 с.54 | 75 | — |
| 5.5.1 | Подключение Контакт-центра | [sections/60-podklyuchenie-kontakt-centra.md](sections/60-podklyuchenie-kontakt-centra.md) | 54-55 | ч.1 с.54-55 | 303 | Роли и права доступа | v. |
| 5.5.2 | Раздел "Финансы" и баланс Лицевого счета | [sections/61-razdel-finansy-i-balans-licevogo-scheta.md](sections/61-razdel-finansy-i-balans-licevogo-scheta.md) | 55-56 | ч.1 с.55-56 | 1080 | Роли и права доступа | v. |
| 5.5.3 | Смена тарифа и подключение услуг | [sections/62-smena-tarifa-i-podklyuchenie-uslug.md](sections/62-smena-tarifa-i-podklyuchenie-uslug.md) | 56-57 | ч.1 с.56-57 | 430 | Роли и права доступа | v. |
| 5.6 | Раздел «Поддержка» | [sections/63-razdel-podderzhka.md](sections/63-razdel-podderzhka.md) | 57 | ч.1 с.57 | 260 | — |
| 5.7 | Раздел «Функции Mango Talker» | [sections/64-razdel-funkcii-mango-talker.md](sections/64-razdel-funkcii-mango-talker.md) | 57-59 | ч.1 с.57-59 | 1523 | Роли и права доступа | v. |
| | **ИТОГО** | | | | **45383** | весь документ |

## Источники

- Источник БЗ, часть 1: `kb/sources/Rolevaya-model-vats/Rolevaya-model-VATS_1_26_08.pdf`
- Стандарт цитирования: [`standards/kb-standard.md`](../../../standards/kb-standard.md), [ADR-007](../../../docs/adr/007-kb-standard.md)

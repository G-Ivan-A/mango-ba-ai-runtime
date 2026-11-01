---
product_taxonomy_ref: taxonomy/products.yaml#classes
product_ids: [voice-ucaas]
type: kb-source-index
doc_code: APISC
doc_title: "Описание API «Сервер-клиент». API MANGO OFFICE"
doc_version: "18.09.2024"
status: extracted
ai-generated: true
source_document: "Api_server_client.pdf"
extraction_date: "2026-11-01"
model_used: "PyMuPDF 1.28.2 + pdfplumber 0.11.10 + tesseract OCR (rus+eng)"
confidence_level: "high"
pages_covered: "1-57"
---

# Описание API «Сервер-клиент». API MANGO OFFICE — индекс БЗ (карта разделов)

> Источник: `kb/sources/api-server-client/Api_server_client.pdf` (версия документа 18.09.2024, 57 с.). Исходный PDF в репозитории
> не хранится. Токены: tiktoken:cl100k_base. Это **карта поиска** для агента (ADR-007 R2): найди
> раздел по колонке «Когда обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия
> **high**. Отбор и описание иллюстраций: [`IMAGES.md`](IMAGES.md).

## Как цитировать

`[APISC, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `docs/kb/api-server-client/sections/<file>#<якорь>` (ADR-007 R3).

## Иллюстрации

Каждая содержательная иллюстрация в разделе сопровождается блоком
`> **Описание иллюстрации APISC-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста
руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.
OCR-текст — вспомогательный: факты цитируются по тексту руководства.

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-3 | ч.1 с.1-3 | 1128 | Описание API «Сервер-клиент» |
| — | Аннотация | [sections/01-annotaciya.md](sections/01-annotaciya.md) | 4 | ч.1 с.4 | 61 | В этом документе описаны основные принципы работы с API «Сервер-клиент», приведены примеры |
| 1 | Принципы интеграции и обработка ошибок | [sections/02-principy-integracii-i-obrabotka-oshibok.md](sections/02-principy-integracii-i-obrabotka-oshibok.md) | 4 | ч.1 с.4 | 0 | — |
| 1.1 | Назначение | [sections/03-naznachenie.md](sections/03-naznachenie.md) | 4 | ч.1 с.4 | 277 | API «Сервер-клиент» (далее по тексту – Сервис) позволяет внешним приложениям: |
| 1.2 | Требования совместимости и список поддерживаемых протоколов | [sections/04-trebovaniya-sovmestimosti-i-spisok-podde.md](sections/04-trebovaniya-sovmestimosti-i-spisok-podde.md) | 4 | ч.1 с.4 | 87 | Чтобы взаимодействовать с Сервисом, внешняя система должна обеспечивать: |
| 1.3 | Доступ к функциям | [sections/05-dostup-k-funkciyam.md](sections/05-dostup-k-funkciyam.md) | 5 | ч.1 с.5 | 167 | Сервис доступен по ссылке: |
| 1.4 | Обработка ошибок | [sections/06-obrabotka-oshibok.md](sections/06-obrabotka-oshibok.md) | 5 | ч.1 с.5 | 123 | В случае некорректных данных или при возникновении ошибок обработки данных любой из методо |
| 2 | Описание примеров использования Сервиса | [sections/07-opisanie-primerov-ispolzovaniya-servisa.md](sections/07-opisanie-primerov-ispolzovaniya-servisa.md) | 5 | ч.1 с.5 | 0 | — |
| 2.1 | Последовательность подключения Сервиса | [sections/08-posledovatelnost-podklyucheniya-servisa.md](sections/08-posledovatelnost-podklyucheniya-servisa.md) | 5-6 | ч.1 с.5-6 | 718 | 1) создать интеграцию, выполнив запрос создания интерации (/integration/create), при этом  |
| 2.2 | Корректное завершение работы приложения пользователя | [sections/09-korrektnoe-zavershenie-raboty-prilozheni.md](sections/09-korrektnoe-zavershenie-raboty-prilozheni.md) | 6 | ч.1 с.6 | 178 | 1) клиентское приложение завершает вебсокет сессию (вкладка браузера закрывается, выход из |
| 2.3 | Порядок получения пропущенных событий | [sections/10-poryadok-polucheniya-propuschennyh-sobyt.md](sections/10-poryadok-polucheniya-propuschennyh-sobyt.md) | 7 | ч.1 с.7 | 267 | 1) пользователь не залогинен в websocket-сессии; 2) все события, проходящие через систему, |
| 2.4 | Порядок инициирования звонка callback | [sections/11-poryadok-iniciirovaniya-zvonka-callback.md](sections/11-poryadok-iniciirovaniya-zvonka-callback.md) | 7 | ч.1 с.7 | 146 | 1) у пользователя открыт софтфон или иное настроенное средство приема; 2) выполняется запр |
| 2.5 | Порядок проигрывания записи | [sections/12-poryadok-proigryvaniya-zapisi.md](sections/12-poryadok-proigryvaniya-zapisi.md) | 7 | ч.1 с.7 | 165 | 1) осуществляется запись звонка более 6 секунд; 2) после получения события записи (/record |
| 2.6 | Порядок перевода на ответственного сотрудника | [sections/13-poryadok-perevoda-na-otvetstvennogo-sotr.md](sections/13-poryadok-perevoda-na-otvetstvennogo-sotr.md) | 8 | ч.1 с.8 | 207 | 1) при получении входящего звонка на ВАТС Сервис отправляет событие телефонии (/ivr) в ста |
| 2.7 | Звонки на группу | [sections/14-zvonki-na-gruppu.md](sections/14-zvonki-na-gruppu.md) | 8 | ч.1 с.8 | 182 | 1) происходит звонок на группу в ВАТС; 2) один из сотрудников группы поднял трубку; 3) ост |
| 3 | REST API | [sections/15-rest-api.md](sections/15-rest-api.md) | 9 | ч.1 с.9 | 0 | — |
| 3.1 | Описание запросов | [sections/16-opisanie-zaprosov.md](sections/16-opisanie-zaprosov.md) | 9 | ч.1 с.9 | 0 | — |
| 3.1.1 | Создание интеграции | [sections/17-sozdanie-integracii.md](sections/17-sozdanie-integracii.md) | 9-11 | ч.1 с.9-11 | 1251 | POST /v1/integration/create |
| 3.1.2 | Обновление интеграции | [sections/18-obnovlenie-integracii.md](sections/18-obnovlenie-integracii.md) | 11-12 | ч.1 с.11-12 | 1169 | POST /v1/integration/update/ Header[X-Mango-API-Token] |
| 3.1.3 | Удалить интеграцию | [sections/19-udalit-integraciyu.md](sections/19-udalit-integraciyu.md) | 13 | ч.1 с.13 | 307 | POST /v1/integration/delete/{token} |
| 3.1.4 | Установить настройки | [sections/20-ustanovit-nastroyki.md](sections/20-ustanovit-nastroyki.md) | 14 | ч.1 с.14 | 496 | POST /v1/settings/set/ Header[X-Mango-API-Token] |
| 3.1.5 | Получить настройки | [sections/21-poluchit-nastroyki.md](sections/21-poluchit-nastroyki.md) | 15 | ч.1 с.15 | 288 | POST /v1/settings/get/ Header[X-Mango-API-Token] |
| 3.1.6 | Создать пользователя (в интеграции) | [sections/22-sozdat-polzovatelya-v-integracii.md](sections/22-sozdat-polzovatelya-v-integracii.md) | 16-17 | ч.1 с.16-17 | 789 | POST /v1/users/create Header[X-Mango-API-Token] |
| 3.1.7 | Обновить пользователя (в интеграции) | [sections/23-obnovit-polzovatelya-v-integracii.md](sections/23-obnovit-polzovatelya-v-integracii.md) | 17-18 | ч.1 с.17-18 | 629 | POST /v1/users/update Header[X-Mango-API-Token] |
| 3.1.8 | Удалить пользователя (в интеграции) | [sections/24-udalit-polzovatelya-v-integracii.md](sections/24-udalit-polzovatelya-v-integracii.md) | 19-20 | ч.1 с.19-20 | 504 | POST /v1/users/delete Header[X-Mango-API-Token] |
| 3.1.9 | Получить статус пользователей (в интеграции) | [sections/25-poluchit-status-polzovateley-v-integraci.md](sections/25-poluchit-status-polzovateley-v-integraci.md) | 20-21 | ч.1 с.20-21 | 805 | POST /v1/users/state Header[X-Mango-API-Token] |
| 3.1.10 | Получить список пользователей (в интеграции) | [sections/26-poluchit-spisok-polzovateley-v-integraci.md](sections/26-poluchit-spisok-polzovateley-v-integraci.md) | 22-23 | ч.1 с.22-23 | 508 | GET /v1/users Header[X-Mango-API-Token] |
| 3.1.11 | Получить список пользователей (ВАТС) | [sections/27-poluchit-spisok-polzovateley-vats.md](sections/27-poluchit-spisok-polzovateley-vats.md) | 23-25 | ч.1 с.23-25 | 664 | POST /v1/vpbxusers/get/ |
| 3.1.12 | Получить вебсокет | [sections/28-poluchit-vebsoket.md](sections/28-poluchit-vebsoket.md) | 25-26 | ч.1 с.25-26 | 501 | GET /v1/channel/{userId} Header[X-Mango-API-Token] |
| 3.1.13 | Начать сессию вебсокета | [sections/29-nachat-sessiyu-vebsoketa.md](sections/29-nachat-sessiyu-vebsoketa.md) | 26-27 | ч.1 с.26-27 | 314 | POST /v1/session/register/{userId} Header[X-Mango-API-Token] |
| 3.1.14 | Завершить сессию вебсокета | [sections/30-zavershit-sessiyu-vebsoketa.md](sections/30-zavershit-sessiyu-vebsoketa.md) | 27-28 | ч.1 с.27-28 | 301 | POST /v1/session/unregister/{userId} Header[X-Mango-API-Token] |
| 3.1.15 | Проверка статуса сервера | [sections/31-proverka-statusa-servera.md](sections/31-proverka-statusa-servera.md) | 28 | ч.1 с.28 | 160 | Запрос без параметров. |
| 3.1.16 | Инициировать звонок | [sections/32-iniciirovat-zvonok.md](sections/32-iniciirovat-zvonok.md) | 29-30 | ч.1 с.29-30 | 453 | POST /v1/callback Header[X-Mango-API-Token] |
| 3.1.17 | Завершение звонка | [sections/33-zavershenie-zvonka.md](sections/33-zavershenie-zvonka.md) | 30-31 | ч.1 с.30-31 | 490 | POST /v1/callmanager/hangup Header[X-Mango-API-Token] |
| 3.1.18 | Отправить SMS | [sections/34-otpravit-sms.md](sections/34-otpravit-sms.md) | 31-32 | ч.1 с.31-32 | 577 | POST /v1/sms Header[X-Mango-API-Token] |
| 3.1.19 | Получение записи | [sections/35-poluchenie-zapisi.md](sections/35-poluchenie-zapisi.md) | 32-33 | ч.1 с.32-33 | 535 | GET /v1/record/{userId}/{recordingId} |
| 3.1.20 | Перевести на сотрудника | [sections/36-perevesti-na-sotrudnika.md](sections/36-perevesti-na-sotrudnika.md) | 34-35 | ч.1 с.34-35 | 462 | POST /v1/route/async/{userId}?TO={ext}&CALL_ID={callId}&TRANSACTION_ID={txId} Header[X-Man |
| 3.1.21 | Получить пропущенные события | [sections/37-poluchit-propuschennye-sobytiya.md](sections/37-poluchit-propuschennye-sobytiya.md) | 35-37 | ч.1 с.35-37 | 731 | POST /v1/notifications/missed/pull?USER_ID={ext}&LIMIT={limit} Header[X- Mango-API-Token] |
| 3.1.22 | Запрос статистики вызовов | [sections/38-zapros-statistiki-vyzovov.md](sections/38-zapros-statistiki-vyzovov.md) | 37-41 | ч.1 с.37-41 | 2346 | Доступность запроса определяется наличием включенной услуги на продукте ВАТС API_VBPX_STAT |
| 3.1.23 | Перевод (transfer) звонка | [sections/39-perevod-transfer-zvonka.md](sections/39-perevod-transfer-zvonka.md) | 42-43 | ч.1 с.42-43 | 582 | 3.1.23.1 "Слепой" перевод |
| 3.1.24 | КЦ. Получение информации о задании | [sections/40-kc-poluchenie-informacii-o-zadanii.md](sections/40-kc-poluchenie-informacii-o-zadanii.md) | 43-44 | ч.1 с.43-44 | 241 | POST /v1/cov/get_campaign_task_info?campaign_task_id={id} Header[X-Mango- API-Token] |
| 3.2 | События | [sections/41-sobytiya.md](sections/41-sobytiya.md) | 44 | ч.1 с.44 | 0 | — |
| 3.2.1 | События телефонии | [sections/42-sobytiya-telefonii.md](sections/42-sobytiya-telefonii.md) | 44-46 | ч.1 с.44-46 | 1004 | Параметр Тип Описание |
| 3.2.2 | События записи | [sections/43-sobytiya-zapisi.md](sections/43-sobytiya-zapisi.md) | 46 | ч.1 с.46 | 307 | Важно! Для внутренних разговоров события записи не передаются |
| 3.2.3 | Изменение статуса пользователя | [sections/44-izmenenie-statusa-polzovatelya.md](sections/44-izmenenie-statusa-polzovatelya.md) | 47 | ч.1 с.47 | 477 | routeKey="/user_state" |
| 3.2.4 | Информация ДКТ | [sections/45-informaciya-dkt.md](sections/45-informaciya-dkt.md) | 48-49 | ч.1 с.48-49 | 1075 | Параметр Тип Описание |
| 3.2.5 | Результат команды route/async/ | [sections/46-rezultat-komandy-route-async.md](sections/46-rezultat-komandy-route-async.md) | 49 | ч.1 с.49 | 147 | routeKey="/route_result" |
| 3.2.6 | Результат команды v1/callstat/request | [sections/47-rezultat-komandy-v1-callstat-request.md](sections/47-rezultat-komandy-v1-callstat-request.md) | 50 | ч.1 с.50 | 170 | Сообщает о готовности результатов запроса статистики. |
| 3.2.7 | Вебсокет закрыт со стороны сервера API | [sections/48-vebsoket-zakryt-so-storony-servera-api.md](sections/48-vebsoket-zakryt-so-storony-servera-api.md) | 50 | ч.1 с.50 | 46 | Получение пустой строки "". После получения такого message необходимо выполнить закрытие в |
| 4 | Справочники | [sections/49-spravochniki.md](sections/49-spravochniki.md) | 51 | ч.1 с.51 | 0 | — |
| 4.1 | Коды ответа JSON Result[code] | [sections/50-kody-otveta-json-result-code.md](sections/50-kody-otveta-json-result-code.md) | 51 | ч.1 с.51 | 100 | 103 Ошибочные параметры |
| 4.2 | Система Registration[system] | [sections/51-sistema-registration-system.md](sections/51-sistema-registration-system.md) | 51 | ч.1 с.51 | 46 | * Алгоритм по умолчанию |
| 4.3 | Состояние звонка | [sections/52-sostoyanie-zvonka.md](sections/52-sostoyanie-zvonka.md) | 51-52 | ч.1 с.51-52 | 391 | APPEARED Звонок в состоянии ожидания |
| 4.4 | Тип звонка | [sections/53-tip-zvonka.md](sections/53-tip-zvonka.md) | 52 | ч.1 с.52 | 347 | Входящий, к пользователю ВАТС с любого номера, не указанного у |
| 4.5 | Статус записи | [sections/54-status-zapisi.md](sections/54-status-zapisi.md) | 52 | ч.1 с.52 | 128 | NONE По звонку началась запись |
| 5 | Список кодов результатов | [sections/55-spisok-kodov-rezultatov.md](sections/55-spisok-kodov-rezultatov.md) | 53-56 | ч.1 с.53-56 | 4478 | Ниже приведен список кодов результатов выполнения команд или запросов, завершения вызовов, |
| 5 | Список изменений в документе | [sections/56-spisok-izmeneniy-v-dokumente.md](sections/56-spisok-izmeneniy-v-dokumente.md) | 57 | ч.1 с.57 | 203 | Изменение дизайна документа. |

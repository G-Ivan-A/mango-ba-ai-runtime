---
type: kb-source-index
doc_code: QM
doc_title: "Руководство по контролю качества"
doc_version: "1.26.18"
status: extracted
ai-generated: true
source_document: "QM_manual_v-1.26.18.pdf"
extraction_date: "2026-08-25"
model_used: "pdfplumber 0.11.10 + PyMuPDF 1.28.2"
confidence_level: "high"
pages_covered: "1-97"
---

# Руководство по контролю качества — индекс БЗ (карта разделов)

> Источник: `kb/sources/quality-managment/QM_manual_v-1.26.18.pdf` · извлечено: pdfplumber 0.11.10 ·
> токены: tiktoken:cl100k_base. Это **карта поиска** для агента (замена
> retrieval-шага до RAG, ADR-007 R2): найди раздел по колонке «Когда
> обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия **high**. Неоднозначности помечены в разделах маркерами `❓ ТРЕБУЕТСЯ ПРОВЕРКА` / `⚠️ ПРОБЕЛ ИЗВЛЕЧЕНИЯ` с точной ссылкой «PDF + страница».

## Как цитировать

`[QM, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `kb/processed/<doc>/sections/<file>#<якорь>` (ADR-007 R3).

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
| — | Титульная часть | [sections/00-titulnaya-chast.md](sections/00-titulnaya-chast.md) | 1-4 | ч.1 с.1-4 | 1153 | КОНТРОЛЬ КАЧЕСТВА |
| 1 | Быстрый старт | [sections/01-bystryy-start.md](sections/01-bystryy-start.md) | 4 | ч.1 с.4 | 120 | Руководство содержит описание работы с модулем "Контроль качества MANGO OFFICE". |
| 1.1 | Как подключить модуль Контроль качества в Личном кабинете | [sections/02-kak-podklyuchit-modul-kontrol-kachestva.md](sections/02-kak-podklyuchit-modul-kontrol-kachestva.md) | 4-5 | ч.1 с.4-5 | 776 | Доступ к модулю Контроль качества MANGO OFFICE осуществляется через браузер по адресу |
| 1.2 | Как добавить контролера | [sections/03-kak-dobavit-kontrolera.md](sections/03-kak-dobavit-kontrolera.md) | 5-6 | ч.1 с.5-6 | 341 | Контролёр – сотрудник ВАТС, оценивающий качество работы операторов по данным |
| 1.3 | Роли и функции | [sections/04-roli-i-funkcii.md](sections/04-roli-i-funkcii.md) | 6-9 | ч.1 с.6-9 | 2458 | Сводное описание параметров доступности, разрешений (прав) и функциональных возможностей |
| 2 | Настройка бланков оценки | [sections/05-nastroyka-blankov-ocenki.md](sections/05-nastroyka-blankov-ocenki.md) | 9 | ч.1 с.9 | 725 | Бланки оценок предназначены для оценки работы сотрудника контролером, по совокупности |
| 2.1 | Создание бланка оценки | [sections/06-sozdanie-blanka-ocenki.md](sections/06-sozdanie-blanka-ocenki.md) | 9-11 | ч.1 с.9-11 | 1411 | Бланк может быть создан двумя способами: |
| 2.2 | Просмотр и редактирование бланка оценки | [sections/07-prosmotr-i-redaktirovanie-blanka-ocenki.md](sections/07-prosmotr-i-redaktirovanie-blanka-ocenki.md) | 11-12 | ч.1 с.11-12 | 493 | Просмотр бланка доступен из рабочей области вкладки. |
| 2.3 | Настройка шкалы оценок и веса критериев | [sections/08-nastroyka-shkaly-ocenok-i-vesa-kriteriev.md](sections/08-nastroyka-shkaly-ocenok-i-vesa-kriteriev.md) | 12-13 | ч.1 с.12-13 | 548 | Для настройки шкалы и веса критериев кликните по кнопке «Настроить бланк». |
| 2.4 | Настройка апелляции | [sections/09-nastroyka-apellyacii.md](sections/09-nastroyka-apellyacii.md) | 13-15 | ч.1 с.13-15 | 802 | Для настройки оператору возможности подать апелляцию кликните по кнопке «Настроить бланк». |
| 2.5 | Удаление бланка оценки | [sections/10-udalenie-blanka-ocenki.md](sections/10-udalenie-blanka-ocenki.md) | 15 | ч.1 с.15 | 189 | Для удаления созданного ранее бланка откройте бланк и нажмите кнопку "Удалить". |
| 2.6 | Бланк оценки "Базовая оценка сотрудника" | [sections/11-blank-ocenki-bazovaya-ocenka-sotrudnika.md](sections/11-blank-ocenki-bazovaya-ocenka-sotrudnika.md) | 15-17 | ч.1 с.15-17 | 493 | Бланк настроен по умолчанию и содержит следующие поля: |
| 3 | Оценка обращений | [sections/12-ocenka-obrascheniy.md](sections/12-ocenka-obrascheniy.md) | 17 | ч.1 с.17 | 137 | Раздел меню Оценка обращений содержит три вкладки: |
| 3.1 | Оценка звонков | [sections/13-ocenka-zvonkov.md](sections/13-ocenka-zvonkov.md) | 17-27 | ч.1 с.17-27 | 7839 | Отчет "Оценка звонков" содержит данные о качестве работы сотрудников ВАТС в соответствии с |
| 3.2 | Оценка чатов | [sections/14-ocenka-chatov.md](sections/14-ocenka-chatov.md) | 27-32 | ч.1 с.27-32 | 3280 | Отчет предназначен для анализа и оценки эффективности текстовой коммуникации с клиентом. |
| 3.3 | Рандомайзер | [sections/15-randomayzer.md](sections/15-randomayzer.md) | 32-34 | ч.1 с.32-34 | 1003 | На вкладке контролер имеет возможность отбирать произвольные разговоры сотрудников |
| 4 | Настройка постзвонковой оценки | [sections/16-nastroyka-postzvonkovoy-ocenki.md](sections/16-nastroyka-postzvonkovoy-ocenki.md) | 34 | ч.1 с.34 | 181 | Для настройки постзвонковой оценки пройдите в раздел меню Настройки Постзвонковая |
| 4.1 | Настройка правил постзвонковой оценки | [sections/17-nastroyka-pravil-postzvonkovoy-ocenki.md](sections/17-nastroyka-pravil-postzvonkovoy-ocenki.md) | 34-38 | ч.1 с.34-38 | 2354 | Постзвонковая оценка качества предназначена для оценки: |
| 4.2 | Настройка уведомлений о постзвонковых оценках | [sections/18-nastroyka-uvedomleniy-o-postzvonkovyh-oc.md](sections/18-nastroyka-uvedomleniy-o-postzvonkovyh-oc.md) | 38-41 | ч.1 с.38-41 | 921 | В Личном кабинете пользователя ВАТС доступна услуга «Настройка уведомлений о постзвонковых |
| 5 | Запись экрана | [sections/19-zapis-ekrana.md](sections/19-zapis-ekrana.md) | 41 | ч.1 с.41 | 64 | — |
| 5.1 | Просмотр и скачивание записей | [sections/20-prosmotr-i-skachivanie-zapisey.md](sections/20-prosmotr-i-skachivanie-zapisey.md) | 41-43 | ч.1 с.41-43 | 2128 | Раздел предназначен для просмотра списка, выбора и скачивания видео-записей экрана |
| 5.2 | Просмотр настроек записи | [sections/21-prosmotr-nastroek-zapisi.md](sections/21-prosmotr-nastroek-zapisi.md) | 43-45 | ч.1 с.43-45 | 956 | Это окно предоставляет возможность управления правилами записи экрана для сотрудников |
| 5.3 | Назначение правил записи | [sections/22-naznachenie-pravil-zapisi.md](sections/22-naznachenie-pravil-zapisi.md) | 45-48 | ч.1 с.45-48 | 1601 | Администратор может настроить расписание для нескольких сотрудников таким образом, чтобы |
| 6 | Оценка качества в чатах | [sections/23-ocenka-kachestva-v-chatah.md](sections/23-ocenka-kachestva-v-chatah.md) | 48 | ч.1 с.48 | 458 | Вкладка Оценок качества в чатах предназначена для оценки работы сотрудника клиентом по |
| 6.1 | Создание, редактирование и удаление правила | [sections/24-sozdanie-redaktirovanie-i-udalenie-pravi.md](sections/24-sozdanie-redaktirovanie-i-udalenie-pravi.md) | 48-51 | ч.1 с.48-51 | 1145 | Чтобы создать новое правило оценки нажмите на кнопку «Добавить правило». |
| 7 | Статистика | [sections/25-statistika.md](sections/25-statistika.md) | 51 | ч.1 с.51 | 87 | Раздел содержит отчеты Динамика оценок и Сводная статистика. |
| 7.1 | Динамика оценок | [sections/26-dinamika-ocenok.md](sections/26-dinamika-ocenok.md) | 51-56 | ч.1 с.51-56 | 2435 | Отчет "Динамика оценок" содержит данные о качестве работы сотрудников ВАТС в соответствии с |
| 7.2 | Сводная статистика | [sections/27-svodnaya-statistika.md](sections/27-svodnaya-statistika.md) | 56-59 | ч.1 с.56-59 | 1032 | В разделе отображаются таблицы сводной статистики оценок сотрудников ВАТС клиентами и |
| 7.3 | Работа контролеров | [sections/28-rabota-kontrolerov.md](sections/28-rabota-kontrolerov.md) | 59-64 | ч.1 с.59-64 | 1980 | Отчет состоит четырех блоков: |
| 8 | Апелляции | [sections/29-apellyacii.md](sections/29-apellyacii.md) | 64 | ч.1 с.64 | 428 | KPI оператора зависит от оценок его разговоров. |
| 8.1 | Как сотруднику подать апелляцию | [sections/30-kak-sotrudniku-podat-apellyaciyu.md](sections/30-kak-sotrudniku-podat-apellyaciyu.md) | 64-65 | ч.1 с.64-65 | 465 | Если после получения уведомления сотрудник хочет подать апелляцию на пересмотр негативной |
| 8.2 | Как контролеру обрабатывать апелляции | [sections/31-kak-kontroleru-obrabatyvat-apellyacii.md](sections/31-kak-kontroleru-obrabatyvat-apellyacii.md) | 65-67 | ч.1 с.65-67 | 725 | Контролер обрабатывает апелляции следующим образом: |
| 9 | Речевая аналитика | [sections/32-rechevaya-analitika.md](sections/32-rechevaya-analitika.md) | 67 | ч.1 с.67 | 257 | Речевая аналитика — эффективный способ контролировать работу колл-центра. |
| 9.1 | Подключение услуги Речевая аналитика | [sections/33-podklyuchenie-uslugi-rechevaya-analitika.md](sections/33-podklyuchenie-uslugi-rechevaya-analitika.md) | 67-69 | ч.1 с.67-69 | 912 | Для подключения услуги "Речевая аналитика" в демо-режиме зайдите в Личный кабинет и найдите |
| 9.2 | Вкладка ОТЧЕТЫ | [sections/34-vkladka-otchety.md](sections/34-vkladka-otchety.md) | 69 | ч.1 с.69 | 395 | Вкладка Отчеты содержит детальную аналитическую информацию о распознанных вызовах в |
| 9.3 | Вкладка ТЕГИРОВАНИЕ РАЗГОВОРОВ | [sections/35-vkladka-tegirovanie-razgovorov.md](sections/35-vkladka-tegirovanie-razgovorov.md) | 69-72 | ч.1 с.69-72 | 1264 | Рабочая область вкладки «Тегирование разговоров» содержит список всех Тематик и ИИ Тематик, |
| 9.4 | Вкладка НАСТРОЙКИ | [sections/36-vkladka-nastroyki.md](sections/36-vkladka-nastroyki.md) | 72-73 | ч.1 с.72-73 | 1106 | Вкладка Настройки модуля Речевая аналитика содержит блок онбординга, а также следующие |
| 9.4.1 | Шаги онбординга | [sections/37-shagi-onbordinga.md](sections/37-shagi-onbordinga.md) | 73-75 | ч.1 с.73-75 | 1034 | В верхней части вкладки Настройки модуля находится блок онбординга, содержащего все этапы |
| 9.4.2 | Настройки распознавания записей | [sections/38-nastroyki-raspoznavaniya-zapisey.md](sections/38-nastroyki-raspoznavaniya-zapisey.md) | 75-77 | ч.1 с.75-77 | 1409 | Блок Настройка распознавания записей позволяет настроить функции распознавания и пересылки |
| 9.4.3 | Аналитика текстовых коммуникаций | [sections/39-analitika-tekstovyh-kommunikaciy.md](sections/39-analitika-tekstovyh-kommunikaciy.md) | 77-78 | ч.1 с.77-78 | 708 | Блок Аналитика текстовых коммуникаций позволяет настроить услугу аналитики текстовых |
| 9.4.4 | ИИ Инструменты | [sections/40-ii-instrumenty.md](sections/40-ii-instrumenty.md) | 78 | ч.1 с.78 | 73 | — |
| 9.4.4.1 | ИИ Конспекты | [sections/41-ii-konspekty.md](sections/41-ii-konspekty.md) | 78-81 | ч.1 с.78-81 | 1453 | Блок ИИ Конспекты позволяет автоматически формировать краткое содержание телефонных |
| 9.4.4.2 | ИИ Тегирование | [sections/42-ii-tegirovanie.md](sections/42-ii-tegirovanie.md) | 81-83 | ч.1 с.81-83 | 693 | Блок ИИ Тегирование позволяет настроить анализ разговоров сотрудников с использованием ИИ. |
| 9.4.4.3 | ИИ Помощники | [sections/43-ii-pomoschniki.md](sections/43-ii-pomoschniki.md) | 83 | ч.1 с.83 | 76 | — |
| 9.4.4.3.1 | Что это такое и зачем нужно | [sections/44-chto-eto-takoe-i-zachem-nuzhno.md](sections/44-chto-eto-takoe-i-zachem-nuzhno.md) | 83 | ч.1 с.83 | 406 | ИИ Помощники - это инструмент, который позволяет автоматически анализировать разговоры по |
| 9.4.4.3.2 | Как создать ИИ Помощника | [sections/45-kak-sozdat-ii-pomoschnika.md](sections/45-kak-sozdat-ii-pomoschnika.md) | 83-84 | ч.1 с.83-84 | 230 | 1. |
| 9.4.4.3.3 | Настройка ИИ Помощника | [sections/46-nastroyka-ii-pomoschnika.md](sections/46-nastroyka-ii-pomoschnika.md) | 84-87 | ч.1 с.84-87 | 1648 | 1. |
| 9.4.4.3.4 | Где смотреть результаты | [sections/47-gde-smotret-rezultaty.md](sections/47-gde-smotret-rezultaty.md) | 87-90 | ч.1 с.87-90 | 1631 | Чтобы посмотреть результат анализа: |
| 9.4.5 | Дополнительные настройки | [sections/48-dopolnitelnye-nastroyki.md](sections/48-dopolnitelnye-nastroyki.md) | 90-91 | ч.1 с.90-91 | 531 | Блок Дополнительные настройки позволяет пользователю управлять расширенными функциями |
| 9.4.6 | Отключение услуги | [sections/49-otklyuchenie-uslugi.md](sections/49-otklyuchenie-uslugi.md) | 91-93 | ч.1 с.91-93 | 347 | При необходимости пользователь может отключить услугу Речевая аналитика. |
| 9.5 | Вкладка ЗАЯВКИ | [sections/50-vkladka-zayavki.md](sections/50-vkladka-zayavki.md) | 93-97 | ч.1 с.93-97 | 1105 | Пользователь, который выбрал для распознавания технологию 3iTech, может отправить заявку на |
| 10 | Дополнительные возможности | [sections/51-dopolnitelnye-vozmozhnosti.md](sections/51-dopolnitelnye-vozmozhnosti.md) | 97 | ч.1 с.97 | 424 | В разделе «Дополнительные возможности» доступно подключение и настройка дополнительных |
| | **ИТОГО** | | | | **54430** | весь документ |

## Источники

- Источник БЗ, часть 1: `kb/sources/quality-managment/QM_manual_v-1.26.18.pdf`
- Стандарт цитирования: [`standards/kb-standard.md`](../../../standards/kb-standard.md), [ADR-007](../../../docs/adr/007-kb-standard.md)

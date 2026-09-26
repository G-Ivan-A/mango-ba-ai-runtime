---
id: vpbx-api-66-pryamaya-ssylka-na-zapis-razgovora-s-avt
doc_code: VPBXAPI
doc_title: "API Mango Office"
doc_version: "1.9"
section: "3.5.3"
pdf_section: "3.5.3"
title: "Прямая ссылка на запись разговора с авторизацией через Личный кабинет"
pdf_heading: "3.5.3 Прямая ссылка на запись разговора с авторизацией через Личный кабинет"
pages: "90"
source: kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf
source_part: "1"
source_pages: "ч.1: 90"
source_refs: '[{"source_pdf":"kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf","part":1,"pages":"90","global_pages":"90"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 639
status: extracted
ai-generated: true
---
# 3.5.3. Прямая ссылка на запись разговора с авторизацией через Личный кабинет

> Трассировка: PDF §3.5.3 · сквозные стр. 90 · источники: ч.1 `kb/sources/vpbx-api/MangoOffice_VPBX_API_v1.9.pdf` с.90.

GET /vpbx/queries/recording/issa/[recording_id]/[action] При обработке данного запроса API выполняет перенаправление (redirect) в Личный кабинет Виртуальной АТС, на этом роль API завершается и пользователь взаимодействует с Личным кабинетом напрямую. Если пользователь уже авторизован в Личном кабинете, выполнится проверка на права доступа к файлу для учетной записи пользователя, после чего будет выполнено еще одно перенаправление к сервису, предоставляющему доступ к файлам. Если пользователь не был авторизован в Личном кабинете (или в браузере не остались cookies), ему выдается запрос на аутентификацию (ввод логина и пароля), после прохождения которой, продолжиться обработка запроса на доступ к файлу. Возвращаемые в перенаправлениях ссылки являются временными, срок их жизни ограничен, после первого доступа к файлу ссылки будут недействительными, поэтому они не должны сохраняться внешней системой. Параметры:

| № | Параметры | Тип | Обяза-<br>тель-<br>ный | Описание |
| --- | --- | --- | --- | --- |
| 1 | recording_id |  |  | Идентификатор записи разговора |
| 2 | action |  |  | Разрешенные значения download, play |

Примеры: Запрос: GET https://app.mango-office.ru/vpbx/queries/recording/issa/0d3f60a984b45c0/play/ Ответ ВАТС API: 302 Found ... Location: https://lk.mango-office.ru/300002862/300003465/mail/play/id/360984450 ... Ответ ЛК: 302 Found ... Location: https://files.mango-office.ru/sdwee3en38fh328923943534ff3d2jh2d ...

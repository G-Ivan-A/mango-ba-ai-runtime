---
id: integration-bitrix24-110-dobavlenie-vo-vneshnyuyu-sistemu-url-adr
doc_code: INTB24
doc_title: "Интеграция Виртуальной АТС и Битрикс24. Инструкция по настройке"
doc_version: "03.03.2026"
section: "0"
pdf_section: "2.11"
title: "Добавление во внешнюю систему URL-адреса вебхука перемещения сделок. Общие требования."
pdf_heading: "Добавление во внешнюю систему URL-адреса вебхука перемещения сделок. Общие требования."
pages: "94-95"
source: kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf
source_part: "1"
source_pages: "ч.1: 94-95"
source_refs: '[{"source_pdf":"kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf","part":1,"pages":"94-95","global_pages":"94-95"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 775
status: extracted
ai-generated: true
---
# Добавление во внешнюю систему URL-адреса вебхука перемещения сделок. Общие требования.

> Трассировка: PDF §2.11 · сквозные стр. 94-95 · источники: ч.1 `kb/sources/integration-bitrix24/Mango_office_integration_Bitrix24.pdf` с.94-95.

сделок. Общие требования. 1) Полученный Вами URL-адрес вебхука перемещения сделок нужно добавить в вашу внешнюю систему. Для этого привлеките вашего специалиста, имеющего навыки администрирования Вашей системы; 2) Для обеспечения корректной обработки вебхука перемещения сделок внешняя система должна обеспечивать: - поддерживать передачу данных по протоколу HTTP; - обеспечивать подстановку в следующие параметры URL- адреса вебхуки перемещения сделок значений, соответствующих следующим требованиям:

| Параметр<br>URL -адреса<br>вебхуки | Требование |
| --- | --- |
| DealID | Внешняя система должна обеспечивать подстановку в<br>параметр “DealID” внутреннего ID-номера сделки, выданного<br>Битрикс24 (по этому номеру приложение интеграции<br>определит какую сделку нужно переместить). При записи |

Интеграция Виртуальной АТС MANGO OFFICE и Битрикс24 | Версия от 03.03.2026

| Параметр<br>URL -адреса<br>вебхуки | Требование |
| --- | --- |
|  | внутреннего номера телефона нужно использовать только<br>арабские цифры от 0 до 9. |
| Result | Внешняя система должна обеспечивать подстановку в<br>параметр “Result” одного из следующих значений: POSITIVE<br>NEGATIVE NEUTRAL Примечание. Подстановка других<br>значений в параметр “Result” запрещена. |

Примеры: 1) Не корректный URL-адрес вебхука: подстановка не корректного значение в параметр "Result": https://integration-webhook.mango- office.ru/webhookapp/?Source=Bitrix24&AuthData=qwerty&Product_id=qwerty.bi trix24.ru&Action=Deal_Move&DealID=12&Result=HELLO 2) Пример корректного URL-адреса вебхука: https://integration-webhook.mango- office.ru/webhookapp/?Source=Bitrix24&AuthData=qwerty2&Product_id=qwerty. bitrix24.ru&Action=Deal_Move&DealID=12&Result=POSITIVE

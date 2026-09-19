---
id: lk-vats-sso-08-vhod-sotrudnika-v-lichnyy-kabinet-vats
doc_code: LKSSO
doc_title: "Аутентификация и авторизация в рамках SSO"
doc_version: "1.0"
section: "5"
pdf_section: "5"
title: "Вход сотрудника в Личный кабинет ВАТС"
pdf_heading: "5. Вход сотрудника в Личный кабинет ВАТС"
pages: "12-13"
source: kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf
source_part: "1"
source_pages: "ч.1: 12-13"
source_refs: '[{"source_pdf":"kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf","part":1,"pages":"12-13","global_pages":"12-13"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 610
status: extracted
ai-generated: true
---
# 5. Вход сотрудника в Личный кабинет ВАТС

> Трассировка: PDF §5 · сквозные стр. 12-13 · источники: ч.1 `kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf` с.12-13.

После перехода сотрудника по ссылке, полученной на вкладке Данные Service- провайдера, откроется форма выбора Identity-провайдера:

![Изображение, стр. 12](../images/08-vhod-sotrudnika-v-lichnyy-kabinet-vats-1.jpeg)

![Изображение, стр. 12](../images/08-vhod-sotrudnika-v-lichnyy-kabinet-vats-2.png)

После выбора из списка нужного Identity-провайдера в новом окне будет открыта форма авторизации выбранного провайдера. После успешной авторизации на стороне IdP пользователь будет перенаправлен в Личный кабинет ВАТС MANGO OFFICE. внимание При обработке ответа (auth-response), полученного от IdP, важно наличие в ответе атрибута с именем «nameID», в котором должно быть передано значение e-mail сотрудника. Если этот атрибут отсутствует или значение не соответствует e-mail сотрудника, то авторизация будет невозможной, то есть сотрудник не сможет успешно войти в систему. совет

| Открытие всплывающих окон может быть заблокировано настройками |
| --- |
| браузера. Если после выбора IdP в списке не открывается всплывающее |
| окно, необходимо проверить настройки отображения всплывающих окон в |
| браузере. |

![Изображение, стр. 13](../images/08-vhod-sotrudnika-v-lichnyy-kabinet-vats-3.jpeg)

<!-- изображение на стр. 13: байты не извлечены (PyMuPDF недоступен) -->

<!-- изображение на стр. 13: байты не извлечены (PyMuPDF недоступен) -->

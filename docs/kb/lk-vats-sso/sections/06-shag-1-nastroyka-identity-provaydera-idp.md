---
id: lk-vats-sso-06-shag-1-nastroyka-identity-provaydera-idp
doc_code: LKSSO
doc_title: "Аутентификация и авторизация в рамках SSO"
doc_version: "1.0"
section: "0"
pdf_section: "4"
title: "Шаг 1. Настройка Identity-провайдера (IdP)."
pdf_heading: "Шаг 1. Настройка Identity-провайдера (IdP)."
pages: "6-8"
source: kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf
source_part: "1"
source_pages: "ч.1: 6-8"
source_refs: '[{"source_pdf":"kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf","part":1,"pages":"6-8","global_pages":"6-8"}]'
extracted_by: "pdfplumber 0.11.10"
token_method: "tiktoken:cl100k_base"
tokens: 1552
status: extracted
ai-generated: true
---
# Шаг 1. Настройка Identity-провайдера (IdP).

> Трассировка: PDF §4 · сквозные стр. 6-8 · источники: ч.1 `kb/sources/lk-vats-sso/MANGO_OFFICE_LK_VATS_Auth_SSO.pdf` с.6-8.

ШАГ 1. НАСТРОЙКА IDENTITY-ПРОВАЙДЕРА (IDP).

![Изображение, стр. 6](../images/06-shag-1-nastroyka-identity-provaydera-idp-1.jpeg)

![Изображение, стр. 6](../images/06-shag-1-nastroyka-identity-provaydera-idp-2.jpeg)

Вы можете выбрать два способа настройки вашего Identity-провайдера: загрузить файл метаданных (metadata.xml) или ввести необходимые данные вручную. Все поля формы являются обязательными для заполнения. Название провайдера - название вашего Identity-провайдера (например Keycloak). Это поле помогает идентифицировать ваш IdP в системе.

<!-- изображение на стр. 7: байты не извлечены (PyMuPDF недоступен) -->

<!-- изображение на стр. 7: байты не извлечены (PyMuPDF недоступен) -->

<!-- изображение на стр. 7: байты не извлечены (PyMuPDF недоступен) -->

Идентификатор (Entity ID) - или идентификатор сущности, уникально идентифицирует ваш Identity-провайдер в контексте SAML 2.0. Entity ID предоставляется вашим Identity- провайдером. Login URL - URL-адрес, по которому ваш сервис-поставщик будет перенаправлять пользователей для аутентификации. Пользователи будут направлены на этот URL для ввода учетных данных в систему IdP. Login URL также предоставляется вашим Identity- провайдером. Logout URL - URL-адрес, по которому пользователи будут перенаправляться после выхода из системы. Этот URL определяет, куда пользователи будут перенаправлены после завершения сеанса. Logout URL также предоставляется вашим Identity- провайдером. Сертификат в формате XML - сертификат в формате XML, который используется для безопасной передачи данных между вашим сервис-поставщиком и Identity- провайдером. Этот сертификат обеспечивает защиту данных во время обмена между системами. Обратитесь к вашему Identity-провайдеру, чтобы получить этот сертификат. Вы также можете найти его в метаданных (metadata.xml), если предоставленный файл содержит эту информацию. Загрузить файл metadata.xml - имеется возможность заполнить данную форму, используя файл с метаданными Identity-провайдера. Структура файла стандартная (соответствует спецификации SAML 2.0). Файл метаданных содержит информацию о вашем Identity-провайдере и его загрузка облегчит настройку, так как позволит автоматически получить необходимые параметры. Файл может быть предоставлен вам вашим IdP или находиться в их системе. Пример структуры файла metadata.xml

| <md:EntityDescriptor |
| --- |
| xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata» |
| validUntil="2023-09-30T19:48:36Z» |
| cacheDuration="PT604800S» entityID="https://adfs- |
| test.by.mgo.su/entityid"> |
| <div id="in-page-channel-node-id» data-channel- |
| name="in_page_channel_jblkcP"/> |
| <md:SPSSODescriptor AuthnRequestsSigned="false» |
| WantAssertionsSigned="false» |
| protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:p |
| rotocol"> |
| <md:KeyDescriptor use="signing"> |
| <ds:KeyInfo |
| xmlns:ds="http://www.w3.org/2000/09/xmldsig#"> |
| <ds:X509Data> |
| <ds:X509Certificate>MIIC4jCCAcoCCQC33wnybT5QZDANBgkqhkiG9 |
| w0BAQsFADAyMQswCQYDVQQGEwJVSzEPMA0GA1UECgwGQm94eUhRMRIwEA |
| YDVQQDDAlNb2NrIFNBTUwwIBcNMjIwMjI4MjE0NjM4WhgPMzAyMTA3MDE |
| yMTQ2MzhaMDIxCzAJBgNVBAYTAlVLMQ8wDQYDVQQKDAZCb3h5SFExEjAQ |
| BgNVBAMMCU1vY2sgU0FNTDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCA |
| QoCggEBALGfYettMsct1T6tVUwTudNJH5Pnb9GGnkXi9Zw/e6x45DD0Ru |
| RONbFlJ2T4RjAE/uG+AjXxXQ8o2SZfb9+GgmCHuTJFNgHoZ1nFVXCmb/H |
| g8Hpd4vOAGXndixaReOiq3EH5XvpMjMkJ3+8+9VYMzMZOjkgQtAqO36eA |
| FFfNKX7dTj3VpwLkvz6/KFCq8OAwY+AUi4eZm5J57D31GzjHwfjH9WTeX |

<!-- изображение на стр. 8: байты не извлечены (PyMuPDF недоступен) -->

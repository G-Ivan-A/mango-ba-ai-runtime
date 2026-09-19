# Настройка репозитория

## 1. Установите инструменты

- Git: [официальная загрузка](https://git-scm.com/downloads).
- GigaCode CLI: используйте инструкции вашей организации и сверяйте их с
  [официальным проектом в GitVerse](https://gitverse.ru/gigacode/).
- Python не нужен для основного валидатора.

Windows: нажмите `Win + X` → **Терминал**. Команды ниже запускайте в PowerShell;
`sh` доступен через Git Bash, который устанавливается вместе с Git for Windows.

## 2. Скачайте и откройте проект

```sh
git clone https://github.com/G-Ivan-A/mango-ba-ai-runtime.git
cd mango-ba-ai-runtime
git status
```

Ожидается строка `On branch main` и отсутствие изменённых файлов.

## 3. Проверьте структуру

```sh
ls -la
sh tools/validate-package.sh
```

Должны быть `taxonomy/`, `contracts/`, `routes/`, `.agents/skills/`,
`templates/`, `golden/`, `evaluation/`, `tools/`, `docs/kb/` и `runs/`.

## 4. Подключите GigaCode

1. Откройте корень репозитория как рабочий каталог.
2. Разрешите чтение `AGENTS.md`, `.hub-profile.json` и `.agents/skills/`.
3. В новом чате спросите: `Покажи имя маршрута и число доступных навыков,
   ничего не изменяя`.
4. Ожидаемый ответ: `RG-BCREQ-v1`, 11 навыков.

Если ваша версия GigaCode не загружает `SKILL.md` автоматически, приложите к
обращению `AGENTS.md` и нужный `.agents/skills/<name>/SKILL.md`; это временный
ручной режим, который следует записать в лист прогона.

[← Быстрый старт](00-quick-start.md) · [Далее: процессы →](02-processes.md)

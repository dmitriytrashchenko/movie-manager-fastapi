# Changelog

## 2026-07-19 — Возрождение проекта
Проект был взят из состояния "не начато" в штабе Core_operation_all_project. Все эндпоинты падали с 500 Internal Server Error сразу после клонирования репозитория.

**Найдено и исправлено:**
1. **Таблицы БД никогда не создавались** — нигде не вызывался `Base.metadata.create_all()`. Любой запрос падал с `sqlite3.OperationalError: no such table`. Добавлен вызов в `app.py` при старте.
2. **Movie и User жили в разных SQLAlchemy metadata** — `models/movie.py` импортировал общий `Base` из `models/base.py`, но следующей строкой переопределял его новым `declarative_base()`. Из-за этого `create_all()` создавал бы только одну из двух таблиц в зависимости от того, какой Base передать. Убрано переопределение, обе модели используют один `Base`.
3. **Битый Foreign Key** — `Movie.genre_id` ссылался на `ForeignKey("genres.id")`, а модели/таблицы `Genre` в проекте нет вообще. Это ломало `db.commit()` при первом же добавлении фильма (`NoReferencedTableError`). FK убран, поле осталось обычным `Integer` (используется только для фильтрации).
4. **bcrypt 4.x несовместим с passlib 1.7.4** — `AttributeError: module 'bcrypt' has no attribute '__about__'`, из-за чего хеширование пароля падало на регистрации. Зафиксирована версия `bcrypt==4.0.1` в `requirements.txt`.
5. **`requirements.txt` был неполным** — отсутствовали `passlib`, `python-jose`, `python-multipart`, `pydantic[email]`, хотя код их использует.
6. **`venv/` целиком был закоммичен в git** (~3300 файлов). Добавлен `.gitignore` (venv/, __pycache__/, *.db, *.log), venv убран из индекса `git rm -r --cached`.
7. **Битый локальный venv** — ссылался на несуществующий `C:\OS\Miniconda\python.exe`. Пересоздан заново.

**Проверено живым запуском** (uvicorn на порту 8123): register → token (JWT) → add movie → list movies → filter by watched → update movie → delete movie — весь путь отработал без ошибок.

**Закоммичено и запушено:** `820ba53` в `github.com/dmitriytrashchenko/movie-manager-fastapi`.

## 2026-07-19 — Чистка мёртвого кода
- Удалён `db/base.py` (+ `db/__init__.py`) — дублирующий, нигде не импортируемый модуль подключения к БД, оставшийся от незавершённой попытки перейти на Postgres.
- Удалён пустой пакет `movies_manager/` (`movies_manager/main.py`, `movies_manager/__init__.py`) — задел под рефакторинг, ни разу не использованный.
- Исправлен баг в `Dockerfile`: `CMD` запускал несуществующий модуль `app.main:app`, поправлено на `app:app` (реальную точку входа) — Docker-сборка раньше не смогла бы запуститься вообще.
- Проверено живым запуском после удаления: register + add movie отработали без ошибок.

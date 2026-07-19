# Known Issues / Backlog

## Postgres в docker-compose не подключён к приложению
`.env` (`DATABASE_URL=postgresql://postgres:postgres@db:5432/movies`), `requirements.txt` (`psycopg2-binary`) и `docker-compose.yml` поднимают Postgres-контейнер, но `app.py` жёстко хардкодит `sqlite:///movies.db` и не читает `DATABASE_URL` вообще. Если запустить `docker-compose up`, Postgres поднимется, но приложение всё равно будет писать в SQLite внутри контейнера (данные потеряются при пересборке, если не примонтирован volume под movies.db).
**Не критично** — SQLite полностью рабочий для pet-проекта. Если понадобится реальный Postgres — нужно переписать `app.py`, чтобы читал `DATABASE_URL` из окружения через `create_engine`.

## Секрет JWT захардкожен в коде
`utils/security.py`: `SECRET_KEY = "your_super_secret_key"`. Уже в публичном репозитории на GitHub. Для pet-проекта не критично, но если проект когда-то реально задеплоят — нужно вынести в `.env` и сгенерировать случайный ключ.

## SECRET_KEY не ротируется, нет refresh-токенов
Токен просто истекает через 30 минут (`ACCESS_TOKEN_EXPIRE_MINUTES`), логаута/инвалидации нет. Ок для учебного проекта.

## Нет тестов
Ни unit, ни integration тестов в проекте нет. Всё проверено вручную через curl 2026-07-19 (см. Changelog).

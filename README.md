# Movie Manager API (CRUD_app)

Учебный pet-проект: REST API для управления коллекцией фильмов, сделан для прокачки FastAPI/SQLAlchemy/JWT (см. `Чему я научился.txt`).

## Статус
Живой. Возрождён и протестирован 2026-07-19 (см. [[Changelog]]).

## Стек
- Python 3.11+, FastAPI, SQLAlchemy, Pydantic
- SQLite (реально используется как БД)
- JWT-аутентификация (python-jose) + bcrypt-хеширование паролей (passlib)
- Docker/docker-compose поднимает Postgres-контейнер, но `app.py` жёстко использует SQLite — Postgres в docker-compose сейчас не используется приложением. См. [[Known_Issues]].

## Установка и запуск
```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn app:app --reload
```
Swagger UI: http://127.0.0.1:8000/docs

## Эндпоинты
- `POST /register` — регистрация пользователя
- `POST /token` — логин, получение JWT
- `POST /movies/`, `GET /movies/` (с фильтрами genre_id/release_year/rating/watched), `GET /movies/{id}`, `PUT /movies/{id}`, `DELETE /movies/{id}`

## Структура
```
app.py              — все роуты (movies + auth)
models/              — SQLAlchemy-модели (Movie, User) + общий Base
schemas/              — Pydantic-схемы
utils/security.py    — хеширование паролей, JWT
```

## GitHub
- Репозиторий: https://github.com/dmitriytrashchenko/movie-manager-fastapi
- Синхронизирован: да

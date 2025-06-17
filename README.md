# Менеджер фильмов (Movie Manager API)

Это CRUD-приложение на Python с использованием FastAPI и SQLAlchemy для управления базой данных фильмов.

---

## О проекте

- Позволяет добавлять, получать, обновлять и удалять фильмы.
- Использует SQLite для хранения данных.
- Поддерживает аутентификацию через JWT токены.
- Реализован с использованием FastAPI, SQLAlchemy, Pydantic.
- Swagger UI доступен по адресу `/docs`.

---

## Установка и запуск

1. Клонируйте репозиторий
```bash
git clone <your_repo_url>
cd <your_project_folder>
```

2. Создайте виртуальное окружение и активируйте его
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

3. Установите зависимости
```bash
pip install -r requirements.txt
```

4. Запустите приложение
```bash
uvicorn app:app --reload
```

5. Откройте в браузере [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) для тестирования API

---

## Структура проекта

```
movies_manager/
|-- movies_manager/
|   |-- __init__.py
|   |-- main.py
|-- models/
|   |-- __init__.py
|   |-- base.py
|   |-- movie.py
|   |-- user.py
|-- db/
|   |-- __init__.py
|   |-- base.py
|-- app.py
|-- README.md
|-- requirements.txt
```

---

## Используемые технологии

- Python 3.9+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

---

## Аутентификация

- Используется OAuth2 с JWT токенами.
- Токен выдаётся по эндпоинту `/token`.
- Защищённые маршруты требуют передачи токена.

---

## Как использовать

- Создайте пользователя (если реализовано).
- Получите токен через `/token`.
- Используйте токен в заголовке Authorization: Bearer `<token>` для доступа к защищённым маршрутам.
- Управляйте фильмами через эндпоинты `/movies/`.

---

## Контакты

По вопросам и предложениям обращайтесь к автору проекта.
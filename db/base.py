from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from models.movie import Movie
import os

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    # fallback на локальный SQLite, если переменная окружения не задана
    DATABASE_URL = "sqlite:///" + os.path.join(os.path.dirname(__file__), "movies.db")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()

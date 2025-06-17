from .base import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    create_engine,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_year = Column(Integer)
    description = Column(String)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    rating = Column(Float)
    watched = Column(Boolean)

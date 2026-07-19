from .base import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_year = Column(Integer)
    description = Column(String)
    genre_id = Column(Integer)
    rating = Column(Float)
    watched = Column(Boolean)

# schemas/movie.py

from pydantic import BaseModel
from typing import Optional


class MovieBase(BaseModel):
    title: str
    release_year: int
    description: str
    genre_id: int
    rating: float
    watched: bool


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    release_year: Optional[int] = None
    description: Optional[str] = None
    genre_id: Optional[int] = None
    rating: Optional[float] = None
    watched: Optional[bool] = None


class MovieOut(MovieBase):
    id: int

    class Config:
        from_attributes = True


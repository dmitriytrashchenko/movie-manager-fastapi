import os
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models.movie import Movie
from models.user import User
from schemas.movie import MovieCreate, MovieUpdate, MovieOut # ⬅️ импорт схем
from schemas.user import UserCreate, UserOut
from utils.security import hash_password, verify_password, create_access_token, oauth2_scheme

DATABASE_URL = "sqlite:///" + os.path.join(os.path.dirname(__file__), "movies.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()


# Dependency для получения БД-сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to the Movie Manager API! Go to /docs for Swagger UI."}


# ============================ MOVIES ============================

@app.post("/movies/", response_model=MovieOut)
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


@app.get("/movies/", response_model=List[MovieOut])
def get_movies(
    genre_id: Optional[int] = None,
    release_year: Optional[int] = None,
    rating: Optional[float] = None,
    watched: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Movie)
    if genre_id:
        query = query.filter(Movie.genre_id == genre_id)
    if release_year:
        query = query.filter(Movie.release_year == release_year)
    if rating:
        query = query.filter(Movie.rating == rating)
    if watched is not None:
        query = query.filter(Movie.watched == watched)
    return query.all()


@app.get("/movies/{movie_id}", response_model=MovieOut)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.put("/movies/{movie_id}", response_model=MovieOut)
def update_movie(movie_id: int, movie_update: MovieUpdate, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = movie_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(movie, key, value)

    db.commit()
    db.refresh(movie)
    return movie


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return {"message": "Movie deleted successfully"}


# ============================ AUTH ============================

@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_pw = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

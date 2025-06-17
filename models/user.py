from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base  # если есть общий Base, или импортируй как у себя

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
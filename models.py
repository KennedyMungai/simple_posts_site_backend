"""Created the python file that holds the logic for the models
"""
import datetime

import passlib.hash as hash
import sqlalchemy.orm as orm
from sqlalchemy import Column, DateTime, Integer, String

from database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())


class PostModel(Base):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True, index=True)

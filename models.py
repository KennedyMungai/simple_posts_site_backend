"""Created the python file that holds the logic for the models
"""
import datetime

import passlib.hash as hash
import sqlalchemy.orm as orm
from sqlalchemy import Column, Table, Row, Integer, String, DateTime

from database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())

"""Created the python file that holds the logic for the models
"""
import datetime

import passlib.hash as _hash
import sqlalchemy.orm as _orm
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey

from database import Base


class UserModel(Base):
    """The template for the UserMOdel data structure

    Args:
        Base (Class): The class which is inherited by the UserModel
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    posts = _orm.relationship("Post", back_populates="user")

    def password_verification(self, password: str):
        return ''


class PostModel(Base):
    """The template for the PostModel data structure

    Args:
        Base (Class): The parent class of the class
    """
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_title = Column(String)
    post_body = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    user = _orm.relationship("User", back_populates="posts")

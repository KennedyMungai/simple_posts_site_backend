"""A file that holds all the schema data
"""
from pydantic import BaseModel
import datetime as _datetime


class UserBase(BaseModel):
    """The UserBase class

    Args:
        BaseModel (class): The parent class for the UserBase class
    """
    email: str
    name: str
    phone: str


class UserRequest(UserBase):
    """The template for the data requested by the server

    Args:
        UserBase (Class defined above): The base class for the data
    """
    password: str

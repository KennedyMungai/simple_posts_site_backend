"""A file that holds all the schema data
"""
import datetime

from pydantic import BaseModel


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

    class Config:
        """The config for the UserRequest class
        """
        orm_mode = True


class UserResponse(UserBase):
    """Created the template for the User response

    Args:
        UserBase (The base class for the data): This is the parent class for this class
    """
    id: int
    created_at: datetime.datetime

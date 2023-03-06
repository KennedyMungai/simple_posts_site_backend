"""This script contains the services code"""
from email_validator import EmailNotValidError, validate_email
from fastapi import HTTPException
from sqlalchemy import orm as _orm

import database as _database
import models as _models
from schemas import UserRequest


def create_db():
    """This method calls the database creation method"""
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    """Created a database session

    Yields:
        db: The database session
    """
    _db = _database.SessionLocal()

    try:
        yield _db
    finally:
        _db.close()


async def get_user_by_email(email: str, _db: _orm.Session):
    """A function that filters users by their emails

    Args:
        email (str): The email address being queried
        _db (orm.Session): The database session

    Returns:
        string: The email being queried
    """
    return _db.query(_models.UserModel).filter(_models.UserModel.email == email).first()


async def create_user(user: UserRequest, db: _orm.Session):
    """A function to create a user in the database

    Args:
        user (UserRequest): The template of the data needed to create the user
        db (_orm.Session): A single session in the database
    """
    # Check for valid email
    try:
        is_valid = validate_email(email=user.email)
        email = is_valid.email
    except EmailNotValidError:
        raise HTTPException(
            status_code=400,
            detail="Provide a valid email address"
        )

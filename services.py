"""This script contains the services code"""
from email_validator import EmailNotValidError, validate_email
from fastapi import HTTPException
from sqlalchemy import orm as _orm

import database as _database
from models import UserModel
from schemas import UserRequest
from passlib import hash


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
    return _db.query(UserModel).filter(UserModel.email == email).first()


async def create_user(user: UserRequest, _db: _orm.Session):
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
            status_code=400, detail="Provide a valid email address")

    # Convert a normal password to a hash
    hashed_password = hash.bcrypt.hash(user.password)

    user_object = UserModel(
        email=email,
        name=user.name,
        phone=user.phone,
        password_hash=hashed_password
    )

    # Save the user in the database
    _db.add(user_object)
    _db.commit()

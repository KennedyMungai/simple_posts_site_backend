"""This script contains the services code"""
import database as _database
import models as _models
from sqlalchemy import orm


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


async def get_user_by_email(email: str, _db: orm.Session):
    return _db.query(_models.UserModel).filter(_models.UserModel.email == email).first()

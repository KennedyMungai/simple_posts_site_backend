"""This script contains the services code
"""
import database as _database
import models as _models


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

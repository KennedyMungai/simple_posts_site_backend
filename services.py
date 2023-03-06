"""This script contains the services code
"""
import database as _database


def create_db():
    """This method calls the database creation method"""
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    """Created a database session

    Yields:
        db: The database session
    """
    db = _database.SessionLocal()

    try:
        yield db
    finally:
        db.close()

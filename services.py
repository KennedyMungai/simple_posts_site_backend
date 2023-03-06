"""This script contains the services code
"""
import database as _database


def create_db():
    """This method calls the database creation method"""
    return _database.Base.metadata.create_all(bind=_database.engine)


create_db()

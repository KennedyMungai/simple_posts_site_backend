"""Created the file that holds the logic for the database file
    """
from os import getenv

import sqlalchemy
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
from sqlalchemy import create_engine

from keys import MYSQL_KEY

DB_URL = MYSQL_KEY

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = orm.declarative_base()

"""Created the file that holds the logic for the database file
    """
import sqlalchemy
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
from os import getenv
from sqlalchemy import create_engine

from dotenv import load_dotenv

load_dotenv()

DB_URL = getenv('MYSQL_PATH')

engine = create_engine(DB_URL, {"check_same_thread": False})

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()

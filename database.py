"""Created the file that holds the logic for the database file
"""
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
from sqlalchemy import create_engine

DB_URL = "sqlite:///./dbfile.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = orm.declarative_base()

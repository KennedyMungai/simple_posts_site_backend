import sqlalchemy as sqlalchemy
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = 'mysql+pymysql://'

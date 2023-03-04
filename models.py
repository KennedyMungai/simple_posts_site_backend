"""Created the python file that holds the logic for the models
"""
import datetime

import passlib.hash as hash
import sqlalchemy
import sqlalchemy.orm as orm

import database


class UserModel(database.Base):
    # ll

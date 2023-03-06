"""This is the new entry point for the application"""
from fastapi import FastAPI, Security as _security, Depends
from sqlalchemy import orm as _orm
from services import get_db

from schemas import UserRequest

app = FastAPI()


@app.post('/api/v1/users')
async def register_user(user: UserRequest, db: _orm.Session = Depends(get_db())):
    """The API endpoint for user creation in the application"""
    pass

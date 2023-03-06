"""This is the new entry point for the application"""
from fastapi import Depends, FastAPI, HTTPException
from fastapi import Security as _security
from sqlalchemy import orm as _orm

from schemas import UserRequest
from services import get_db, get_user_by_email

app = FastAPI()


@app.post('/api/v1/users')
async def register_user(user: UserRequest, _db: _orm.Session = Depends(get_db())):
    """The API endpoint for user creation in the application"""
    db_user = await get_user_by_email(user.email, _db)

    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists, try with another email address"
        )

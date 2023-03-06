"""This is the new entry point for the application"""
from fastapi import FastAPI, Security as _security, Depends, HTTPException
from sqlalchemy import orm as _orm
from services import get_db, get_user_by_email

from schemas import UserRequest

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

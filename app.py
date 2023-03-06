"""This is the new entry point for the application"""
from fastapi import FastAPI, Security as _security
from sqlalchemy import orm as _orm

app = FastAPI()

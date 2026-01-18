from db import BaseClass
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime


class User(BaseClass):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String)
    Age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow())

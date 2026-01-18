from db import base
from sqlalchemy import Column, String, Integer


class userdetails(base):
    __tablename__ = 'user_det'

    id = Column(Integer, primary_key=True,)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

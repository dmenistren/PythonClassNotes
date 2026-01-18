from const import DB_URL
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

Engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(autoflush=False, autocommit=False, bind=Engine)
BaseClass = declarative_base()

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

db_url = "postgresql://postgres:toor@localhost:5432/pythonclass"

engine = create_engine(db_url, echo=True)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
base = declarative_base()

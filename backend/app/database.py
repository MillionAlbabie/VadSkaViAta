# backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

# Skapa engine
engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class för modeller
Base = declarative_base()

# Dependency för att få databas session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

## Database Connection
DATABASE_URL=os.getenv("DATABASE_URL")

## Create a database engine
engine=create_engine(DATABASE_URL)

## Create a session Maker
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

##Base class for SQLAlchemy models
Base=declarative_base()

## Dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
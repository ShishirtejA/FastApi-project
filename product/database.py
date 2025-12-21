from sqlalchemy import create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker # for sessions.
# This file is for the database configuration.

SQLALCHEMY_DATABASE_URL = 'sqlite:///./product.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={
    "check_same_thread" : False
})


SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()


def get_db(): # this will allow us to get the access to the database when ever we want.
    db = SessionLocal() # This will give us access to the session instance.
    try:
        yield db
    finally:
        db.close()

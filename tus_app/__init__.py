from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

app = FastAPI()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://pavlo:1111@localhost/tus_db'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
engine.connect()
db_session = scoped_session(sessionmaker(bind=engine))


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()

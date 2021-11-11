from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import uvicorn

app = FastAPI()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://pavlo:1111@localhost/tus_db'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
engine.connect()
db_session = scoped_session(sessionmaker(bind=engine))


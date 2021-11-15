from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["http://localhost:3000",
    "http://localhost:8000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

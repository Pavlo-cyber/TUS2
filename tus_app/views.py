from fastapi import FastAPI
from tus_app import app, db_session
from tus_app.models import User
from fastapi.security import HTTPBasic

session = db_session()

auth = HTTPBasic()


@app.get('/')
def index():
    return {'data': {'text': 'main_page'}}


@app.get('/tutor')
def tutors():
    return {'data': {'text': 'tutor_data'}}


@app.get('/tutor/{id}')
def tutor(id: int):
    return {'data': id}

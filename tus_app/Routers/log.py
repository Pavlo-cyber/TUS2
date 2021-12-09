from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from tus_app import models, get_db
from tus_app import schema
from tus_app import token

router = APIRouter(
    prefix='/log',
    tags=['log']
)


@router.get('/')
def get_log():
    f = open("log.txt", "r")
    text = f.read()
    return text




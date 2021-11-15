from fastapi import Depends, status,APIRouter
from sqlalchemy.orm import Session
from tus_app import models
from tus_app import schema, get_db
from tus_app.hashing import Hash
from typing import Any, Callable
from fastapi import APIRouter as FastAPIRouter
from fastapi.types import DecoratedCallable



router = APIRouter(
    prefix='/register',
    tags=['register']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def add_user(user: schema.User, db: Session = Depends(get_db)):
    hashed_password = Hash.encrypt(user.password)
    temp = db.query(models.User).filter(models.User.username == user.username).first()
    if not temp:
        new_user = models.User(first_name=user.first_name, last_name=user.last_name,
                               email=user.email, username=user.username, password_hash=hashed_password,
                               role=user.role)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    else:
        return "User with that username is already exist"


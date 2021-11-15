from fastapi import Depends, status, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from tus_app import models
from tus_app import schema, get_db
from tus_app.hashing import Hash
from tus_app.token import *

router = APIRouter(

    tags=['Authentication']
)


@router.post('/login', response_model=schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    if not Hash.verify(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect password")

    access_token = create_access_token( data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}





from fastapi import APIRouter
from fastapi import Depends, status, HTTPException

from sqlalchemy.orm import Session
from tus_app import models, get_db
from tus_app import schema
from tus_app import token

router = APIRouter(
    prefix='/cv',
    tags=['cv']
)


@router.get('/{id}')
def get_cv(id, db: Session = Depends(get_db)):
    cv = db.query(models.CV).filter(models.CV.id == id).first()
    if not cv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tutor with id {id} not available")
    return cv


@router.post('/', status_code=status.HTTP_201_CREATED, tags=['cv'])
def add_cv(cv: schema.CV, db: Session = Depends(get_db), current_user: schema.User = Depends(token.get_current_user)):
    user= db.query(models.User).filter(models.User.username == current_user.username).first()
    new_cv = models.CV(text=cv.text, rating=cv.rating, user_id=user.id)
    db.add(new_cv)
    db.commit()
    db.refresh(new_cv)
    return new_cv


@router.get('/')
def get_all_cv(db: Session = Depends(get_db)):
    all_cv = db.query(models.CV).all()
    return all_cv


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_cv(id, db: Session = Depends(get_db)):
    cv = db.query(models.CV).filter(models.CV.id == id)
    if not cv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tutor with id {id} not available")
    cv.delete(synchronize_session=False)
    db.commit()
    return "done"


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_cv(id, request: schema.CV, db: Session = Depends(get_db)):
    cv = db.query(models.CV).filter(models.CV == id)
    if not cv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tutor with id {id} not available")
    cv.update(request)
    db.commit()
    return cv

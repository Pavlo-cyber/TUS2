from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from typing import List
from datetime import datetime
from pydantic import parse_obj_as
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


@router.post('/')
def add_cv(cv: schema.CV, db: Session = Depends(get_db), current_user: schema.User = Depends(token.get_current_user)):
    user = db.query(models.User).filter(models.User.username == current_user.username).first()
    f = open("log.txt", "a")
    date = datetime.now()
    f.write(f'{date} User with username  {user.username} add new CV\n')
    f.close()
    new_cv = models.CV(text=cv.text, rating=cv.rating, user_id=user.id)
    db.add(new_cv)
    db.commit()
    db.refresh(new_cv)
    obj = db.query(models.CV).order_by(models.CV.id.desc()).first()
    new_subject = models.Subject(name=cv.subject, cv_id=obj.id, cv_user_id=user.id)
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject


@router.get('/')
def get_all_cv(db: Session = Depends(get_db)):
    all_cv = db.query(models.CV).all()
    just_data = []
    for cv in all_cv:
        subjects = []
        new_subject = db.query(models.Subject).filter(models.Subject.cv_id == cv.id).first()
        user = db.query(models.User).filter(models.User.id == cv.user_id).first()
        just_data.append(
            { "id": cv.id, "subject": new_subject.name, "first_name": user.first_name, "last_name": user.last_name, "text": cv.text,
             "rating": cv.rating, "photo": user.photo, "email": user.email, "phone": user.phone})
    m = parse_obj_as(List[schema.CVResponse], just_data)
    return just_data


@router.delete('/{id}')
def delete_cv(id, db: Session = Depends(get_db),current_user: schema.User = Depends(token.get_current_user)):
    cv = db.query(models.CV).filter(models.CV.id == id).first()
    if not cv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tutor with id {id} not available")
    if cv.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=f"CV with {id} not allowed")
    f = open("log.txt", "a")
    date = datetime.now()
    f.write(f'{date} User with username {current_user.username} delete CV\n')
    f.close()
    db.query(models.Subject).filter(models.Subject.cv_id == id).delete(synchronize_session=False)
    db.commit()
    db.query(models.CV).filter(models.CV.id == id).delete(synchronize_session=False)
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

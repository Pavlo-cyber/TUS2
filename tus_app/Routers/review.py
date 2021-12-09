from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
import json
from typing import List
from datetime import datetime

from pydantic import parse_obj_as
from sqlalchemy.orm import Session
from tus_app import models, get_db
from tus_app import schema
from tus_app import token

router = APIRouter(
    prefix='/review',
    tags=['review']
)


@router.post('/')
def add_review(review: schema.Review, db: Session = Depends(get_db),
               current_user: schema.User = Depends(token.get_current_user)):
    new_review = models.Review(text=review.text, user_id=current_user.id)
    db.add(new_review)
    db.commit()
    f = open("log.txt", "a")
    date = datetime.now()
    f.write(f'{date} User with username {current_user.username} add new review\n')
    f.close()
    return new_review


@router.get('/')
def get_all(db: Session = Depends(get_db)):
    all_review = db.query(models.Review).all()
    just_data = []
    for review in all_review:
        user = db.query(models.User).filter(models.User.id == review.user_id).first()
        just_data.append(
            {"id": review.id, "first_name": user.first_name, "last_name": user.last_name,
             "text": review.text})
    return just_data


@router.delete('/{id}')
def delete_review(id, db: Session = Depends(get_db), current_user: schema.User = Depends(token.get_current_user)):
    review = db.query(models.Review).filter(models.Review.id == id)
    if not review.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review with id {id} not available")
    review.delete(synchronize_session=False)
    db.commit()
    f = open("log.txt", "a")
    date = datetime.now()
    f.write(f'{date} User with username {current_user.username} delete review\n')
    f.close()
    return "done"

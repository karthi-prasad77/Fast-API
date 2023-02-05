from blog import models
from blog import schemas
from blog import hashing
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def create_user(request : schemas.Users, db : Session):
    new_user = models.Users(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db : Session, id : int):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id {id} not found")
    return user
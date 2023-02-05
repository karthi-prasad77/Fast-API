from fastapi import APIRouter, Depends, HTTPException, status
from blog import schemas
from blog import database
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    tags = ['Users'],
    prefix = "/user"
)

get_db = database.get_db

@router.post('/', response_model = schemas.ShowUser)
def create_user(request : schemas.Users, db : Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model = schemas.ShowUser)
def get_user(id : int, db : Session = Depends(get_db)):
    return user.get_user(db, id)
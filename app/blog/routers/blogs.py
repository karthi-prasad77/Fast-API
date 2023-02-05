from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, models, database
from blog.repository import blogs
from typing import List
from sqlalchemy.orm import Session
from blog.Oauth2 import get_current_user

router = APIRouter(
    tags = ['Blogs'],
    prefix = "/blog"
)

get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowBlog])
def all_blog(db : Session = Depends(get_db), current_user : schemas.Users = Depends(get_current_user)):
    return blogs.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db), current_user : schemas.Users = Depends(get_current_user)):
    return blogs.create(request, db)

@router.get('/{id}', status_code = 200, response_model = schemas.ShowBlog)
def show(id : int,  db : Session = Depends(get_db), current_user : schemas.Users = Depends(get_current_user)):
    return blogs.get_one(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id , request : schemas.Blog, db : Session = Depends(get_db), current_user : schemas.Users = Depends(get_current_user)):
    return blogs.update(id, db, request)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id : int, db : Session = Depends(get_db), current_user : schemas.Users = Depends(get_current_user)):
    return blogs.destroy(id, db)
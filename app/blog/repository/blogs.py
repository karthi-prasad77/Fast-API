from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog import schemas, models

def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request : schemas.Blog, db : Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_one(id : int , db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Particular blog with the {id} was not available")
    return blog

def update(id : int, db : Session, request : schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id) # pass the request it into dictionary type
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.update(request.dict()) 
    db.commit()
    return {"Blog updated successfully"}

def destroy(id : int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session = False)
    db.commit()  
    return {f'Blog with {id} destroyed successfully'}
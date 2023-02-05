from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit, published : bool, sort : Optional[str] = None):
    if published:
        return {'data' : f'{limit} blog list'}
    else:
        return {'data' : f'1000 blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blogs'}


@app.get('/show/{id}')
def show(id : int):
    return {'data' : id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data' : {'1', '2'}}

class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]


@app.post('/blog')
def create_blog(request : Blog):
    return {'data' : f'Blog is created with title as {request.title}'}


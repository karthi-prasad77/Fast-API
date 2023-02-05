from fastapi import FastAPI
from blog import models, database
from blog.routers import blogs, user, authenticate


app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(blogs.router)
app.include_router(user.router)
app.include_router(authenticate.router)
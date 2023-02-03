from fastapi import FastAPI
from router import BlogGet,BlogPost,user,articles

from db import models
from db.database import engine 

app = FastAPI()
app.include_router(user.router)
app.include_router(articles.router)
app.include_router(BlogGet.router)
app.include_router(BlogPost.router)


@app.get('/')
def index():
    return {"message":"Hello world"}

# Ceate Database
models.Base.metadata.create_all(engine)
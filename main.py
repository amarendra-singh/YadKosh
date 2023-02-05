from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import HTTPException

from router import BlogGet,BlogPost,user,articles
from db import models
from db.database import engine 
from exceptions import StoryException


app = FastAPI()
app.include_router(user.router)
app.include_router(articles.router)
app.include_router(BlogGet.router)
app.include_router(BlogPost.router)


@app.get('/')
def index():
    return {"message":"Hello world"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )

# @app.exception_handler(HTTPException)
# def custom_handlerr(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)

# Ceate Database
models.Base.metadata.create_all(engine)
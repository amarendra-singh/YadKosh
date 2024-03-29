from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from router import BlogGet,BlogPost,user,articles,product, file
from auth import authentication
from db import models
from db.database import engine 
from exceptions import StoryException


app = FastAPI()
app.include_router(file.router)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(articles.router)
app.include_router(BlogGet.router)
app.include_router(BlogPost.router)
app.include_router(product.router)


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

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.mount('/files', StaticFiles(directory= "files"), name="files")
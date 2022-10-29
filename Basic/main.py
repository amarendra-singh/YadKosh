import imp
from typing import Optional
from fastapi import FastAPI
from router import blog

app = FastAPI()
app.include_router(blog.router)

@app.get('/')
def index():
    return {"message":"Hello world"}

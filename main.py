from fastapi import FastAPI, APIRouter
from db import models
from db.database import engine

app =FastAPI()

@app.get("/")
def root():
    return "Hello"


models.Base.metadata.create_all(engine)
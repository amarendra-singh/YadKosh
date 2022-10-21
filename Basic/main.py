from typing import Optional
from fastapi import FastAPI
from enum import Enum
app = FastAPI()


@app.get("/")
def index():
    return "hhello"

class BlogType(str,Enum):
    Food = "Foodie"
    Travel = 'Travling'

# def cal1(int,num):
#     # num = num
#     if num < 0:
#         return 0
#     return num % 10 + cal1(num//10)

@app.get("/pages/all", tags=['Blog'], summary='Retrive all blogs', description="This api call simulates fetching all blogs")
def blogall(page = 1,pagesize : Optional[int] = None):
    return {"message":f"your page is {page} and  pagesize is {pagesize}"}

@app.get("/blog/type/{type}")
def bloging(type : BlogType):
    return {"message": f"Your blog type is {type}"}

@app.get("/blog/{id}")
def blog(id:int):
    return {"message":f"your blog id is {id}"}


# @app.get("/cal/{num}")
# def cal(num: cal1):
#     return {"message":f" result{num}"}
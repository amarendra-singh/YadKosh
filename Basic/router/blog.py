from fastapi import APIRouter, status
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix= '/blog',
    tags = ['blog']
)



@router.get("/{id}", status_code = status.HTTP_200_OK, tags = ['Blog'])
def blog(id):
    return {"message":f"Your blog id is {id}"}

class blogType(str, Enum):
    Food = "Foodie"
    Travel = "Traveler"

@router.get("/pages/all", tags=['Blog'], summary='Retrive all blogs', description="This api call simulates fetching all blogs")
def blogs(type:blogType, city = "India", cost: Optional[int] = None ):
    return f"You are {type}, your in {city}, and it will cost you {cost}"
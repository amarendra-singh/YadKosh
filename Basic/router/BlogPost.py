from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Optional,List

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class BlogModel(BaseModel):
    name : str
    content : str
    pushlised : Optional[bool]

@router.post("/create/{id}")
def create(blog : BlogModel, id :int, version : int = 1):
    return {
        'id':id,
        'data' : blog,
        'version' : version
    }

@router.post("/create/{id}/comment/{comment_id}")
def createComment(blog: BlogModel, id: int,
            comment_title: int = Query(None,
                title = "Id of comment", description = " detail of comment",
                alias = 'commentId',
                deprecated = True
        ),
        content : str = Body(..., 
            min_length = 10,
            max_length = 50,
            regex = '^[a-z\s]*$'
        ),
        v: Optional[List[str]] = Query(['2','3','6']),
        comment_id: int = Path(None, gt=5, le=10)
    ):
    
    return {
        "Blog":blog,
        "Id":id,
        "comment":comment_title,
        "content":content,
        "v" : v,
        comment_id: comment_id
    }
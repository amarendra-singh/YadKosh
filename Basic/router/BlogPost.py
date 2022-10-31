from fastapi import FastAPI, APIRouter
router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

router.post("/create")
def create():
    pass
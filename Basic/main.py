
from fastapi import FastAPI
from router import BlogGet,BlogPost

app = FastAPI()
app.include_router(BlogGet.router)
app.include_router(BlogPost.router)

@app.get('/')
def index():
    return {"message":"Hello world"}



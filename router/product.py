from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

product = ['watch', 'camera','phone']

@router.get('/all')
def get_all_product():
    data = " ".join(product)
    return Response(content=data, media_type="text/plain")

@router.get('/{id}', responses={
    200: {
        "content":{
            "text/html":{
                "example":"<div>Product</div>"
            }
        },
        "description":"Returns the HTML for an object"
    },
    404:{
        "content":{
            "text/plain":{
                "example": "Product not available"
            }
        },
        "descriptiion":"A error message"
    }
})

def get_product(id:int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(status_code=404)
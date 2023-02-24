from typing import Optional, List
from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera','phone']


@router.post("/create_product")
def create_product(name: str = Form(...)):
    products.append(name)
    return products



@router.get('/all')
def get_all_product():
    data = " ".join(products)

    return Response(content=data, media_type="text/plain")

@router.get('/withheader')
def get_product(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None)
    ):

    if custom_header:
        response.headers['custom_response_header'] = "and ".join[custom_header]
    return {
        'data': products,
        'custom_header': custom_header,
        'my_cookie': test_cookie
    }


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
    product = products[id]
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(status_code=404)
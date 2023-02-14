from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends

from schemas import ArticleBase, ArticeDisplay, UserBase
from db import db_articles
from db.database import get_db
from auth.oauth2 import oauth2_schema, get_current_user

router = APIRouter(
    prefix = '/article',
    tags=['article']
)

@router.post('/', response_model = ArticeDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_articles.create_article(db, request)

@router.get('/{id}' )#, response_model = ArticeDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data': db_articles.get_article(db, id),
        'current_user': current_user,
        }
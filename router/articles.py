from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends

from schemas import ArticleBase, ArticeDisplay
from db import db_articles
from db.database import get_db


router = APIRouter(
    prefix = '/article',
    tags=['article']
)

@router.post('/', response_model = ArticeDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_articles.create_article(db, request)

@router.get('/{id}', response_model = ArticeDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_articles.get_article(db, id)
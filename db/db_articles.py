from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from fastapi import HTTPException, status
from db.models import DbArticles
from exceptions import StoryException


def create_article(db: Session, request: ArticleBase):
    if request.content.startswith('Once upon atime'):
        raise StoryException('No Stories please')

    new_article = DbArticles(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id= request.creator_id
    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db: Session, request: ArticleBase):
    article = db.query(DbArticles).filter(DbArticles.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {id} not found')
    return article

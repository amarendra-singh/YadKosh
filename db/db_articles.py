from sqlalchemy.orm.session import Session
from db.models import DbArticles
from schemas import ArticleBase

def create_article(db: Session, request: ArticleBase):
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
    return article

from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from db.models import DbUser

def createUser(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=request.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return new_user
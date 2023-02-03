from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql.sqltypes import ForeignKey
from db.database import Base
from sqlalchemy import Column

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, index = True )
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbArticles', back_populates = 'user')

class DbArticles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    content = Column(String)
    published = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("DbUser", back_populates = 'items')
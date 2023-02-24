from .database import Base
from sqlalchemy import Column, Integer, String

class DBUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index= True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    
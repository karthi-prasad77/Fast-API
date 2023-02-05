from blog.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('use.id'))
    creator = relationship("Users", back_populates = "blogs")

class Users(Base):
    __tablename__ = 'use'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blog', back_populates = "creator")

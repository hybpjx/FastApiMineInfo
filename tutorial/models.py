#models.py
from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True)
    hashed_password=Column(String)
    is_active=Column(Boolean,default=True)

    items=relationship('Item',back_populates='owner')



class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # 表a_user.items等于相应的Item表
    owner = relationship("User", back_populates="items")

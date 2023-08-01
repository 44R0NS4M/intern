from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date
from database import Base
from sqlalchemy import Date

class Posts(Base):
    __tablename__ ="Posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    content = Column(String, nullable=True)
    published = Column(Boolean, default=False)
    created = Column(Date)

class Users(Base):
    __tablename__ ="Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    created = Column(Date)


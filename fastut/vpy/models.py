from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Characters(Base):
    __tablename__ ="characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    house = Column(String)

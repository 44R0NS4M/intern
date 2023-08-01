from pydantic import BaseModel
from datetime import date
# from typing import List

class PostUp(BaseModel):
    # id:int
    title:str
    content:str
    
    
  
class LsPost(BaseModel):
    # data:List[CharacterUp]
    title:str
    created:date
    
    class Config:
        orm_mode=True

class  PubPost(BaseModel):
    # id:int
    title:str
    content:str
    created:date

class UserUp(BaseModel):
    
    email:str
    password:str
    
class PubUsr(BaseModel):
    
    email:str
    created:date
    class config():
        orm_mode = True
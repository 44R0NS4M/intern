from pydantic import BaseModel
# from typing import List

class  CharacterUp(BaseModel):
    # id:int
    name:str
    house:str
    
class PubChar(BaseModel):
    # data:List[CharacterUp]
    name:str
    house:str
    class Config:
        orm_mode=True
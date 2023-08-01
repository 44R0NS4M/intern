from fastapi import Depends, FastAPI, HTTPException,Body
from schemas import CharacterUp,PubChar
from database import get_db,engine
from sqlalchemy.orm import Session
import models
from typing import List

# conn=psycopg2.connect(database="apitut",host="localhost",user="postgres",password="admin",port="5432")
# cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)


app=FastAPI()
models.Base.metadata.create_all(bind=engine)


# cursor.execute("select * from characters")
# characters=cursor.fetchall()

@app.get("/",response_model=List[PubChar])
def get_user(db: Session = Depends(get_db)):
    characters=db.query(models.Characters).all()
    return characters

@app.get("/{id}",response_model=PubChar)
def get_user(id:int,db: Session = Depends(get_db)):
    characters=db.query(models.Characters).filter(models.Characters.id==id).first()
    # for i in characters:
    #     if i.id == id:
    #         return i
    return characters

@app.post("/add")   
def add_character(payload:CharacterUp, db: Session = Depends(get_db)):
    
    charins=models.Characters(name = payload.name, house=payload.house)
    db.add(charins)
    db.commit()
    db.refresh(charins)
    return charins

    # cursor.execute(f"insert into characters values({payload.id},'{payload.name}','{payload.house}')")
    # conn.commit()
    # cursor.execute("select * from characters")
    # characters=cursor.fetchall()

    
#     return characters

@app.put("/update/{id}")
def update_user(id:int,payload: CharacterUp, db: Session = Depends(get_db)):
    characters=db.query(models.Characters).filter(models.Characters.id == id)
    characters.update({**payload.dict()})
    db.commit()
    db.refresh(characters)
    return characters

    # return payload

#     # cursor.execute(f"update characters set name = '{payload.name}', house = '{payload.house}' where id = {payload.id}")
#     # conn.commit()
#     # cursor.execute("select * from characters");
#     # characters = cursor.fetchall()
        
#     return characters
        
            
                      
        
        
        

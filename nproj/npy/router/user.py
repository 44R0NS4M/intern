from fastapi import Depends, FastAPI, HTTPException,Body,APIRouter
from schemas import PostUp,PubPost,LsPost,UserUp,PubUsr
from database import get_db,engine
from sqlalchemy.orm import Session
import models
from typing import List
from sqlalchemy import Date
from datetime import date

router=APIRouter(
    prefix="/user"
)

@router.get("/users/",response_model=List[PubUsr])
def get_usr(db: Session = Depends(get_db)):
    LsUsr=db.query(models.Users).all()
    return LsUsr

@router.get("/{id}",response_model=PubUsr)
def get_usr(id:int,db: Session = Depends(get_db)):
    DisUser=db.query(models.Users).filter(models.Users.id==id).first()
    return DisUser

@router.post("/add")   
def add_usr(usrPL:UserUp, db: Session = Depends(get_db)):
    
    creat=models.Users(email = usrPL.email, password = usrPL.password, created = date.today())
    db.add(creat)
    db.commit()
    db.refresh(creat)
    return creat


@router.put("/edit/{id}")
def update_usr(id:int,usrPL: UserUp, db: Session = Depends(get_db)):
    upd=db.query(models.Users).filter(models.Users.id == id)
    # upd.update({**usrPL.dict()})
    for attr, value in usrPL.dict().items():
        setattr(upd, attr, value)
    db.commit()
    db.refresh(upd)
    return upd
        
@router.delete("/remove/{id}")
def del_usr(id:int, db: Session = Depends(get_db)):
    db.query(models.Users).filter(models.Users.id == id).delete()
    db.commit()
    LsUsr=db.query(models.Users).all()
    return LsUsr
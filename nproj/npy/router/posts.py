from fastapi import Depends, FastAPI, HTTPException,Body,APIRouter
from schemas import PostUp,PubPost,LsPost,UserUp,PubUsr
from database import get_db,engine
from sqlalchemy.orm import Session
import models
from typing import List
from sqlalchemy import Date
from datetime import date

router=APIRouter(
    prefix="/posts"
)

@router.get("/blog/",response_model=List[LsPost])
def get_post(db: Session = Depends(get_db)):
    LPosts=db.query(models.Posts).all()
    return LPosts

@router.get("/{id}",response_model=PubPost)
def get_post(id:int,db: Session = Depends(get_db)):
    DisPost=db.query(models.Posts).filter(models.Posts.id==id).first()
    return DisPost

@router.post("/")   
def add_post(payload:PostUp, db: Session = Depends(get_db)):
    
    Post=models.Posts(title = payload.title, content = payload.content, created = date.today())
    db.add(Post)
    db.commit()
    db.refresh(Post)
    return Post


@router.put("/update/{id}")
def update_post(id:int,payload: PostUp, db: Session = Depends(get_db)):
    post=db.query(models.Posts).filter(models.Posts.id == id).first()
    post.update({**payload.dict()})
    db.commit()
    db.refresh(post)
    return post
        
@router.delete("/delete/{id}")
def del_post(id:int, db: Session = Depends(get_db)):
    post=db.query(models.Posts).filter(models.Posts.id == id)
    post.delete()
    LPosts=db.query(models.Posts).all()
    return LPosts


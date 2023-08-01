from fastapi import Depends, FastAPI, HTTPException,Body
# from fastapi.middleware.cors import CORSMiddleware
from router import user, posts
# from schemas import PostUp,PubPost,LsPost,UserUp,PubUsr
from database import get_db,engine
from sqlalchemy.orm import Session
import models
from typing import List
from sqlalchemy import Date
from datetime import date


app=FastAPI()
models.Base.metadata.create_all(bind=engine)



# origins = [
#     "http://localhost",
#     "http://127.0.0.1:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(user.router)
app.include_router(posts.router)




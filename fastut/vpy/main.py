# from fastapi import FastAPI,Body
# from pydantic import BaseModel
# import psycopg2.extras


# conn=psycopg2.connect(database="alchemytut",host="localhost",user="postgres",password="admin",port="5432")
# cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)




# class  CharacterUp(BaseModel):
#     id:int
#     name:str
#     house:str

# app=FastAPI()

# # characters=[]
# # dicts={
# #         "id": 1,
# #         "name": "Harry Potter",
# #         "house": "Gryffindor"
# #     }

# # dict2={
# #         "id": 2,
# #         "name": "Hermione Granger",
# #         "house": "Gryffindor"
# #     }
# # characters.append(dicts)
# # characters.append(dict2)

# cursor.execute("select * from characters")
# characters=cursor.fetchall()


# @app.get("/")
# def get_user():
#     return {"data": characters}

# @app.get("/{id}")
# def get_user(id:int):
#     for i in characters:
#         if i["id"] == id:
#             return i

# @app.post("/add")   
# def add_character(payload:CharacterUp):
#     cursor.execute(f"insert into characters values({payload.id},'{payload.name}','{payload.house}')")
#     conn.commit()
#     cursor.execute("select * from characters")
#     characters=cursor.fetchall()

#     # characters.append(payload.dict())
#     return characters

# @app.put("/update/{id}")
# def update_user(id:int,payload: CharacterUp):        
#     # for i in characters:
#     #     if i["id"] == id:
#     cursor.execute(f"update characters set name = '{payload.name}', house = '{payload.house}' where id = {payload.id}")
#     conn.commit()
#     cursor.execute("select * from characters");
#     characters = cursor.fetchall()
#         # i["name"]=payload.name
#     return characters
        
            
                      
        
        
        

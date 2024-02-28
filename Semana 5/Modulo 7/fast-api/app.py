from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role


app = FastAPI()

db: List[User] = [
    User(
        id=UUID("57051eb9-ff81-44c0-9177-f2aefc030ba0"),
        first_name="Beth",
        last_name="Pereira",
        email="email@gmail.com",
        role=[Role.role_1]
        ),
    User(
        id=UUID("fde48456-0008-4cd8-ad64-7c34f3673ef1"),
        first_name="Jeff",
        last_name="Almeida",
        email="email@gmail.com",
        role=[Role.role_2]
        ),
    User(
        id=UUID("34c7a2f0-7497-4b54-b260-4e8eeb08ad0a"),
        first_name="Vanessa",
        last_name="Pereira",
        email="email@gmail.com",
        role=[Role.role_3]
        ) 
]

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}
        

#Metodo post criar um novo registro (é estático, não é físico)
@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    "id": "UUID",
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "role": Role
    """
    db.append(user)
    return{"id": user.id}


#Delete 
@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db: #pesquise esse user específico dentro do DB
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )
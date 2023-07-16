from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel

# CRUD
# C - Create
# R - Read
# U - Update
# D - Delete

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

users = []

@app.get("/test")
def read_root():
    a = 5
    b = 7
    c = a + b


    return {"message": users}

@app.post("/users")
def create_user(user: UserCreate):
    users.append({"name": user.name, "email": user.email})
    return {"message": f"Usuário criado: {user.name}, {user.email}"}

@app.put("/users")
def update_user(user: UserCreate):
    name = user.name
    email = user.email
    for i in users:
        if i['name'] == name:
            i['email'] = email

    return {"message": "email atualizado"}
    
    
@app.delete("/users/{name}")
def delete_user(name: str):
    print(name)

    for user in users:
        if user['name']==name:
            users.remove(user)

    return {"message": f"Usuário com ID {name} excluído com sucesso"}



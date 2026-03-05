
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# @app.get("/geeksforgeeks.org")
# def say_hello():
#     return "say test"

# @app.get("/geeksforgeeks.org/python")
# def say_hello():
#     return "say geek"

# @app.get("/geeksforgeeks.org/python/fastapi-tutorial/")
# def say_hello():
#     return "say hello"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = [
    {"id": 1, "name": "Alice", "age": 25,"native":"Chennai"},
    {"id": 2, "name": "Bob", "age": 30,"native":"Salem"},
    {"id": 3, "name": "Charlie", "age": 28,"native":"Madurai"}
]



class User(BaseModel):
    name: str
    age: int
    native: str
    
@app.post("/create_users")
def create_user(user: User):

    new_user = user.dict()

    new_user["id"] = len(users) + 1

    users.append(new_user)

    return {"message": "User added successfully", "user": new_user}

@app.get("/users")
def get_users():
    return {"users": users}
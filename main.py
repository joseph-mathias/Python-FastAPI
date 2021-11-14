from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User, UserUpdateResquest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("7552a5ac-61f7-491e-b95f-3bc65a64ff1b"),
        first_name="Joseph",
        last_name="Nchimunya",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
    User(
        id=UUID("22ccc1bb-88a4-4f6e-889f-536e6d5c889e"),
        first_name="Stephen",
        last_name="Nchimunya",
        gender=Gender.male,
        roles=[Role.user]
    )
]

@app.get("/")
def root():
    return {"Hello": "Joseph"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateResquest, user_id: UUID):
    for user in db:
        if user_id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return

    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} does not exist"
    )
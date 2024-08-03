from fastapi import APIRouter
from pydantic import BaseModel
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User
from config.database import Session
from services.user import UserService

user_router = APIRouter()

@user_router.post('/create-user', tags=['Auth'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un usuario"})

@user_router.post('/login', tags=['Auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
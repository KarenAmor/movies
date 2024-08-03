from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.comment import CommentService
from schemas.comment import Comment

comment_router = APIRouter()

@comment_router.get('/comments/{id_movie}', tags=['Comments'], response_model=Comment)
def get_comment(id_movie: int = Path(ge=1, le=200)) -> Comment:
    db = Session()
    result = CommentService(db).get_comment(id_movie)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@comment_router.post('/comments', tags=['Comments'], response_model=dict, status_code=201)
def create_comment(comment: Comment) -> dict:
    db = Session()
    CommentService(db).create_comment(comment)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el comentario"})
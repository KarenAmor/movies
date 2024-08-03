from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: Optional[int] = None
    email:str
    password:str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "micuenta@correo.com",
                "password": "+123AaK@",
            }
        }
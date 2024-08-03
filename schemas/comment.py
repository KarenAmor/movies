from pydantic import BaseModel, Field
from typing import Optional

class Comment(BaseModel):
    id: Optional[int] = None
    id_movie: int = Field(..., le=200)
    comment: str = Field(min_length=15, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "id_movie": 2,
                "comment": "Descripción de la película",
            }
        }
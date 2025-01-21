from uuid import UUID

from pydantic import BaseModel


class Matrix(BaseModel):
    uuid: UUID
    name: str
    height: int
    width: int

    class Config:
        from_attributes = True

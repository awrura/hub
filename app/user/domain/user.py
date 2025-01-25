from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    uuid: UUID
    username: str

    class Config:
        from_attributes = True

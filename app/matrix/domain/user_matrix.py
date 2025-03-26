from uuid import UUID

from pydantic import BaseModel


class UserMatrix(BaseModel):
    matrix_uuid: UUID
    user_uuid: UUID

    class Config:
        from_attributes = True

from uuid import UUID

from pydantic import BaseModel


class RegisterUserDTO(BaseModel):
    uuid: UUID
    username: str
    password: bytes

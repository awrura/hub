from pydantic import BaseModel


class ToLoginUserDTO(BaseModel):
    username: str
    password: str


class AuthTokens(BaseModel):
    access: str
    refresh: str

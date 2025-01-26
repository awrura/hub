from pydantic import BaseModel


class ToRegisterUserDTO(BaseModel):
    username: str
    password: str
    pass_confirm: str


class StoreRegisterUserDTO(BaseModel):
    username: str
    password: bytes

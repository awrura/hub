from pydantic import BaseModel


class ToLoginUserDTO(BaseModel):
    username: str
    password: str

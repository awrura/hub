from pydantic import BaseModel
from pydantic import Field


class RegisterUserInputSchema(BaseModel):
    username: str
    password: str
    pass_confirm: str = Field(description='Re-entry. Must match the main password')

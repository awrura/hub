from pydantic import BaseModel
from pydantic import Field


class RegisterUserInputSchema(BaseModel):
    username: str
    password: str
    pass_confirm: str = Field(description='Re-entry. Must match the main password')

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'twoics',
                'password': 'welocme',
                'pass_confirm': 'welocme',
            }
        }

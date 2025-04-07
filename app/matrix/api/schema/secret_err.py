from pydantic import BaseModel


class AddMatrixBySecretError(BaseModel):
    error: str

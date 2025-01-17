from pydantic import BaseModel


class DatabaseConnectConfig(BaseModel):
    HOST: str
    PORT: int
    USER: str
    PASS: str

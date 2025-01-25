from pydantic_settings import BaseSettings


class DatabaseConnectConfig(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASS: str

    class Config:
        env_file = '../.env'

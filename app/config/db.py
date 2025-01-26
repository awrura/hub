from pydantic_settings import BaseSettings


class DatabaseConnectConfig(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASS: str
    DB_NAME: str

    class Config:
        env_file = '../.env'

from pydantic_settings import BaseSettings


class AuthTokenSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = '../.env'


class AdminAuthSettings(BaseSettings):
    ADMIN_AUTH_SECRET: str
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    TOKEN_SECRET: str

    class Config:
        env_file = '../.env'

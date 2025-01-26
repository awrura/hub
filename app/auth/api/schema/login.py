from pydantic import BaseModel


class UserLoginCred(BaseModel):
    username: str
    password: str

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'twoics',
                'password': 'welocme',
            }
        }


class RefreshToken(BaseModel):
    refresh_token: str

    class Config:
        json_schema_extra = {
            'example': {
                'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxMjAwNzYsInN1YiI6InR3b2ljcyIsImFjY2Vzc190b2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpsZUhBaU9qRTNNemN4TWpBd056WXNJbk4xWWlJNkluUjNiMmxqY3lKOS5sQUU1aUNOTTRYYy1HNW1MNHFVVllZLURjdC1ZZ29QYjhydEpYTy1wMG9NIn0.WTACB1GSW0-o5o9CdlLPSlY0tDjtjEzF1uxthPaAodo',
            }
        }


class UserTokens(BaseModel):
    access: str
    refresh: str

    class Config:
        json_schema_extra = {
            'example': {
                'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxMjAwNzYsInN1YiI6InR3b2ljcyJ9.lAE5iCNM4Xc-G5mL4qUVYY-Dct-YgoPb8rtJXO-p0oM',
                'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcxMjAwNzYsInN1YiI6InR3b2ljcyIsImFjY2Vzc190b2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpsZUhBaU9qRTNNemN4TWpBd056WXNJbk4xWWlJNkluUjNiMmxqY3lKOS5sQUU1aUNOTTRYYy1HNW1MNHFVVllZLURjdC1ZZ29QYjhydEpYTy1wMG9NIn0.WTACB1GSW0-o5o9CdlLPSlY0tDjtjEzF1uxthPaAodo',
            }
        }

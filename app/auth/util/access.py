from auth.dto.auth import AuthUser
from auth.exception.auth import InvalidTokenError
from auth.service.token import JwtTokenAuth
from config.auth import AuthTokenSettings
from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

auth_scheme = HTTPBearer()


@inject
def authuser_from_token(
    token_cfg: FromDishka[AuthTokenSettings],
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> AuthUser:
    """
    Получить пользователя по его access token.
    В случае проеблемы декодирововки токена выкинуть исключение

    :raises: InvalidTokenError
    """

    token = credentials.credentials
    token_auth = JwtTokenAuth(conf=token_cfg)
    claims = token_auth.decode(token)

    if not claims:
        raise InvalidTokenError()
    return AuthUser(username=claims['username'])

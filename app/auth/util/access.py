from auth.exception.auth import InvalidTokenError
from auth.service.token import JwtTokenAuth
from config.auth import AuthTokenSettings
from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from user.domain.user import User
from user.store.proto.user import IUserRepository

auth_scheme = HTTPBearer()


@inject
async def user_from_token(
    token_cfg: FromDishka[AuthTokenSettings],
    user_repo: FromDishka[IUserRepository],
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> User:
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

    user = await user_repo.get_by_name(claims['sub'])
    if not user:
        raise InvalidTokenError()

    return user

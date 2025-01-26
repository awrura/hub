from typing import Protocol
from typing import TypedDict

from auth.action.usecase.login import UserLoginUseCase
from auth.dto.login import AuthTokens
from auth.dto.login import ToLoginUserDTO
from auth.exception.login import UnableRefreshTokens
from auth.exception.login import UserNotFoundError
from auth.exception.login import WrongUserPasswordError
from auth.service.crypt import is_valid_pswrd
from auth.store.proto.auth import ILoginUserRepository


class Tokens(TypedDict):
    access_token: str
    refresh_token: str


class ITokenAuth(Protocol):
    def renew(self, refresh_token: str) -> Tokens | None:
        """Проверка возможности обновления JWT токена"""

        raise NotImplementedError()

    def generate(self, username: str) -> Tokens:
        """Генерация JWT токена по username пользователя"""

        raise NotImplementedError()


class UserLoginInteractor(UserLoginUseCase):
    def __init__(self, login_repo: ILoginUserRepository, token_service: ITokenAuth):
        self._login_repo = login_repo
        self._token_service = token_service

    async def login(self, user_info: ToLoginUserDTO) -> AuthTokens:
        username = user_info.username
        if not await self._login_repo.user_exsist(username=username):
            raise UserNotFoundError(username=username)

        db_pswrd = await self._login_repo.get_user_pswrd(username=username)
        if not is_valid_pswrd(user_info.password, db_pswrd):
            raise WrongUserPasswordError()

        tokens = self._token_service.generate(username=username)
        return AuthTokens(
            access=tokens['access_token'], refresh=tokens['refresh_token']
        )


class UserRefreshInteractor(UserLoginUseCase):
    def __init__(self, token_service: ITokenAuth):
        self._token_service = token_service

    def refresh(self, refresh_token: str) -> AuthTokens:
        new_tokens = self._token_service.renew(refresh_token)
        if new_tokens is None:
            raise UnableRefreshTokens()

        return AuthTokens(
            access=new_tokens['access_token'], refresh=new_tokens['refresh_token']
        )

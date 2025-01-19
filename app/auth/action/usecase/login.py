from typing import Protocol

from auth.dto.login import AuthTokens
from auth.dto.login import ToLoginUserDTO


class UserLoginUseCase(Protocol):
    async def login(self, user_info: ToLoginUserDTO) -> AuthTokens:
        """Вход пользователя в систему. Получение токена доступа"""

        raise NotImplementedError()


class UserRefreshUseCase(Protocol):
    def refresh(self, refresh_token: str) -> AuthTokens:
        """Обновить токены пользователя по переданному refresh token"""

        raise NotImplementedError()

from typing import Protocol

from dto.register import RegisterUserDTO


class AuthUserRepository(Protocol):
    async def create_user(self, user: RegisterUserDTO) -> None:
        """Создание пользователя в хранилище"""

        raise NotImplementedError()

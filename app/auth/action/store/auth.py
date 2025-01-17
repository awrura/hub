from typing import Protocol

from auth.dto.register import RegisterUserDTO


class IAuthUserRepository(Protocol):
    async def create_user(self, user: RegisterUserDTO) -> None:
        """Создание пользователя в хранилище"""

        raise NotImplementedError()

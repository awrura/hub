from typing import Protocol

from auth.dto.register import StoreRegisterUserDTO


class IAuthUserRepository(Protocol):
    async def create_user(self, user: StoreRegisterUserDTO) -> None:
        """Создание пользователя в хранилище"""

        raise NotImplementedError()

    async def user_exsist(self, username: str) -> bool:
        """Проврка существования пользователя с такиим username"""

        raise NotImplementedError()

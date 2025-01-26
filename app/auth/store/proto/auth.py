from typing import Protocol

from auth.dto.register import StoreRegisterUserDTO


class UserExsistInRepository(Protocol):
    async def user_exsist(self, username: str) -> bool:
        """Проврка существования пользователя с такиим username"""

        raise NotImplementedError()


class IAuthUserRepository(UserExsistInRepository, Protocol):
    async def create_user(self, user: StoreRegisterUserDTO) -> None:
        """Создание пользователя в хранилище"""

        raise NotImplementedError()


class ILoginUserRepository(UserExsistInRepository, Protocol):
    async def get_user_pswrd(self, username: str) -> bytes:
        """Получишь хешированный пароль пользователя"""

        raise NotImplementedError()

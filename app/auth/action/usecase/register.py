from typing import Protocol

from dto.register import RegisterUserDTO


class RegistrationUseCase(Protocol):
    async def exec(self, user: RegisterUserDTO) -> None:
        """Регистрация (создание) пользователя в системе"""

        raise NotImplementedError()

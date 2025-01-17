from typing import Protocol

from auth.dto.register import ToRegisterUserDTO


class RegistrationUseCase(Protocol):
    async def exec(self, user: ToRegisterUserDTO) -> None:
        """Регистрация (создание) пользователя в системе"""

        raise NotImplementedError()

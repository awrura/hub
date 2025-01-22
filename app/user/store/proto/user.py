from typing import Protocol

from user.domain.user import User


class IUserRepository(Protocol):
    async def get_by_name(self, username) -> User | None:
        """Получить пользователя по его имени"""

        raise NotImplementedError()

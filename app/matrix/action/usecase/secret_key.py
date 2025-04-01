from typing import Protocol

from user.domain.user import User


class UserMatrixSecretkeyUseCase(Protocol):
    async def add_matrix_to_user(self, user: User, secret: str):
        """
        Найти матрицу по секретному ключу и добавить ее пользователю

        В случае успеха возвращается True, в случае неудачи False

        :raises:
            ValueError: Ошибка привязки матрицы к пользователю
        """

        raise NotImplementedError()

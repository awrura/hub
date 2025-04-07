from typing import List
from typing import Protocol

from matrix.domain.matrix import Matrix
from matrix.domain.user_matrix import UserMatrix
from user.domain.user import User


class IUserMatrixRepository(Protocol):
    async def get_user_matrices(self, user: User) -> List[Matrix]:
        """Получить доступные пользователю матрицы"""

        raise NotImplementedError()

    async def add_user_to_matrix(self, user: User, matrix: Matrix) -> UserMatrix | None:
        """Добавить пользователю матрицу"""

        raise NotImplementedError()

    async def user_matrix_exist(self, user: User, matrix: Matrix) -> bool:
        """Проверить существует ли данная матрица у пользователя"""

        raise NotImplementedError()

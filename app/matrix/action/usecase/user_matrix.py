from typing import List
from typing import Protocol

from matrix.domain.matrix import Matrix
from user.domain.user import User


class UserMatrixUseCase(Protocol):
    async def get_user_matrices(self, user: User) -> List[Matrix]:
        """Получить матрицы, доступные пользователю"""

        raise NotImplementedError()

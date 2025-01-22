from typing import List

from matrix.action.store.user_matrix import IUserMatrixRepository
from matrix.action.usecase.user_matrix import UserMatrixUseCase
from matrix.domain.matrix import Matrix
from user.domain.user import User


class UserMatrixInteractor(UserMatrixUseCase):
    def __init__(self, user_matrix_repo: IUserMatrixRepository):
        self._user_matrix_repo = user_matrix_repo

    async def get_user_matrices(self, user: User) -> List[Matrix]:
        return await self._user_matrix_repo.get_user_matrices(user)

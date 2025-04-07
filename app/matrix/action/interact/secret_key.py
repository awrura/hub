import logging

from matrix.action.usecase.secret_key import UserMatrixSecretkeyUseCase
from matrix.store.proto.matrix import IMatrixRepository
from matrix.store.proto.user_matrix import IUserMatrixRepository
from user.domain.user import User

logger = logging.getLogger(__name__)


class MatrixSecretKeyInteractor(UserMatrixSecretkeyUseCase):
    def __init__(
        self, matrix_repo: IMatrixRepository, user_matrix_repo: IUserMatrixRepository
    ):
        self._matrix_repo = matrix_repo
        self._user_matrix_repo = user_matrix_repo

    async def add_matrix_to_user(self, user: User, secret: str):
        matrix = await self._matrix_repo.get_matrix_by_secret(secret)

        if matrix is None:
            raise ValueError('Matrix with this secret does not exsist')

        user_matrix_exsist = await self._user_matrix_repo.user_matrix_exist(
            user, matrix
        )
        if user_matrix_exsist:
            raise ValueError('User already have this matrix')

        user_matrix = await self._user_matrix_repo.add_user_to_matrix(user, matrix)

        if not user_matrix:
            raise ValueError('Can not link user with current matrix')

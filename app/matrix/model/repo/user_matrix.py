from typing import List

from matrix.action.store.user_matrix import IUserMatrixRepository
from matrix.domain.matrix import Matrix as MatrixDomain
from matrix.model.entity.matrix import Matrix
from matrix.model.entity.user_matrix import UserMatrix
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select
from user.domain.user import User


class UserMatrixRepository(IUserMatrixRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user_matrices(self, user: User) -> List[MatrixDomain]:
        query = (
            select(Matrix)
            .distinct()
            .join(UserMatrix, Matrix.uuid == UserMatrix.matrix_uuid)
            .where(UserMatrix.user_uuid == user.uuid)
        )

        matrices = await self._session.scalars(query)
        return [MatrixDomain.model_validate(matrix) for matrix in matrices.all()]

from typing import List

from matrix.domain.matrix import Matrix as MatrixDomain
from matrix.domain.user_matrix import UserMatrix as DomainUserMatrix
from matrix.store.entity.matrix import Matrix
from matrix.store.entity.user_matrix import UserMatrix
from matrix.store.proto.user_matrix import IUserMatrixRepository
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
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

    async def add_user_to_matrix(
        self, user: User, matrix: MatrixDomain
    ) -> DomainUserMatrix | None:
        new_record = UserMatrix(user_uuid=user.uuid, matrix_uuid=matrix.uuid)

        self._session.add(new_record)

        try:
            await self._session.commit()
            await self._session.refresh(new_record)
        except IntegrityError:
            await self._session.rollback()
            return None

        return DomainUserMatrix.model_validate(new_record)

    async def user_matrix_exist(self, user: User, matrix: MatrixDomain) -> bool:
        return bool(await self._get_user_matrix(user, matrix))

    async def _get_user_matrix(
        self, user: User, matrix: MatrixDomain
    ) -> DomainUserMatrix | None:
        query = select(UserMatrix).where(
            and_(
                UserMatrix.user_uuid == user.uuid, UserMatrix.matrix_uuid == matrix.uuid
            )
        )

        user_matrix = await self._session.scalar(query)
        if not user_matrix:
            return None
        return DomainUserMatrix.model_validate(user_matrix)

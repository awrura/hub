from uuid import UUID

from matrix.domain.matrix import Matrix as DomainMatrix
from matrix.store.entity.matrix import Matrix
from matrix.store.proto.matrix import IMatrixRepository
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select


class MatrixRepository(IMatrixRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_matrix_by_secret(self, secret_key: str) -> DomainMatrix | None:
        try:
            secret_uuid = UUID(secret_key)
        except ValueError:
            return None

        query = select(Matrix).where(Matrix.secret_key == secret_uuid)
        matrix = await self._session.scalar(query)
        if not matrix:
            return None

        return DomainMatrix.model_validate(matrix)

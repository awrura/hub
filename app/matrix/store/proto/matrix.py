from typing import Protocol

from matrix.domain.matrix import Matrix


class IMatrixRepository(Protocol):
    async def get_matrix_by_secret(self, secret_key: str) -> Matrix | None:
        """Получить матрицу по ее секретному ключу"""

        raise NotImplementedError()

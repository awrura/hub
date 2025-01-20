from typing import TYPE_CHECKING
from uuid import UUID
from uuid import uuid4

from matrix.model.entity.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped

if TYPE_CHECKING:
    pass


class Matrix(Base):
    __tablename__ = 'matrix'

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True)
    height: Mapped[int]
    width: Mapped[int]

    # users: Mapped[List['User']] = relationship(
    #     secondary='user_matrix', back_populates='matrices'
    # )

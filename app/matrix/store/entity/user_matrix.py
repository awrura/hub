from uuid import UUID
from uuid import uuid4

from matrix.store.entity.base import Base
from matrix.store.entity.matrix import Matrix
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from user.store.entity.user import User


class UserMatrix(Base):
    __tablename__ = 'user_matrix'

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_uuid: Mapped[UUID] = mapped_column(
        ForeignKey(User.uuid), nullable=False, primary_key=True
    )
    matrix_uuid: Mapped[UUID] = mapped_column(
        ForeignKey(Matrix.uuid), nullable=False, primary_key=True
    )

from uuid import UUID
from uuid import uuid4

from matrix.store.entity.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped


class Matrix(Base):
    __tablename__ = 'matrix'

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True)
    height: Mapped[int]
    width: Mapped[int]
    secret_key: Mapped[UUID] = mapped_column(default=uuid4)

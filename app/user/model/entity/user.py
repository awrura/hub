from typing import TYPE_CHECKING
from uuid import UUID
from uuid import uuid4

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from user.model.entity.base import Base

if TYPE_CHECKING:
    pass


class User(Base):
    __tablename__ = 'user'

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]

    # matrices: Mapped[List['Matrix']] = relationship(
    #     secondary='user_matrix', back_populates='users'
    # )

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select
from user.action.store.user import IUserRepository
from user.domain.user import User
from user.model.entity.user import User as DBUser


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_name(self, username) -> User | None:
        query = select(DBUser).where(DBUser.username == username)
        db_user = await self._session.scalar(query)
        if not db_user:
            return None
        return User(uuid=db_user.uuid, username=db_user.username)

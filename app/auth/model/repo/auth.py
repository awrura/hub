from auth.action.store.auth import IAuthUserRepository
from auth.dto.register import StoreRegisterUserDTO
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select
from user.model.entity.user import User


class AuthUserRepository(IAuthUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_user(self, user: StoreRegisterUserDTO) -> None:
        db_user = User(username=user.username, password=user.password)
        self._session.add(db_user)
        await self._session.commit()

    async def user_exsist(self, username: str) -> bool:
        query = select(User).where(User.username == username)
        user = await self._session.scalar(query)
        return bool(user)

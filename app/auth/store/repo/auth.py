from auth.dto.register import StoreRegisterUserDTO
from auth.store.proto.auth import IAuthUserRepository
from auth.store.proto.auth import ILoginUserRepository
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select
from user.store.entity.user import User


class AuthUserRepository(IAuthUserRepository, ILoginUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_user(self, user: StoreRegisterUserDTO) -> None:
        db_user = User(username=user.username, password=user.password)
        self._session.add(db_user)
        await self._session.commit()

    async def user_exsist(self, username: str) -> bool:
        user = await self._get_user_by(username)
        return bool(user)

    async def get_user_pswrd(self, username: str) -> bytes:
        user = await self._get_user_by(username)
        if user is None:
            raise ValueError(f'User {username} does not exsist')
        return user.password

    async def _get_user_by(self, username: str) -> User | None:
        query = select(User).where(User.username == username)
        return await self._session.scalar(query)

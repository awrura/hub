from auth.action.store.auth import IAuthUserRepository
from auth.dto.register import RegisterUserDTO
from sqlalchemy.ext.asyncio.session import AsyncSession
from user.model.entity.user import User


class AuthUserRepository(IAuthUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_user(self, user: RegisterUserDTO) -> None:
        user = User(**user.model_dump())
        self._session.add(user)
        await self._session.commit()

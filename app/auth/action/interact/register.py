from auth.action.store.auth import IAuthUserRepository
from auth.action.usecase.register import RegistrationUseCase
from auth.dto.register import RegisterUserDTO


class UserRegistrationInteractor(RegistrationUseCase):
    def __init__(self, repo: IAuthUserRepository):
        self._repo = repo

    async def exec(self, user: RegisterUserDTO) -> None:
        await self._repo.create_user(user)

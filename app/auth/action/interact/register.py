from action.usecase.register import RegistrationUseCase
from auth.model.repo.auth.base import AuthUserRepository
from dto.register import RegisterUserDTO


class UserRegistrationInteractor(RegistrationUseCase):
    def __init__(self, repo: AuthUserRepository):
        self._repo = repo

    async def exec(self, user: RegisterUserDTO) -> None:
        await self._repo.create_user(user)

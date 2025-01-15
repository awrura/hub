from action.usecase.register import RegistrationUseCase
from dto.register import RegisterUserDTO
from repo.auth import AuthUserRepository


class UserRegistrationInteractor(RegistrationUseCase):
    def __init__(self, repo: AuthUserRepository):
        self._repo = repo

    async def exec(self, user: RegisterUserDTO) -> None:
        await self._repo.create_user(user)

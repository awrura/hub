from auth.action.usecase.register import RegistrationUseCase
from auth.dto.register import StoreRegisterUserDTO
from auth.dto.register import ToRegisterUserDTO
from auth.exception.register import InvalidPasswordConfirmError
from auth.exception.register import UserAlreadyRegisteredError
from auth.service.crypt import hash_password
from auth.store.proto.auth import IAuthUserRepository


class UserRegistrationInteractor(RegistrationUseCase):
    def __init__(self, repo: IAuthUserRepository):
        self._repo = repo

    async def exec(self, user: ToRegisterUserDTO) -> None:
        if await self._repo.user_exsist(user.username):
            raise UserAlreadyRegisteredError(username=user.username)

        if user.password != user.pass_confirm:
            raise InvalidPasswordConfirmError()

        passwrd = hash_password(user.password)
        await self._repo.create_user(
            StoreRegisterUserDTO(username=user.username, password=passwrd)
        )

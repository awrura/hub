from auth.exception.base import BaseAuthUserError


class UserAlreadyRegisteredError(BaseAuthUserError):
    def __init__(self, *, username: str):
        self.message = f'User with username {username} already registered'
        super().__init__()


class InvalidPasswordConfirmError(BaseAuthUserError):
    message: str = 'Incompatible passwords and confirmations'

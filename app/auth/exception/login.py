from auth.exception.base import BaseAuthUserError


class WrongUserPasswordError(BaseAuthUserError):
    message: str = 'Wrong password for this user'


class UserNotFoundError(BaseAuthUserError):
    def __init__(self, *, username: str):
        self.message = f'User with {username} username not found'


class UnableRefreshTokens(BaseAuthUserError):
    message: str = 'Unable renew tokens'

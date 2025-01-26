from auth.exception.base import BaseAuthUserError


class InvalidTokenError(BaseAuthUserError):
    message: str = 'Invalid access token'

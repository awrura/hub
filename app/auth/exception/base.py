class BaseAuthUserError(Exception):
    message: str = 'Auth module internal ERROR'

    def __str__(self):
        return self.message

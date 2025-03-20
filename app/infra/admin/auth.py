from config.auth import AdminAuthSettings
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


class AdminAuth(AuthenticationBackend):
    def __init__(self, cfg: AdminAuthSettings) -> None:
        super().__init__(cfg.ADMIN_AUTH_SECRET)
        self._cfg = cfg

    async def login(self, request: Request) -> bool:
        form = await request.form()
        request_cred = form['username'], form['password']

        if (self._cfg.ADMIN_USERNAME, self._cfg.ADMIN_PASSWORD) != request_cred:
            return False

        request.session.update({'token': self._cfg.TOKEN_SECRET})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get('token')

        if not token or token != self._cfg.TOKEN_SECRET:
            return False

        return True

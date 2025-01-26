from auth.action.interact.login import ITokenAuth
from auth.service.token import JwtTokenAuth
from dishka import provide
from dishka import Provider
from dishka import Scope


class TokenServiceProvider(Provider):
    token_service = provide(
        JwtTokenAuth,
        provides=ITokenAuth,
        scope=Scope.APP,
    )

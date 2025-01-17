from auth.action.store.auth import IAuthUserRepository
from auth.action.store.auth import ILoginUserRepository
from auth.model.repo.auth import AuthUserRepository
from dishka import provide
from dishka import Provider
from dishka import Scope


class AuthRepoProvider(Provider):
    auth_repository = provide(
        AuthUserRepository,
        provides=IAuthUserRepository,
        scope=Scope.REQUEST,
    )


class LoginUserRepositoryProvider(Provider):
    login_repositroy = provide(
        AuthUserRepository, provides=ILoginUserRepository, scope=Scope.REQUEST
    )

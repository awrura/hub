from auth.action.interact.login import UserLoginInteractor
from auth.action.interact.login import UserRefreshInteractor
from auth.action.interact.register import UserRegistrationInteractor
from auth.action.usecase.login import UserLoginUseCase
from auth.action.usecase.login import UserRefreshUseCase
from auth.action.usecase.register import RegistrationUseCase
from dishka import provide
from dishka import Provider
from dishka import Scope


class RegistrationUseCaseProvider(Provider):
    registration_use_case = provide(
        UserRegistrationInteractor,
        provides=RegistrationUseCase,
        scope=Scope.REQUEST,
    )


class LoginUseCaseProvider(Provider):
    login_use_case = provide(
        UserLoginInteractor, provides=UserLoginUseCase, scope=Scope.REQUEST
    )


class RefreshUseCaseProvider(Provider):
    refresh_use_case = provide(
        UserRefreshInteractor, provides=UserRefreshUseCase, scope=Scope.REQUEST
    )

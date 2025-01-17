from auth.action.interact.register import UserRegistrationInteractor
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

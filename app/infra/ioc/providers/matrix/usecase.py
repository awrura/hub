from dishka import provide
from dishka import Provider
from dishka import Scope
from matrix.action.interact.user_matrix import UserMatrixInteractor
from matrix.action.usecase.user_matrix import UserMatrixUseCase


class UserMatrixUseCaseProvider(Provider):
    get_user_matrices_case = provide(
        UserMatrixInteractor,
        provides=UserMatrixUseCase,
        scope=Scope.REQUEST,
    )

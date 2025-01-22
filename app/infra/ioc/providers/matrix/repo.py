from dishka import provide
from dishka import Provider
from dishka import Scope
from matrix.store.proto.user_matrix import IUserMatrixRepository
from matrix.store.repo.user_matrix import UserMatrixRepository


class UserMatrixRepoProvider(Provider):
    user_matrix_repository = provide(
        UserMatrixRepository,
        provides=IUserMatrixRepository,
        scope=Scope.REQUEST,
    )

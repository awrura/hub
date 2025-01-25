from dishka import provide
from dishka import Provider
from dishka import Scope
from user.store.proto.user import IUserRepository
from user.store.repo.user import UserRepository


class UserRepoProvider(Provider):
    user_repository = provide(
        UserRepository,
        provides=IUserRepository,
        scope=Scope.REQUEST,
    )

from dishka import provide
from dishka import Provider
from dishka import Scope
from user.action.store.user import IUserRepository
from user.model.repo.user import UserRepository


class UserRepoProvider(Provider):
    user_repository = provide(
        UserRepository,
        provides=IUserRepository,
        scope=Scope.REQUEST,
    )

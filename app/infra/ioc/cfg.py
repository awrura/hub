from config.auth import AdminAuthSettings
from config.auth import AuthTokenSettings
from config.db import DatabaseConnectConfig
from dishka.dependency_source import from_context
from dishka.entities.scope import Scope
from dishka.provider import Provider


class DBConfigProvider(Provider):
    config = from_context(provides=DatabaseConnectConfig, scope=Scope.APP)


class AuthConfigProvider(Provider):
    config = from_context(provides=AuthTokenSettings, scope=Scope.APP)


class AdminAuthConfigProvider(Provider):
    config = from_context(provides=AdminAuthSettings, scope=Scope.APP)

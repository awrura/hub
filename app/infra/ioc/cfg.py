from config.db import DatabaseConnectConfig
from dishka.dependency_source import from_context
from dishka.entities.scope import Scope
from dishka.provider import Provider


class ApplicationConfigProvider(Provider):
    config = from_context(provides=DatabaseConnectConfig, scope=Scope.APP)

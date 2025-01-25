from config.auth import AuthTokenSettings
from config.db import DatabaseConnectConfig
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI
from infra.ioc.cfg import AuthConfigProvider
from infra.ioc.cfg import DBConfigProvider
from infra.ioc.providers.auth.repo import AuthRepoProvider
from infra.ioc.providers.auth.repo import LoginUserRepositoryProvider
from infra.ioc.providers.auth.service import TokenServiceProvider
from infra.ioc.providers.auth.usecase import LoginUseCaseProvider
from infra.ioc.providers.auth.usecase import RefreshUseCaseProvider
from infra.ioc.providers.auth.usecase import RegistrationUseCaseProvider
from infra.ioc.providers.db import SQLAlchemyProvider
from infra.ioc.providers.matrix.repo import UserMatrixRepoProvider
from infra.ioc.providers.matrix.usecase import UserMatrixUseCaseProvider
from infra.ioc.providers.user.repo import UserRepoProvider


def init_di(app: FastAPI) -> None:
    # Incompatible with pyright - in issue recomend change pyright to mypy
    # Issue: https://github.com/pydantic/pydantic-settings/issues/383

    container = make_async_container(
        DBConfigProvider(),
        AuthConfigProvider(),
        SQLAlchemyProvider(),
        AuthRepoProvider(),
        RegistrationUseCaseProvider(),
        TokenServiceProvider(),
        RefreshUseCaseProvider(),
        LoginUseCaseProvider(),
        LoginUserRepositoryProvider(),
        UserMatrixRepoProvider(),
        UserMatrixUseCaseProvider(),
        UserRepoProvider(),
        context={
            DatabaseConnectConfig: DatabaseConnectConfig(),  # pyright: ignore[reportCallIssue]
            AuthTokenSettings: AuthTokenSettings(),  # pyright: ignore[reportCallIssue]
        },
    )
    setup_dishka(container, app)

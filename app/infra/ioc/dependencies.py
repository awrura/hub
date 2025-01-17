from config.db import DatabaseConnectConfig
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI
from infra.ioc.cfg import ApplicationConfigProvider
from infra.ioc.providers.auth.repo import AuthRepoProvider
from infra.ioc.providers.auth.usecase import RegistrationUseCaseProvider
from infra.ioc.providers.db import SQLAlchemyProvider


def init_di(app: FastAPI) -> None:
    # Incompatible with pyright - in issue recomend change pyright to mypy
    # Issue: https://github.com/pydantic/pydantic-settings/issues/383

    container = make_async_container(
        ApplicationConfigProvider(),
        SQLAlchemyProvider(),
        AuthRepoProvider(),
        RegistrationUseCaseProvider(),
        context={
            DatabaseConnectConfig: DatabaseConnectConfig(
                HOST='', PORT=1, USER='', PASS=''
            )
        },
    )
    setup_dishka(container, app)

from collections.abc import AsyncGenerator

from config.db import DatabaseConnectConfig
from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider
from matrix.model.entity.matrix import Matrix
from matrix.model.entity.user_matrix import UserMatrix
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy.ext.asyncio.session import AsyncSession
from user.model.entity.user import User


def get_connection_url(cfg: DatabaseConnectConfig) -> str:
    return 'sqlite+aiosqlite:///:memory:'


async def init_db(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Matrix.metadata.create_all)
        await conn.run_sync(User.metadata.create_all)
        await conn.run_sync(UserMatrix.metadata.create_all)


class SQLAlchemyProvider(Provider):
    @classmethod
    @provide(scope=Scope.APP)
    async def get_engine(cls, settings: DatabaseConnectConfig) -> AsyncEngine:
        database_url = get_connection_url(settings)
        database_params = {}
        engine = create_async_engine(database_url, **database_params)
        await init_db(engine)
        return engine

    @classmethod
    @provide(scope=Scope.REQUEST)
    async def get_session(
        cls, engine: AsyncEngine
    ) -> AsyncGenerator[AsyncSession, None]:
        async_session = async_sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )
        async with async_session() as session:
            yield session

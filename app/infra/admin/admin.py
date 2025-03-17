import logging

from fastapi import FastAPI
from infra.admin.view.matrix import MatrixAdminView
from sqladmin import Admin
from sqlalchemy.ext.asyncio import AsyncEngine

logger = logging.getLogger(__name__)


async def init_admin(app: FastAPI):
    container = app.state.dishka_container
    engine = await container.get(AsyncEngine)

    admin = Admin(app, engine)
    admin.add_view(MatrixAdminView)

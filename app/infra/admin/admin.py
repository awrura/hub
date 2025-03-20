import logging

from config.auth import AdminAuthSettings
from fastapi import FastAPI
from infra.admin.auth import AdminAuth
from infra.admin.view.matrix import MatrixAdminView
from infra.admin.view.user import UserAdminView
from infra.admin.view.user_matrix import UserMatrixAdminView
from sqladmin import Admin
from sqlalchemy.ext.asyncio import AsyncEngine

logger = logging.getLogger(__name__)


async def init_admin(app: FastAPI, engine: AsyncEngine, cfg: AdminAuthSettings):
    """
    Регистрация представлений админки
    """

    authentication_backend = AdminAuth(cfg)
    admin = Admin(app, engine, authentication_backend=authentication_backend)
    admin.add_view(MatrixAdminView)
    admin.add_view(UserAdminView)
    admin.add_view(UserMatrixAdminView)

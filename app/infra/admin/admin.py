import logging

from fastapi import FastAPI
from infra.admin.view.matrix import MatrixAdminView
from infra.admin.view.user import UserAdminView
from infra.admin.view.user_matrix import UserMatrixAdminView
from sqladmin import Admin
from sqlalchemy.ext.asyncio import AsyncEngine

logger = logging.getLogger(__name__)


async def init_admin(app: FastAPI, engine: AsyncEngine):
    """
    Регистрация представлений админки
    """

    admin = Admin(app, engine)
    admin.add_view(MatrixAdminView)
    admin.add_view(UserAdminView)
    admin.add_view(UserMatrixAdminView)

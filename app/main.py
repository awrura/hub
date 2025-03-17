import logging
from contextlib import asynccontextmanager

from auth.api.routes.auth import router as auth_router
from dishka.integrations.fastapi import inject
from fastapi import FastAPI
from infra.admin.admin import init_admin
from infra.exc_handler import setup_exception_handlers
from infra.ioc.dependencies import init_di
from matrix.api.routes.user_matrix import router as user_matrix_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_admin(app)
    yield


logger = logging.getLogger(__name__)
app = FastAPI(lifespan=lifespan)
init_di(app)
setup_exception_handlers(app)

app.include_router(auth_router)
app.include_router(user_matrix_router)


@app.get('/')
@inject
async def root():
    return {'message': 'Hello World'}

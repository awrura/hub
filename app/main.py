import logging
from typing import Annotated

from auth.api.routes.auth import router as auth_router
from auth.dto.auth import AuthUser
from auth.util.access import authuser_from_token
from dishka.integrations.fastapi import inject
from fastapi import Depends
from fastapi import FastAPI
from infra.exc_handler import setup_exception_handlers
from infra.ioc.dependencies import init_di


logger = logging.getLogger(__name__)
app = FastAPI()
init_di(app)
setup_exception_handlers(app)
app.include_router(auth_router)

logger.info('Hello world')


@app.get('/')
@inject
async def root(auth_user: Annotated[AuthUser, Depends(authuser_from_token)]):
    logger.info(auth_user)
    return {'message': 'Hello World'}

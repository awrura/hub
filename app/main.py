import logging

from auth.api.routes.auth import router as auth_router
from dishka.integrations.fastapi import inject
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
async def root():
    return {'message': 'Hello World'}

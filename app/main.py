import logging
import uuid

from auth.action.store.auth import IAuthUserRepository
from auth.dto.register import RegisterUserDTO
from dishka.integrations.fastapi import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import FastAPI
from infra.ioc.dependencies import init_di

logger = logging.getLogger(__name__)
app = FastAPI()
init_di(app)
logger.info('Hello world')


@app.get('/')
@inject
async def root(repo: FromDishka[IAuthUserRepository]):
    dto = RegisterUserDTO(
        uuid=uuid.uuid4(), username='twoics', password=bytes([1, 2, 3, 4])
    )
    await repo.create_user(dto)
    return {'message': f'Hello World {repo}'}

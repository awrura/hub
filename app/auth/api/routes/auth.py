from auth.action.usecase.register import RegistrationUseCase
from auth.api.schema.register import RegisterUserInputSchema
from auth.dto.register import ToRegisterUserDTO
from dishka.integrations.fastapi import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import status
from fastapi.routing import APIRouter

router = APIRouter(tags=['Auth'], prefix='/auth')


@router.post('/register', status_code=status.HTTP_201_CREATED)
@inject
async def register(
    userinfo: RegisterUserInputSchema,
    interactor: FromDishka[RegistrationUseCase],
):
    await interactor.exec(
        user=ToRegisterUserDTO(
            username=userinfo.username,
            password=userinfo.password,
            pass_confirm=userinfo.pass_confirm,
        )
    )

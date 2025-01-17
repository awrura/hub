from auth.action.usecase.login import UserLoginUseCase
from auth.action.usecase.login import UserRefreshUseCase
from auth.action.usecase.register import RegistrationUseCase
from auth.api.schema.login import RefreshToken
from auth.api.schema.login import UserLoginCred
from auth.api.schema.login import UserTokens
from auth.api.schema.register import RegisterUserInputSchema
from auth.dto.login import ToLoginUserDTO
from auth.dto.register import ToRegisterUserDTO
from dishka.integrations.fastapi import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import status
from fastapi.responses import Response
from fastapi.routing import APIRouter

router = APIRouter(tags=['Auth'], prefix='/auth')


@router.post('/register')
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

    return Response(status_code=status.HTTP_201_CREATED)


@router.post('/login')
@inject
async def login(
    user_cred: UserLoginCred, interactor: FromDishka[UserLoginUseCase]
) -> UserTokens:
    tokens = await interactor.login(
        user_info=ToLoginUserDTO(
            username=user_cred.username, password=user_cred.password
        )
    )

    return UserTokens(access=tokens.access, refresh=tokens.refresh)


@router.post('/refresh')
@inject
async def refresh(
    refresh_token: RefreshToken, interactor: FromDishka[UserRefreshUseCase]
) -> UserTokens:
    tokens = interactor.refresh(refresh_token.refresh_token)
    return UserTokens(access=tokens.access, refresh=tokens.refresh)

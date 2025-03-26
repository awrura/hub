from typing import List

from auth.util.access import user_from_token
from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Depends
from fastapi import status
from fastapi.responses import Response
from fastapi.routing import APIRouter
from matrix.action.usecase.secret_key import UserMatrixSecretkeyUseCase
from matrix.action.usecase.user_matrix import UserMatrixUseCase
from matrix.api.schema.user_matrix import UserMatrixOutSchema
from user.domain.user import User

router = APIRouter(tags=['Matrix'], prefix='/matrix')


@router.get('/my')
@inject
async def my_matrix(
    interactor: FromDishka[UserMatrixUseCase],
    user: User = Depends(user_from_token),
) -> List[UserMatrixOutSchema]:
    matrices = await interactor.get_user_matrices(user)

    return [
        UserMatrixOutSchema(name=matrix.name, height=matrix.height, width=matrix.width)
        for matrix in matrices
    ]


@router.post('/add/{secret}')
@inject
async def add_user_matrix(
    secret: str,
    interactor: FromDishka[UserMatrixSecretkeyUseCase],
    user: User = Depends(user_from_token),
):
    sucsess = await interactor.add_matrix_to_user(user, secret)
    if sucsess:
        return Response(status_code=status.HTTP_201_CREATED)
    return Response(status_code=status.HTTP_400_BAD_REQUEST)

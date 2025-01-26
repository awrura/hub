from typing import List

from auth.util.access import user_from_token
from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Depends
from fastapi.routing import APIRouter
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

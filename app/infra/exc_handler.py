from functools import partial

from auth.exception.login import UserNotFoundError
from auth.exception.login import WrongUserPasswordError
from auth.exception.register import BaseAuthUserError
from auth.exception.register import InvalidPasswordConfirmError
from auth.exception.register import UserAlreadyRegisteredError
from fastapi import status
from fastapi.applications import FastAPI
from fastapi.responses import JSONResponse


def exception_handler(_, exc, status):
    return JSONResponse(content={'error': exc.message}, status_code=status)


def handler_factory(status_code: int):
    return partial(exception_handler, status=status_code)


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(
        UserAlreadyRegisteredError, handler_factory(status.HTTP_400_BAD_REQUEST)
    )
    app.add_exception_handler(
        InvalidPasswordConfirmError, handler_factory(status.HTTP_400_BAD_REQUEST)
    )
    app.add_exception_handler(
        BaseAuthUserError, handler_factory(status.HTTP_500_INTERNAL_SERVER_ERROR)
    )
    app.add_exception_handler(
        UserNotFoundError, handler_factory(status.HTTP_404_NOT_FOUND)
    )
    app.add_exception_handler(
        WrongUserPasswordError, handler_factory(status.HTTP_400_BAD_REQUEST)
    )

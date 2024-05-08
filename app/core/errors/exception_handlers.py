from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.core.errors.api_exception import APIException
from app.core.errors.responses import JSONErrorResponse
from app.core.schema.error import ErrorDataSchema, ErrorResponseSchema


async def http_exception_handler(
    request: Request, exc: APIException
) -> JSONErrorResponse:
    error_response = ErrorResponseSchema(
        code=exc.code, data=ErrorDataSchema(error_message=exc.detail)
    )
    return JSONErrorResponse(
        err_response=error_response,
        code=exc.code,
        http_code=exc.status_code,
        headers=exc.headers,
    )


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONErrorResponse:
    _errors = exc.errors()
    err_msg = f"{len(_errors)} validation errors"

    error_response = ErrorResponseSchema(
        code=HTTP_422_UNPROCESSABLE_ENTITY,
        data=ErrorDataSchema(
            error_message=err_msg, details=jsonable_encoder(exc.errors())
        ),
    )
    return JSONErrorResponse(
        code=HTTP_422_UNPROCESSABLE_ENTITY,
        err_response=error_response,
        http_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )

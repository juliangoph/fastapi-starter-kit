from typing import Callable

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.core.errors import (
    http_exception_handler,
    request_validation_exception_handler,
)
from app.core.errors.api_exception import APIException


def create_fastapi_app(
    name: str,
    desc: str,
    prefix: str,
    cors_origin: str | list[str],
    debug: bool,
    lifespan: Callable,
) -> FastAPI:
    app = FastAPI(
        debug=debug,
        title=name,
        description=desc,
        openapi_url=f"{prefix}/openapi.json",
        lifespan=lifespan,
    )

    register_cors(app, cors_origin)
    register_exception(app)

    return app


def register_cors(app: FastAPI, origins: list[str]):
    # Set all CORS enabled origins
    if origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_exception(app: FastAPI):
    @app.exception_handler(APIException)
    async def custom_http_exception_handler(request, e):
        return await http_exception_handler(request, e)

    @app.exception_handler(RequestValidationError)
    async def custom_validation_exception_handler(request, e):
        return await request_validation_exception_handler(request, e)

from typing import Any, Optional

from app.core.schema import PydanticModel

from .base import BaseResponse


class ErrorDataSchema(PydanticModel):
    error_message: str = "Internal Server Error"
    details: Optional[Any]


class ErrorResponseSchema(BaseResponse):
    success: bool = False
    code: int = 50001
    data: Optional[ErrorDataSchema]

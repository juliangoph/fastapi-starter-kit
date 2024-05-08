from typing import Any, Dict, Optional

from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


class APIException(HTTPException):
    def __init__(
        self,
        msg: str,
        code: int,
        http_code: Optional[int] = HTTP_500_INTERNAL_SERVER_ERROR,
        headers: Optional[Dict[str, Any]] = None,
    ):
        self.detail = msg
        self.code = code
        self.status_code = http_code
        self.headers = headers

    def __str__(self):
        return self.detail

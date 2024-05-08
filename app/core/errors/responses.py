from typing import Any, Dict, Optional

from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from starlette.responses import JSONResponse

from app.core.schema.error import ErrorResponseSchema


class JSONErrorResponse(JSONResponse):
    def __init__(
        self,
        code: int,
        err_response: ErrorResponseSchema,
        http_code: int = HTTP_500_INTERNAL_SERVER_ERROR,
        headers: Optional[Dict[str, Any]] = None,
    ):
        err_response.code = code
        super(JSONErrorResponse, self).__init__(
            content=err_response.dict(), status_code=http_code, headers=headers
        )

from pydantic import field_validator
from typing import Optional
from app.core.schema import PydanticModel


class BaseResponse(PydanticModel):
    success: bool
    code: int


class LogData(PydanticModel):
    request_id: Optional[str]
    user_host: Optional[str]
    user_agent: Optional[str]
    path: Optional[str]
    method: Optional[str]
    path_params: Optional[dict]
    query_params: Optional[dict]
    payload: Optional[dict]
    request_data: Optional[str]
    response_data: Optional[str]
    response_code: Optional[int]
    response_time: Optional[int]

    class Config:
        validate_assignment = True

    @field_validator("request_data", mode="before")
    def prepare_request_data(cls, v, values):
        res = dict()
        if "path_params" in values and values["path_params"]:
            res["path_params"] = values["path_params"]
        if "query_params" in values and values["query_params"]:
            res["query_params"] = values["query_params"]
        if "payload" in values and values["payload"]:
            res["payload"] = values["payload"]
        return res or None

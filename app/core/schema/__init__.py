from pydantic import BaseModel


class PydanticModel(BaseModel):
    class Config:
        use_enum_values = True

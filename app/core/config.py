from pydantic import Field, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    PROJECT_NAME: str = "FastAPI Starter Kit"
    PROJECT_DESC: str = "A starter kit for FastAPI with SQLAlchemy"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    # CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    CORS_ORIGINS: str | list[str] = ["127.0.0.1", "0.0.0.0"]

    REDIS_HOST: str = Field(alias="REDIS_HOST")
    REDIS_PORT: str = Field(alias="REDIS_PORT")
    REDIS_PASS: str = Field(alias="REDIS_PASS")

    DB_HOST: str = Field(alias="DB_HOST")
    DB_PORT: int = Field(alias="DB_PORT")
    DB_NAME: str = Field(alias="POSTGRES_DB")
    DB_USERNAME: str = Field(alias="POSTGRES_USER")
    DB_PASSWORD: str = Field(alias="POSTGRES_PASSWORD")
    DB_URL: str = ""

    TIME_ZONE: str = Field(alias="TIME_ZONE")
    LOG_LEVEL: str = Field(alias="LOG_LEVEL")
    LOG_FORMAT: str = (
        "time: %(asctime)s | level: %(levelname)s | request_id: %(request_id)s | "
        "user_host: %(user_host)s | user_agent: %(user_agent)s | path: %(path)s | method: %(method)s | "
        "request_data: %(request_data)s | response_data: %(response_data)s | "
        "response_time: %(response_time)s | response_code: %(response_code)s | "
        "message: %(message)s"
    )

    @field_validator("DB_URL", mode="before")
    def prepare_db_url(cls, value, info: ValidationInfo):
        return (
            f"postgresql+asyncpg://{info.data.get('DB_USERNAME')}:{info.data.get('DB_PASSWORD')}"
            f"@{info.data.get('DB_HOST')}:{info.data.get('DB_PORT')}/{info.data.get('DB_NAME')}"
        )

    @field_validator("CORS_ORIGINS")
    def assemble_cors_origins(cls, v: str | list[str]):
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        raise ValueError(v)

    @field_validator("LOG_LEVEL")
    def validate_log_level(cls, v: str):
        if v not in [
            "TRACE",
            "DEBUG",
            "INFO",
            "SUCCESS",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ]:
            raise ValueError(
                "Should be one of these value: 'TRACE', 'DEBUG', 'INFO', 'SUCCESS', "
                "'WARNING', 'ERROR', 'CRITICAL'"
            )
        return v


settings = Settings()

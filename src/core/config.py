from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 7000


class Settings(BaseSettings):
    run_config: RunConfig = RunConfig()


settings = Settings()

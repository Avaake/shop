from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, MySQLDsn


BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 7000


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30


class DatabaseConfig(BaseModel):
    # "mysql+aiomysql://admin:22lolka8833@localhost:3306/test3"
    url: MySQLDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    db: DatabaseConfig
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()

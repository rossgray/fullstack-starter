from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./sqlite/dev.db"
    # SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"


settings = Settings()  # type: ignore

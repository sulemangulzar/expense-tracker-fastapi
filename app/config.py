from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    POSTGRES_SERVER: str | None = None
    POSTGRES_PORT: int | None = None
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_DB: str | None = None
    DATABASE_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file="./.env", env_ignore_empty=True, extra="ignore"
    )

    @property
    def database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        if self.POSTGRES_SERVER and self.POSTGRES_USER and self.POSTGRES_PASSWORD and self.POSTGRES_DB:
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT or 5432}/{self.POSTGRES_DB}"
            )
        return "sqlite+aiosqlite:///expense.db"


settings = DatabaseSettings()  # type: ignore

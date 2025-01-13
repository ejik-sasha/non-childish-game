from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_ASYNC(self) -> str:
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    model_config = SettingsConfigDict(env_file=r'C:\Users\pomaz\Documents\GitHub\non-childish-game-new\non-childish-game\.env')
settings = Settings()

engine = create_async_engine(settings.DATABASE_URL_ASYNC, echo=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
    )

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session
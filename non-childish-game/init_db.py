import asyncio
from shared.database import engine, Base
from auth_service.models.user import User
from game_service.models.character import Character

async def init_models():
    async with engine.begin as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_models())
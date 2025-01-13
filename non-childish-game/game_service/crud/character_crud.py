from sqlalchemy.ext.asyncio import AsyncSession
from game_service.models.character import Character
from sqlalchemy.future import select

async def create_character(user_id: int, character_name: str, db: AsyncSession):
    new_character = Character(user_id=user_id, name=character_name)
    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character

async def get_characters_by_user(user_id: int, db: AsyncSession):
    query = select(Character).where(Character.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()

from sqlalchemy.ext.asyncio import AsyncSession
from game_service.models.character import Character
from sqlalchemy.future import select
async def create_character(payload, db: AsyncSession) -> Character:
    new_character = Character(
        name=payload.name,
        class_type=payload.class_type,
        user_id=payload.user_id
    )
    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character

async def get_characters_by_user(user_id: int, db: AsyncSession):
    result = await db.execute(select(Character).filter(Character.user_id == user_id))
    return result.scalars().all()

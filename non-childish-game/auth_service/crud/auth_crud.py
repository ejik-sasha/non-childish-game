from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from auth_service.models.user import User

async def get_user_by_email(email: str, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

async def create_user(email: str, hashed_password: str, db: AsyncSession) -> User:
    new_user = User(email=email, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

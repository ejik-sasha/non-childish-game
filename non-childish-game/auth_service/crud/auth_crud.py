from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from auth_service.models.user import User
from passlib.hash import bcrypt
from auth_service.schemas.auth_schemas import UserCreate

async def get_user_by_email(email: str, db: AsyncSession):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def create_user(user_data: UserCreate, db: AsyncSession):
    password_hash = bcrypt.hash(user_data.password)
    new_user = User(
        email=user_data.email,
        username=user_data.username,
        password_hash=password_hash
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user(db: AsyncSession, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


async def get_all_users(db: AsyncSession):
    return db.query(User).all()


async def delete_user(db: AsyncSession, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
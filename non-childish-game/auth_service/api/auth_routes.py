from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from auth_service.schemas.auth_schemas import UserCreate, UserResponse
from auth_service.crud.auth_crud import *
from shared.database import get_db
from auth_service.utils.hash_utils import hash_password

auth_router = APIRouter()

@auth_router.post("/register")
async def register_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_email(payload.email, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = hash_password(payload.password)
    user = await create_user(payload.email, hashed_password, db)
    return {"id": user.id, "email": user.email}

@auth_router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)


@auth_router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

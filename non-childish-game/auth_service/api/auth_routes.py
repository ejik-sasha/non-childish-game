from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from auth_service.schemas.auth_schemas import RegisterSchema
from auth_service.crud.auth_crud import create_user, get_user_by_email
from shared.database import get_db
from auth_service.utils.hash_utils import hash_password

router = APIRouter()

@router.post("/register")
async def register_user(payload: RegisterSchema, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_email(payload.email, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = hash_password(payload.password)
    user = await create_user(payload.email, hashed_password, db)
    return {"id": user.id, "email": user.email}

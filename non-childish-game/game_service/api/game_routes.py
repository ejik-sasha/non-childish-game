from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from shared.database import get_db
from game_service.crud.character_crud import create_character
from pydantic import BaseModel

class CreateCharacterRequest(BaseModel):
    user_id: int
    name: str

game_router = APIRouter()

@game_router.post("/create-character")
async def create_character_for_user(character: CreateCharacterRequest, db: AsyncSession = Depends(get_db)):
    new_character = await create_character(character.user_id, character.name, db)
    return {"id": new_character.id, "name": new_character.name}

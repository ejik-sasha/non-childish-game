from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from shared.database import get_db
from game_service.crud.character_crud import *
from game_service.schemas.game_schemas import *
from game_service.utils.game_logic import *
from pydantic import BaseModel

class CreateCharacterRequest(BaseModel):
    user_id: int
    name: str

game_router = APIRouter()

@game_router.post("/create-character")
async def create_character_for_user(character: CreateCharacterRequest, db: AsyncSession = Depends(get_db)):
    new_character = await create_character(character.user_id, character.name, db)
    return {"id": new_character.id, "name": new_character.name}

@game_router.post("/characters", response_model=CharacterResponse)
async def create_character(character: CharacterCreate, db: AsyncSession = Depends(get_db)):
    user = get_character(db, user_id=1)  # Для теста используем user_id=1
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return create_character(db, character, user.id)


@game_router.get("/characters/{character_id}", response_model=CharacterResponse)
async def read_character(character_id: int, db: AsyncSession = Depends(get_db)):
    character = get_character(db, character_id=character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@game_router.post("/characters/{character_id}/level-up")
async def level_up_character(character_id: int, experience: int, db: AsyncSession = Depends(get_db)):
    character = get_character(db, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    leveled_up = level_up(character, experience)
    db.commit()
    if leveled_up:
        return {"message": "Character leveled up!", "level": character.level}
    return {"message": "Experience added, but no level up yet."}

@game_router.post("/characters/{character_id}/gather")
async def gather(character_id: int, resource_type: str, base_amount: float, db: AsyncSession = Depends(get_db)):
    character = get_character(db, character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    total_amount = gather_resources(character, resource_type, base_amount)
    update_resource_amount(db, character_id, resource_type, total_amount)
    return {"message": f"Gathered {total_amount} of {resource_type}"}

@game_router.post("/fight")
async def fight_endpoint(player_id: int, opponent_id: int, db: AsyncSession = Depends(get_db)):
    player = get_character(db, player_id)
    opponent = get_character(db, opponent_id)

    if not player or not opponent:
        raise HTTPException(status_code=404, detail="One or both characters not found")

    result = fight(player, opponent)
    db.commit()
    return {"result": result}


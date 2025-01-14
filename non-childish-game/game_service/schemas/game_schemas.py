from pydantic import BaseModel
from typing import List, Optional

class CharacterBase(BaseModel):
    name: str
    class_type: str

class CharacterCreate(CharacterBase):
    pass

class CharacterResponse(CharacterBase):
    id: int
    level: int
    intelligence: float
    strength: float
    agility: float
    gathering: float

    class Config:
        orm_mode = True


class ResourceResponse(BaseModel):
    resource_type: str
    amount: float

    class Config:
        orm_mode = True

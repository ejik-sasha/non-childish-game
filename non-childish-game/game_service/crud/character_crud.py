from sqlalchemy.ext.asyncio import AsyncSession
from game_service.models.character import Character
from game_service.models.resource import Resource
from game_service.models.alliance import Alliance

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

def get_character(db: AsyncSession, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()


def get_all_characters(db: AsyncSession):
    return db.query(Character).all()


def update_character_level(db: AsyncSession, character_id: int, new_level: int):
    character = db.query(Character).filter(Character.id == character_id).first()
    if character:
        character.level = new_level
        db.commit()
        db.refresh(character)
        return character
    return None


def delete_character(db: AsyncSession, character_id: int):
    character = db.query(Character).filter(Character.id == character_id).first()
    if character:
        db.delete(character)
        db.commit()
        return True
    return False


def create_resource(db: AsyncSession, character_id: int, resource_type: str, amount: float):
    db_resource = Resource(
        resource_type=resource_type,
        amount=amount,
        character_id=character_id
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource


def get_resources_by_character(db: AsyncSession, character_id: int):
    return db.query(Resource).filter(Resource.character_id == character_id).all()


def update_resource_amount(db: AsyncSession, character_id: int, resource_type: str, amount: float):
    resource = db.query(Resource).filter(Resource.character_id == character_id, Resource.resource_type == resource_type).first()
    if resource:
        resource.amount += amount
        db.commit()
        db.refresh(resource)
        return resource
    return None


def delete_resource(db: AsyncSession, resource_id: int):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if resource:
        db.delete(resource)
        db.commit()
        return True
    return False


def create_alliance(db: AsyncSession, name: str, description: str):
    db_alliance = Alliance(name=name, description=description)
    db.add(db_alliance)
    db.commit()
    db.refresh(db_alliance)
    return db_alliance


def get_alliance(db: AsyncSession, alliance_id: int):
    return db.query(Alliance).filter(Alliance.id == alliance_id).first()


def get_all_alliances(db: AsyncSession):
    return db.query(Alliance).all()


def add_character_to_alliance(db: AsyncSession, alliance_id: int, character_id: int):
    alliance = db.query(Alliance).filter(Alliance.id == alliance_id).first()
    character = db.query(Character).filter(Character.id == character_id).first()
    if alliance and character:
        alliance.members.append(character)
        db.commit()
        db.refresh(alliance)
        return alliance
    return None

def remove_character_from_alliance(db: AsyncSession, alliance_id: int, character_id: int):
    alliance = db.query(Alliance).filter(Alliance.id == alliance_id).first()
    character = db.query(Character).filter(Character.id == character_id).first()
    if alliance and character:
        alliance.members.remove(character)
        db.commit()
        return True
    return False


def delete_alliance(db: AsyncSession, alliance_id: int):
    alliance = db.query(Alliance).filter(Alliance.id == alliance_id).first()
    if alliance:
        db.delete(alliance)
        db.commit()
        return True
    return False
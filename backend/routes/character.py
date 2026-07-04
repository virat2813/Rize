from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import CharacterStats

router = APIRouter()


@router.get("/character")
def get_character(db: Session = Depends(get_db)):
    character = (
        db.query(CharacterStats)
        .filter(CharacterStats.user_id == 1)
        .first()
    )

    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")

    calculated_level = (character.total_xp // 100) + 1

    if character.level != calculated_level:
        character.level = calculated_level
        db.commit()
        db.refresh(character)

    return {
        "id": character.id,
        "user_id": character.user_id,
        "level": character.level,
        "total_xp": character.total_xp,
        "confidence": character.confidence,
        "knowledge": character.knowledge,
        "fitness": character.fitness,
        "creativity": character.creativity,
        "social": character.social,
    }

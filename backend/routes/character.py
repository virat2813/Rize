from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from decay import apply_stat_decay
from models import CharacterStats

router = APIRouter()


@router.get("/character")
def get_character(db: Session = Depends(get_db)):
    apply_stat_decay(user_id=1, db=db)

    character = (
        db.query(CharacterStats)
        .filter(CharacterStats.user_id == 1)
        .first()
    )

    if not character:
        raise HTTPException(
            status_code=404,
            detail="Character not found",
        )

    calculated_level = (character.total_xp // 100) + 1

    if character.level != calculated_level:
        character.level = calculated_level
        db.commit()
        db.refresh(character)

    return {
        "id": character.id,
        "user_id": character.user_id,
        "confidence": character.confidence,
        "knowledge": character.knowledge,
        "fitness": character.fitness,
        "creativity": character.creativity,
        "social": character.social,
        "level": character.level,
        "total_xp": character.total_xp,
    }

@router.get("/streaks")
def get_streaks(db: Session = Depends(get_db)):
    from models import Streak

    streaks = (
        db.query(Streak)
        .filter(Streak.user_id == 1)
        .all()
    )

    return [
        {
            "id": streak.id,
            "stat_name": streak.stat_name,
            "current_streak": streak.current_streak,
            "longest_streak": streak.longest_streak,
            "last_completed_date": (
                streak.last_completed_date.isoformat()
                if streak.last_completed_date
                else None
            ),
        }
        for streak in streaks
    ]

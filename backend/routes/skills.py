from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import CharacterStats, Skill, UnlockedSkill


router = APIRouter(tags=["Skills"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/skills")
def get_skills(db: Session = Depends(get_db)):
    demo_user_id = 1

    character = (
        db.query(CharacterStats)
        .filter(CharacterStats.user_id == demo_user_id)
        .first()
    )

    character_level = 1

    if character:
        character_level = character.level

    unlocked_skill_ids = {
        unlocked.skill_id
        for unlocked in (
            db.query(UnlockedSkill)
            .filter(UnlockedSkill.user_id == demo_user_id)
            .all()
        )
    }

    skills = (
        db.query(Skill)
        .order_by(
            Skill.stat_name,
            Skill.unlock_level
        )
        .all()
    )

    response = []

    for skill in skills:
        level_requirement_met = character_level >= skill.unlock_level

        already_unlocked = skill.id in unlocked_skill_ids

        response.append(
            {
                "id": skill.id,
                "stat_name": skill.stat_name,
                "title": skill.title,
                "description": skill.description,
                "unlock_level": skill.unlock_level,
                "unlocked": level_requirement_met or already_unlocked
            }
        )

    return response
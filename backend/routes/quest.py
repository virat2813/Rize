from fastapi import APIRouter, Depends, Form, HTTPException
from pydantic import BaseModel
from sqlalchemy import or_
from sqlalchemy.orm import Session

from database import get_db
from models import CharacterStats, Completion, Quest

router = APIRouter()


class QuestCreate(BaseModel):
    title: str
    description: str
    linked_stat: str
    xp_reward: int


@router.get("/quests")
def get_quests(db: Session = Depends(get_db)):
    quests = (
        db.query(Quest)
        .filter(
            or_(
                Quest.is_preset == True,
                Quest.user_id == 1,
            )
        )
        .all()
    )

    return [
        {
            "id": quest.id,
            "title": quest.title,
            "description": quest.description,
            "linked_stat": quest.linked_stat,
            "xp_reward": quest.xp_reward,
            "is_preset": quest.is_preset,
            "user_id": quest.user_id,
        }
        for quest in quests
    ]


@router.post("/quests")
def create_quest(
    quest_data: QuestCreate,
    db: Session = Depends(get_db),
):
    quest = Quest(
        title=quest_data.title,
        description=quest_data.description,
        linked_stat=quest_data.linked_stat,
        xp_reward=quest_data.xp_reward,
        user_id=1,
        is_preset=False,
    )

    db.add(quest)
    db.commit()
    db.refresh(quest)

    return {
        "id": quest.id,
        "title": quest.title,
        "description": quest.description,
        "linked_stat": quest.linked_stat,
        "xp_reward": quest.xp_reward,
        "is_preset": quest.is_preset,
        "user_id": quest.user_id,
    }


@router.post("/quests/{quest_id}/complete")
def complete_quest(
    quest_id: int,
    proof_type: str = Form(...),
    proof_content: str = Form(...),
    db: Session = Depends(get_db),
):
    quest = db.query(Quest).filter(Quest.id == quest_id).first()

    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")

    character = (
        db.query(CharacterStats)
        .filter(CharacterStats.user_id == 1)
        .first()
    )

    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    previous_level = character.level

    completion = Completion(
        user_id=1,
        quest_id=quest.id,
        proof_type=proof_type,
        proof_content=proof_content,
        ai_verified=True,
        xp_earned=quest.xp_reward,
    )

    db.add(completion)

    stat = quest.linked_stat.lower()

    if stat == "confidence":
        character.confidence += quest.xp_reward
    elif stat == "knowledge":
        character.knowledge += quest.xp_reward
    elif stat == "fitness":
        character.fitness += quest.xp_reward
    elif stat == "creativity":
        character.creativity += quest.xp_reward
    elif stat == "social":
        character.social += quest.xp_reward

    character.total_xp += quest.xp_reward
    character.level = (character.total_xp // 100) + 1

    db.commit()
    db.refresh(character)

    return {
        "character": {
            "id": character.id,
            "user_id": character.user_id,
            "confidence": character.confidence,
            "knowledge": character.knowledge,
            "fitness": character.fitness,
            "creativity": character.creativity,
            "social": character.social,
            "total_xp": character.total_xp,
            "level": character.level,
        },
        "leveled_up": character.level > previous_level,
    }


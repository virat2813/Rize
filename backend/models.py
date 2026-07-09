from datetime import date, datetime

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    character_stats = relationship(
        "CharacterStats",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    quests = relationship(
        "Quest",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    completions = relationship(
        "Completion",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    streaks = relationship(
        "Streak",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    unlocked_skills = relationship(
        "UnlockedSkill",
        back_populates="user",
        cascade="all, delete-orphan"
    )

class CharacterStats(Base):
    __tablename__ = "character_stats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    confidence = Column(Integer, default=0, nullable=False)
    knowledge = Column(Integer, default=0, nullable=False)
    fitness = Column(Integer, default=0, nullable=False)
    creativity = Column(Integer, default=0, nullable=False)
    social = Column(Integer, default=0, nullable=False)

    level = Column(Integer, default=1, nullable=False)
    total_xp = Column(Integer, default=0, nullable=False)

    user = relationship(
        "User",
        back_populates="character_stats"
    )


class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)

    linked_stat = Column(String, nullable=False)

    xp_reward = Column(Integer, nullable=False)

    is_preset = Column(Boolean, default=False, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship(
        "User",
        back_populates="quests"
    )

    completions = relationship(
        "Completion",
        back_populates="quest",
        cascade="all, delete-orphan"
    )


class Completion(Base):
    __tablename__ = "completions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    quest_id = Column(
        Integer,
        ForeignKey("quests.id"),
        nullable=False
    )

    proof_type = Column(String, nullable=False)

    proof_content = Column(Text, nullable=False)

    ai_verified = Column(Boolean, default=False, nullable=False)

    ai_narration = Column(Text, nullable=True)

    xp_earned = Column(Integer, nullable=False)

    completed_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship(
        "User",
        back_populates="completions"
    )

    quest = relationship(
        "Quest",
        back_populates="completions"
    )


class Streak(Base):
    __tablename__ = "streaks"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    stat_name = Column(String, nullable=False)

    current_streak = Column(Integer, default=0, nullable=False)

    longest_streak = Column(Integer, default=0, nullable=False)

    last_completed_date = Column(Date, nullable=True)

    user = relationship(
        "User",
        back_populates="streaks"
    )

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    stat_name = Column(String, nullable=False)

    title = Column(String, nullable=False)

    description = Column(Text, nullable=False)

    unlock_level = Column(Integer, nullable=False)

    unlocked_users = relationship(
        "UnlockedSkill",
        back_populates="skill",
        cascade="all, delete-orphan"
    )


class UnlockedSkill(Base):
    __tablename__ = "unlocked_skills"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        nullable=False
    )

    unlocked_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="unlocked_skills"
    )

    skill = relationship(
        "Skill",
        back_populates="unlocked_users"
    )
from models import User, CharacterStats, Quest, Skill
from database import Base, SessionLocal, engine


def seed_database():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        demo_user = (
            db.query(User)
            .filter(User.email == "demo@rize.app")
            .first()
        )

        if demo_user is None:
            demo_user = User(
                id=1,
                email="demo@rize.app",
                hashed_password="placeholder_hashed_password",
                display_name="Preetansh"
            )
            db.add(demo_user)
            db.commit()
            db.refresh(demo_user)

        character = (
            db.query(CharacterStats)
            .filter(CharacterStats.user_id == demo_user.id)
            .first()
        )

        if character is None:
            character = CharacterStats(
                user_id=demo_user.id,
                confidence=0,
                knowledge=0,
                fitness=0,
                creativity=0,
                social=0,
                level=1,
                total_xp=0
            )
            db.add(character)
            db.commit()

        preset_exists = (
            db.query(Quest)
            .filter(Quest.is_preset == True)
            .first()
        )

        if preset_exists is None:
            preset_quests = [
                Quest(
                    title="Read for 30 minutes",
                    description="Read any book or educational material for at least 30 minutes.",
                    linked_stat="knowledge",
                    xp_reward=30,
                    is_preset=True
                ),
                Quest(
                    title="Workout",
                    description="Complete a workout or exercise session.",
                    linked_stat="fitness",
                    xp_reward=50,
                    is_preset=True
                ),
                Quest(
                    title="Draw something",
                    description="Spend time creating a drawing or sketch.",
                    linked_stat="creativity",
                    xp_reward=25,
                    is_preset=True
                ),
                Quest(
                    title="Talk to someone new",
                    description="Start a conversation with someone you haven't spoken to before.",
                    linked_stat="social",
                    xp_reward=40,
                    is_preset=True
                ),
                Quest(
                    title="Try something that scares you",
                    description="Step outside your comfort zone with a challenging activity.",
                    linked_stat="confidence",
                    xp_reward=45,
                    is_preset=True
                ),
                Quest(
                    title="Practice a skill for 20 minutes",
                    description="Practice a skill you want to improve for at least 20 minutes.",
                    linked_stat="knowledge",
                    xp_reward=25,
                    is_preset=True
                )
            ]

            db.add_all(preset_quests)
            db.commit()

        skills_exist = db.query(Skill).first()

        if skills_exist is None:
            skills = [
                Skill(
                    stat_name="confidence",
                    title="Bold Voice",
                    description="Gain confidence when taking initiative.",
                    unlock_level=2
                ),
                Skill(
                    stat_name="confidence",
                    title="Fearless Action",
                    description="Face uncomfortable challenges with greater resolve.",
                    unlock_level=8
                ),
                Skill(
                    stat_name="confidence",
                    title="Unbreakable Will",
                    description="Remain calm and determined under pressure.",
                    unlock_level=18
                ),

                Skill(
                    stat_name="knowledge",
                    title="Quick Learner",
                    description="Absorb new ideas more efficiently.",
                    unlock_level=3
                ),
                Skill(
                    stat_name="knowledge",
                    title="Deep Thinker",
                    description="Understand complex topics with greater clarity.",
                    unlock_level=10
                ),
                Skill(
                    stat_name="knowledge",
                    title="Master Scholar",
                    description="Develop exceptional learning discipline.",
                    unlock_level=20
                ),

                Skill(
                    stat_name="fitness",
                    title="Strong Foundation",
                    description="Build consistency through regular exercise.",
                    unlock_level=4
                ),
                Skill(
                    stat_name="fitness",
                    title="Peak Conditioning",
                    description="Improve endurance and physical resilience.",
                    unlock_level=12
                ),
                Skill(
                    stat_name="fitness",
                    title="Elite Athlete",
                    description="Reach your highest level of physical performance.",
                    unlock_level=19
                ),

                Skill(
                    stat_name="creativity",
                    title="Creative Spark",
                    description="Generate fresh ideas with ease.",
                    unlock_level=5
                ),
                Skill(
                    stat_name="creativity",
                    title="Inspired Mind",
                    description="Maintain creative momentum on difficult projects.",
                    unlock_level=11
                ),
                Skill(
                    stat_name="creativity",
                    title="Master Creator",
                    description="Express your ideas with confidence and originality.",
                    unlock_level=17
                ),

                Skill(
                    stat_name="social",
                    title="Friendly Presence",
                    description="Connect with new people more naturally.",
                    unlock_level=6
                ),
                Skill(
                    stat_name="social",
                    title="Trusted Ally",
                    description="Build stronger and more meaningful relationships.",
                    unlock_level=14
                ),
                Skill(
                    stat_name="social",
                    title="Community Leader",
                    description="Inspire and support those around you.",
                    unlock_level=20
                )
            ]

            db.add_all(skills)
            db.commit()

        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()


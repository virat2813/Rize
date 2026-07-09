from datetime import date

from models import CharacterStats, Streak


def apply_stat_decay(user_id, db):
    character = (
        db.query(CharacterStats)
        .filter(CharacterStats.user_id == user_id)
        .first()
    )

    if character is None:
        return

    streaks = (
        db.query(Streak)
        .filter(Streak.user_id == user_id)
        .all()
    )

    today = date.today()

    for streak in streaks:
        if streak.last_completed_date is None:
            continue

        days_since_completion = (
            today - streak.last_completed_date
        ).days

        if days_since_completion >= 4:
            stat_name = streak.stat_name.lower()

            if hasattr(character, stat_name):
                current_value = getattr(character, stat_name)
                updated_value = max(0, current_value - 5)
                setattr(character, stat_name, updated_value)

    db.commit()

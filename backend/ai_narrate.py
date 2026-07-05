import os

from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"


def generate_narration(quest_title, linked_stat):
    """
    Generate a short encouraging narration after a quest completion.

    Returns:
        str
    """

    try:
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = f"""
The user has just completed a personal growth quest.

Quest:
{quest_title}

Related Area:
{linked_stat}

Write exactly one sentence.

Rules:
- Under 15 words.
- Calm and encouraging.
- Sounds like a personal growth journal.
- No fantasy.
- No RPG language.
- No medieval words.
- Return only the sentence.
"""

        response = model.generate_content(prompt)

        narration = response.text.strip()

        if narration.startswith("```"):
            lines = narration.splitlines()

            if lines[0].startswith("```"):
                lines = lines[1:]

            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]

            narration = "\n".join(lines).strip()

        return narration

    except Exception:
        return "Well done, that is progress."
    
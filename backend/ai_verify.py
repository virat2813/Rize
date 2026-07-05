import json
import os
import traceback

from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"


def verify_photo_proof(image_bytes, quest_title, linked_stat):
    """
    Verify whether an uploaded image plausibly proves completion of a quest.

    Returns:
        {
            "accepted": bool,
            "reason": str
        }
    """

    try:
        model = genai.GenerativeModel(MODEL_NAME)

        prompt = f"""
You are verifying photo proof for a self-improvement quest.

Quest Title:
{quest_title}

Related Stat:
{linked_stat}

Determine whether this image plausibly shows evidence that the quest was completed.

Respond ONLY as valid JSON in exactly this format:

{{
  "accepted": true,
  "reason": "One short sentence."
}}

Rules:
- accepted must be true or false.
- Be reasonably strict.
- The reason must be one short sentence.
- Do not include markdown.
- Do not include any extra text.
"""

        response = model.generate_content(
            [
                prompt,
                {
                    "mime_type": "image/jpeg",
                    "data": image_bytes,
                },
            ]
        )

        text = response.text.strip()

        if text.startswith("```"):
            lines = text.splitlines()

            if lines[0].startswith("```"):
                lines = lines[1:]

            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]

            text = "\n".join(lines).strip()

        result = json.loads(text)

        accepted = bool(result.get("accepted", False))
        reason = str(result.get("reason", "")).strip()

        if not reason:
            reason = (
                "The image appears to match the quest."
                if accepted
                else "The image does not clearly match the quest."
            )

        return {
            "accepted": accepted,
            "reason": reason,
        }

    except Exception as e:
        print("\n========== GEMINI ERROR ==========")
        traceback.print_exc()
        print("==================================\n")

        return {
            "accepted": False,
            "reason": str(e),
        }
    

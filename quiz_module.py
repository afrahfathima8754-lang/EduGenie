import os
from dotenv import load_dotenv
from google import genai
import json
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz(passage: str):
    prompt = f"""
Create 3 multiple-choice questions from this passage.

For each question give:
- question
- 4 options
- correct answer

Return only valid JSON.

Passage:
{passage}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {"error": str(e)}

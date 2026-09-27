import os
from dotenv import load_dotenv
from google import genai
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_question(question: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

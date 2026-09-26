from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

def create_learning_path(topic: str) -> str:
    prompt = f"""
Create a simple learning path for the topic: {topic}

Include:
1. Beginner level
2. Intermediate level
3. Advanced level
4. Useful learning resources

Keep it clear and easy to understand.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {e}"
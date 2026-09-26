from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

def summarize_text(text: str) -> str:
    try:
        prompt = f"""
Summarize the following text in simple language:

{text}
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {e}"
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(message: str, language: str = "en") -> str:
    if language == "hi":
        prompt = f"""
आप एक कृषि विशेषज्ञ हैं।
किसान की मदद सरल भाषा में करें।
उत्तर हिंदी में दें।

प्रश्न:
{message}
"""
    else:
        prompt = f"""
You are an agriculture expert.
Answer clearly and simply for farmers.

Question:
{message}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()

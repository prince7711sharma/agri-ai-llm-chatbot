import os
import re
from dotenv import load_dotenv
from groq import Groq
from app.core.prompt import build_prompt

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def clean_and_number(text: str) -> str:
    lines = text.split("\n")
    output = []
    num = 1

    for line in lines:
        line = line.strip()

        # skip empty lines but keep spacing
        if not line:
            output.append("")
            continue

        # remove all markdown symbols
        line = re.sub(r"\*\*", "", line)   # **
        line = re.sub(r"\*", "", line)     # *
        line = re.sub(r"_", "", line)      # _
        line = re.sub(r"`", "", line)      # `
        line = re.sub(r"-", "", line)      # -

        # if line looks like a point → convert to number
        if (
            line.startswith("•")
            or line.startswith("–")
            or re.match(r"\d+\.", line)
        ):
            line = re.sub(r"^\d+\.\s*", "", line)
            line = f"{num}. {line}"
            num += 1

        output.append(line)

    return "\n".join(output).strip()

def generate_answer(message: str, language: str, history: list) -> str:
    prompt = build_prompt(message, language, history)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    raw = response.choices[0].message.content
    return clean_and_number(raw)

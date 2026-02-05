# def build_prompt(message: str, language: str, history: list) -> str:
#     if language == "hi":
#         return f"""
# आप एक अनुभवी कृषि विशेषज्ञ हैं।
#
# नियम:
# - उत्तर हिंदी में दें
# - सरल भाषा का प्रयोग करें
# - बिंदुओं में जानकारी दें
# - व्यावहारिक सलाह दें
#
# प्रश्न:
# {message}
#
# उत्तर:
# """
#     else:
#         return f"""
# You are an agriculture expert.
#
# Rules:
# - Answer in English
# - Give information in points
# - Keep it practical
#
# Question:
# {message}
#
# Answer:
# """
def build_prompt(message: str, language: str, history: list) -> str:
    conversation = ""

    for msg in history:
        if language == "hi":
            role = "किसान" if msg["role"] == "user" else "एग्री असिस्टेंट"
        else:
            role = "Farmer" if msg["role"] == "user" else "Agri Assistant"

        conversation += f"{role}: {msg['content']}\n"

    if language == "hi":
        return f"""
आप Agri Assistant हैं – एक मित्रवत और अनुभवी कृषि सहायक।

निर्देश:
- उत्तर छोटे पैराग्राफ में दें
- 3 से 6 बिंदु दें
- हर बिंदु नई पंक्ति में हो
- हर बिंदु 1–2 वाक्य का हो
- सरल और दोस्ताना भाषा प्रयोग करें
- सटीक रासायनिक मात्रा न बताएं

पिछली बातचीत:
{conversation}

नया प्रश्न:
{message}

उत्तर:
"""
    else:
        return f"""
You are Agri Assistant – a friendly and experienced agriculture helper.

Rules:
- Write short paragraphs
- Give 3 to 6 numbered points
- Each point must be on a new line
- Each point should be 1–2 sentences
- Keep the tone friendly and practical
- Do NOT give exact chemical dosages

Previous conversation:
{conversation}

New question:
{message}

Answer:
"""

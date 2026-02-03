def build_prompt(message: str, language: str, history: list) -> str:
    if language == "hi":
        return f"""
आप एक अनुभवी कृषि विशेषज्ञ हैं।

नियम:
- उत्तर हिंदी में दें
- सरल भाषा का प्रयोग करें
- बिंदुओं में जानकारी दें
- व्यावहारिक सलाह दें

प्रश्न:
{message}

उत्तर:
"""
    else:
        return f"""
You are an agriculture expert.

Rules:
- Answer in English
- Give information in points
- Keep it practical

Question:
{message}

Answer:
"""

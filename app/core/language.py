# def detect_language(text: str) -> str:
#     for char in text:
#         if '\u0900' <= char <= '\u097F':
#             return "hi"
#     return "en"

def detect_language(text: str) -> str:
    text = text.lower()

    # Hindi (Devanagari)
    for char in text:
        if '\u0900' <= char <= '\u097F':
            return "hi"

    # Hinglish words
    hinglish_words = [
        "kya", "kaise", "kab", "fasal", "beej",
        "kheti", "pani", "barish", "mausam",
        "khad", "dawai", "rog"
    ]

    if any(word in text for word in hinglish_words):
        return "hi"

    return "en"

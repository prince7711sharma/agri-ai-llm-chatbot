# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.core.llm import generate_answer
# from app.core.language import detect_language
# from app.core.memory import add_message, get_history
#
# router = APIRouter()
#
# class ChatRequest(BaseModel):
#     message: str
#     session_id: str = "default"
#
# @router.post("/chat")
# def chat(request: ChatRequest):
#     language = detect_language(request.message)
#
#     history = get_history(request.session_id)
#
#     answer = generate_answer(
#         message=request.message,
#         language=language,
#         history=history
#     )
#
#     add_message(request.session_id, "user", request.message)
#     add_message(request.session_id, "assistant", answer)
#
#     return {
#         "reply": answer,
#         "language": language,
#         "source": "LLM"
#     }
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio

from app.core.llm import generate_answer
from app.core.language import detect_language
from app.core.memory import add_message, get_history

router = APIRouter(prefix="/chat", tags=["Agri Assistant"])


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


FRIENDLY_WORDS = [
    "hi", "hello", "hey", "good morning",
    "good evening", "namaste"
]


def is_friendly_message(text: str) -> bool:
    return any(word in text.lower() for word in FRIENDLY_WORDS)


@router.post("")
async def chat(request: ChatRequest):
    language = detect_language(request.message)

    # Greeting response (no streaming needed)
    if is_friendly_message(request.message):
        reply = (
            "Hello 👋 I am **Agri Assistant**.\n\n"
            "I help farmers with crop guidance, irrigation, "
            "fertilizer use, pest control, and weather-based advice.\n\n"
            "You can ask me questions in simple language 😊"
        )

        return {
            "reply": reply,
            "language": language,
            "suggestions": [
                "Ask about crop sowing time",
                "Ask about fertilizer guidance",
                "Ask about weather-based advice"
            ]
        }

    history = get_history(request.session_id)

    answer, suggestions = generate_answer(
        message=request.message,
        language=language,
        history=history
    )

    add_message(request.session_id, "user", request.message)
    add_message(request.session_id, "assistant", answer)

    async def streamer():
        for char in answer:
            yield char
            await asyncio.sleep(0.01)

        yield "\n__SUGGESTIONS__\n"
        for s in suggestions:
            yield s + "\n"

    return StreamingResponse(streamer(), media_type="text/plain")

from fastapi import APIRouter
from pydantic import BaseModel
from app.core.llm import generate_answer
from app.core.language import detect_language
from app.core.memory import add_message, get_history

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@router.post("/chat")
def chat(request: ChatRequest):
    language = detect_language(request.message)

    history = get_history(request.session_id)

    answer = generate_answer(
        message=request.message,
        language=language,
        history=history
    )

    add_message(request.session_id, "user", request.message)
    add_message(request.session_id, "assistant", answer)

    return {
        "reply": answer,
        "language": language,
        "source": "LLM"
    }

from fastapi import APIRouter
from pydantic import BaseModel
from app.core.llm import generate_answer

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    language: str = "en"   # en | hi

@router.post("/chat")
def chat(request: ChatRequest):
    answer = generate_answer(
        message=request.message,
        language=request.language
    )

    return {
        "reply": answer,
        "source": "LLM"
    }

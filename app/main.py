# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.api.chat import router as chat_router
#
# app = FastAPI(
#     title="Agri AI Chatbot v2",
#     version="2.0"
# )
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# app.include_router(chat_router, prefix="/api/v1")
#
# @app.get("/")
# def root():
#     return {"status": "Agri AI Chatbot v2 running"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router

app = FastAPI(
    title="Agri Assistant",
    description="Friendly AI-powered agriculture assistant for farmers",
    version="2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"status": "Agri Assistant running"}

@app.get("/health")
def health():
    return {"status": "ok"}
